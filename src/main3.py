import os
import time
import csv
from datetime import datetime
from collections import deque
import matplotlib.pyplot as plt

from sensors.voltage_reader import read_voltage
from sensors.current_reader import read_current
from sensors.temperature_reader import read_temperature

# make logs directory
os.makedirs("logs", exist_ok=True)
log_file_path = "logs/data_log3.csv"

# setup CSV logging
with open(log_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Voltage (V)", "Current (A)", "Temperature (C)"])

# keep only last 100 readings for live plot
time_data = deque(maxlen=100)
voltage_data = deque(maxlen=100)
current_data = deque(maxlen=100)
temperature_data = deque(maxlen=100)

# setup matplotlib interactive plotting
plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

try:
    with open(log_file_path, "a", newline="") as file:
        writer = csv.writer(file)

        while True:
            voltage = read_voltage()
            current = read_current()
            temperature = read_temperature()
            timestamp = datetime.now().strftime("%H:%M:%S")

            # save to CSV
            writer.writerow([timestamp, f"{voltage:.2f}", f"{current:.2f}", f"{temperature:.2f}"])
            file.flush()

            # save to deque for plotting
            time_data.append(timestamp)
            voltage_data.append(voltage)
            current_data.append(current)
            temperature_data.append(temperature)

            # clear and re-plot each axis
            ax1.cla(); ax2.cla(); ax3.cla()

            # Voltage
            ax1.plot(time_data, voltage_data, color="blue", label="Voltage (V)")
            ax1.set_ylabel("Voltage (V)")
            ax1.legend(loc="upper right")
            ax1.grid(True)

            # Current
            ax2.plot(time_data, current_data, color="orange", label="Current (A)")
            ax2.set_ylabel("Current (A)")
            ax2.legend(loc="upper right")
            ax2.grid(True)

            # Temperature
            ax3.plot(time_data, temperature_data, color="red", label="Temp (°C)")
            ax3.set_ylabel("Temp (°C)")
            ax3.set_xlabel("Time (HH:MM:SS)")
            ax3.legend(loc="upper right")
            ax3.grid(True)

            # rotate x-axis ticks for readability
            plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45, ha="right")

            plt.tight_layout()
            plt.pause(0.5)  # update every 0.5 sec

except KeyboardInterrupt:
    print(f"\nLogging stopped by user. Data saved to {log_file_path}")
