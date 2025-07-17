import streamlit as st
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from data_ingestion.config import DB_CONFIG
import matplotlib.pyplot as plt

st.set_page_config(page_title="🌦️ Weather Dashboard", layout="wide")

# Function to load data from MySQL using SQLAlchemy engine
def load_data():
    db_url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    engine = create_engine(db_url)
    query = "SELECT * FROM weather_data"
    return pd.read_sql(query, con=engine)

# Load data
try:
    df = load_data()
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

st.title("🌦️ Weather Dashboard")

# If no data yet
if df.empty:
    st.info("No data available yet. Please wait for the pipeline to collect some records.")
    st.stop()

# Convert timestamp to datetime if not already
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Get latest weather record per city
latest_df = df.sort_values("timestamp").groupby("city").tail(1)

# KPI Section
st.subheader("🌡️ Key Weather Indicators")

# Safely get city with highest temp/humidity
hottest = latest_df.sort_values("temperature", ascending=False).iloc[0]
coldest = latest_df.sort_values("temperature", ascending=True).iloc[0]
rainiest = latest_df.sort_values("humidity", ascending=False).iloc[0]
pleasant = latest_df.iloc[((latest_df["temperature"] - 24).abs() + (latest_df["humidity"] - 50).abs()).argsort().iloc[0]]

col1, col2, col3, col4 = st.columns(4)
col1.metric("🔥 Hottest City", hottest["city"], f"{hottest['temperature']}°C")
col2.metric("❄️ Coldest City", coldest["city"], f"{coldest['temperature']}°C")
col3.metric("💧 Most Humid", rainiest["city"], f"{rainiest['humidity']}%")
col4.metric("🌤️ Most Pleasant", pleasant["city"], f"{pleasant['temperature']}°C")

# Trend Graphs
st.subheader("📊 Weather Trends by City")

# Grouping by city
temp_by_city = df.groupby("city")["temperature"].mean().sort_values()
humidity_by_city = df.groupby("city")["humidity"].mean().sort_values()
pressure_by_city = df.groupby("city")["pressure"].mean().sort_values()

# Show bar charts in columns
col5, col6 = st.columns(2)

with col5:
    st.markdown("**🌡️ Average Temperature by City (°C)**")
    fig, ax = plt.subplots(figsize=(5, 3))
    temp_by_city.plot(kind="bar", color="coral", ax=ax)
    ax.set_title("Temperature")
    st.pyplot(fig)
with col6:
    st.markdown("**💧 Average Humidity by City (%)**")
    fig, ax = plt.subplots(figsize=(5, 3))
    humidity_by_city.plot(kind="bar", color="mediumseagreen", ax=ax)
    ax.set_title("Humidity")
    st.pyplot(fig)

_, col7, _ = st.columns([1, 2, 1])

with col7:
    st.markdown("**🧭 Average Pressure by City (hPa)**")
    fig, ax = plt.subplots(figsize=(5, 3))
    pressure_by_city.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_title("Pressure")
    st.pyplot(fig)
    
# Latest data table
st.subheader("🧾 Latest Weather Records")
st.table(latest_df.sort_values(by=["id", "timestamp"], ascending=[False, False]).reset_index(drop=True))
