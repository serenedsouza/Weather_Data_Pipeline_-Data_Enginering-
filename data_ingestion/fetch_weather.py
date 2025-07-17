import requests
import datetime
import mysql.connector
from mysql.connector import Error


# Replace with your credentials
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",  # Add your MySQL password if set
    database="weather_project"
)

def fetch_weather(city):
    API_KEY = "bb4ece27bae08d4477fede61690d4afe"  # Your OpenWeatherMap API key here
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for 4xx/5xx
        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["main"],
            "timestamp": datetime.datetime.now()
        }

    except requests.exceptions.Timeout:
        print(f"[ERROR] Timeout while fetching weather data for {city}.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch weather for {city}: {e}")
    
    return None  # Return nothing if fetch failed

def store_weather(data):
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO weather_data (city, temperature, humidity, pressure, weather, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data["city"],
            data["temperature"],
            data["humidity"],
            data["pressure"],
            data["weather"],
            data["timestamp"]
        )
        cursor.execute(sql, values)
        conn.commit()
        print(f"[INFO] Stored weather data for {data['city']} at {data['timestamp']}")

    except Error as e:  # ✅ Only catch MySQL-related errors
        print(f"[DB ERROR] Failed to store data: {e}")
        
def run_pipeline(cities):
    for city in cities:
        data = fetch_weather(city)
        if data:
            store_weather(data)

if __name__ == "__main__":
    # Add your target cities here
    city_list = ["Mumbai", "Delhi", "Chennai"]
    run_pipeline(city_list)
