import schedule
import time
from data_ingestion.fetch_weather import fetch_weather
from data_ingestion.store_to_mysql import store_weather

def job():
    cities = ["Mumbai", "Delhi", "Chennai"]
    for city in cities:
        data = fetch_weather(city)
        if data:
            store_weather(data)

schedule.every(1).hour.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)