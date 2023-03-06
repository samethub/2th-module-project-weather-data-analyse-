import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("all_graphs\\all_data\\ordered_csv")
dates_clm = 'Местное время в Нижнем Новгороде / им. В. П. Чкалова (аэропорт)'


#                                                 creating plot
plt.style.use("bmh")

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df[dates_clm], df["P0"], linewidth=3, color="#5D8BF4")

ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))


ax.set_ylabel("Pressure (mmHg)", fontfamily='serif', fontweight='bold', fontsize=16, color='#051367')
ax.set_title("Нижний Новгород\nPressure Change in May 2020", fontfamily='serif', fontweight='bold', fontsize=20, color='#051367')

plt.xticks(rotation=-20)

plt.show()
