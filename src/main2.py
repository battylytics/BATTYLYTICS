import os
import time
import csv
from datetime import datetime
from sensors.voltage_reader import read_voltage
from sensors.current_reader import read_current
from sensors.temperature_reader import read_temperature

os.makedirs("logs",exist_ok=True)

log_file_path = "logs/data_log2.csv"

with open(log_file_path,"w",newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["Time","Voltage (V)","Current (A)","Temperature (C)"])

    try:
        while True:
            voltage=read_voltage()
            current=read_current()
            temperature=read_temperature()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"VOLTAGE: {voltage:.2f} V | CURRENT: {current:.2f} A | TEMP: {temperature:.2f} C")
    
            writer.writerow([timestamp,f"{voltage:.2f}",f"{current:.2f}",f"{temperature:.2f}"])
            file.flush()

            time.sleep(1)

    except KeyboardInterrupt:
       print(f"\nLogging stopped by user. Data saved to {log_file_path}")

