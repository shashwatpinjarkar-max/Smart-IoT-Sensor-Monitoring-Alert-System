import random
import time
import sqlite3
from datetime import datetime

# Database setup (Cloud la MySQL vapru shakto)
conn = sqlite3.connect('iot_data.db')
conn.execute('''CREATE TABLE IF NOT EXISTS sensor_data 
             (id INTEGER PRIMARY KEY, temp REAL, humidity REAL, timestamp TEXT)''')

def read_sensor():
    # Real madhe DHT11 sensor data yeil
    temp = random.uniform(25, 45) 
    humidity = random.uniform(40, 80)
    return temp, humidity

def check_alert(temp):
    if temp > 40:
        print(f"ALERT! High Temperature: {temp}°C - Mail/SMS Trigger")

while True:
    temp, hum = read_sensor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{timestamp}] Temp: {temp:.2f}°C | Humidity: {hum:.2f}%")
    
    conn.execute("INSERT INTO sensor_data (temp, humidity, timestamp) VALUES (?,?,?)",
                 (temp, hum, timestamp))
    conn.commit()
    
    check_alert(temp)
    time.sleep(5) # 5 sec interval
