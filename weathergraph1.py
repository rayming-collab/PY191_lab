import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("station_weather.csv")
fig, ax = plt.subplots(figsize=(10, 5))

hourly_avg = df.groupby(['station_id', 'hour'])['temperature_f'].mean()
station_data = hourly_avg.unstack(level='station_id')

for station in station_data.columns:
    ax.plot(station_data.index, station_data[station], label=station)

ax.legend(title="Stations")

ax.set_title("Average Temperature by Station and Hour", fontsize=14)
ax.set_xlabel("Hour of Day", fontsize=12)
ax.set_ylabel("Temperature (°F)", fontsize=12)
plt.show()