import mysql.connector
from mysql.connector import Error
from data_ingestion.config import DB_CONFIG

def store_weather(data):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
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
    except Error as e:
        print(f"[DB ERROR] Failed to store data: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()