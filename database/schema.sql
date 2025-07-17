CREATE DATABASE IF NOT EXISTS weather_project;

USE weather_project;

CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    weather VARCHAR(50),
    timestamp DATETIME
);