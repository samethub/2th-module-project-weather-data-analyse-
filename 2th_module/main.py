import pandas as pd
import matplotlib.pyplot as plt

# weather data 01.05.2020 and 01.06.2020 Нижнем Новгороде
full_df = pd.read_csv("all_graphs\\all_data\\UWGG.01.05.2020.01.06.2020.1.0.0.ru.utf8.00000000.csv",
                        skiprows = 6, sep=";", on_bad_lines="skip")

# creating df that we need (date/T/P0/U/FF)
df = full_df[['Местное время в Нижнем Новгороде / им. В. П. Чкалова (аэропорт)', 'T', 'P0', 'U', 'Ff']]

# simplify and update data
def simplify_df(list_name, clm_name):
    """returns mean of values and appends to list"""
    # indexes
    start = 0
    end = 48

    while start < len(df) - 1:
        val = df[clm_name][start:end].mean()
        list_name.append(val)
        start = end
        end += 48

dates_series = df['Местное время в Нижнем Новгороде / им. В. П. Чкалова (аэропорт)'].apply(lambda x: x.split()[0])

dates, temperatures, pressures, moistures, wind_speeds = [], [], [], [], []

simplify_df(temperatures, "T")
simplify_df(pressures, "P0")
simplify_df(moistures, "U")
simplify_df(wind_speeds, "Ff")
dates = dates_series.unique()

data_frame_dict = {
    'Местное время в Нижнем Новгороде / им. В. П. Чкалова (аэропорт)': reversed(dates),
    "T": reversed(temperatures),
    "P0": reversed(pressures),
    "U": reversed(moistures),
    "Ff": reversed(wind_speeds),
}
main_df = pd.DataFrame(data_frame_dict)

test = pd.to_datetime(main_df.iloc[:, 0], dayfirst=True, format="%d.%m.%Y")
main_df[main_df.columns[0]] = test












