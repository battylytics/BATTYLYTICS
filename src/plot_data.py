log_file_path = "logs/data_log2.csv"
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV log file
data = pd.read_csv("logs/data_log2.csv", on_bad_lines="skip")

# Convert 'Time' column to datetime format
data['Time'] = pd.to_datetime(data['Time'])

# Plot the data
plt.figure(figsize=(12, 6))

# Voltage plot
plt.plot(data['Time'], data['Voltage (V)'], label='Voltage (V)', linewidth=2)

# Current plot
plt.plot(data['Time'], data['Current (A)'], label='Current (A)', linewidth=2)

# Temperature plot
plt.plot(data['Time'], data['Temperature (C)'], label='Temperature (C)', linewidth=2)

plt.xlabel("Time")
plt.ylabel("Sensor Values")
plt.title("Battery Parameters Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
