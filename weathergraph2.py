import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("station_weather.csv")
fig, ax = plt.subplots(figsize=(10, 5))

hourly_avg = df.groupby(['station_id', 'date'])['temperature_f'].mean()
station_data = hourly_avg.unstack(level='station_id')

station_data.plot.bar(ax=ax, width=0.8)

ax.legend(title="Stations")

ax.set_title("Average Temperature by Station by Day", fontsize=14)
ax.set_xlabel("Average of Day", fontsize=12)
ax.set_ylabel("Temperature (°F)", fontsize=12)
plt.show()