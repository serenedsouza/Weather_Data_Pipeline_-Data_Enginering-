# Weather_Data_Pipeline_Data_Enginering
Weather Data Pipeline – An end-to-end data engineering project that collects real-time weather data using OpenWeatherMap API, stores it in a MySQL database, and visualizes trends like temperature, humidity, and pressure across cities using a Streamlit dashboard.

## 📁 Project Structure
<pre>
weather_data_pipeline/
│
├── data_ingestion/
│ ├── fetch_weather.py # Fetches weather data from API
│ ├── store_to_mysql.py # Inserts data into MySQL
│ └── config.py # Stores API key and DB config
│
├── database/
│ └── schema.sql # MySQL schema definition
│
├── scheduler/
│ └── run_scheduler.py # Runs the fetch + store jobs hourly
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── .env # API key and DB credentials (not committed)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Files/folders to ignore
</pre>

---

## 🚀 Features

- ⛅ Pulls real-time weather data for multiple cities
- 🛢️ Stores data in a MySQL database
- 📊 Interactive dashboard using Streamlit
- 📅 Automatically scheduled pipeline using `schedule` library
- 🛠️ Modular folder structure for scalability

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/serenedsouza/Weather_Data_Pipeline_Data_Enginering.git  
cd Weather_Data_Pipeline_Data_Enginering

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure environment variables
Create a .env file in the root directory:  
- API_KEY=your_openweathermap_api_key  
- DB_HOST=localhost  
- DB_USER=your_user
- DB_PASSWORD=your_password  
- DB_NAME=weather_db  

### 4. Set up the MySQL database
Start MySQL server  
Run the schema: mysql -u <mysql_username> -p < database/schema.sql

## 🔄 Running the Pipeline
Run the scheduler to fetch and store weather data:  
python scheduler/run_scheduler.py

## 📈 Running the Dashboard
cd dashboard  
streamlit run app.py

## 📊 Dashboard Visualizations
KPIs for hottest, wettest, and most pleasant cities  
Bar charts for:
- Average temperature by city
- Average humidity by city
- Average pressure by city

Real-time weather data table

## 🛠️ Built With
- Python
- MySQL
- Streamlit
- Pandas
- OpenWeatherMap API
