#ML003 Оценка модели
"""
This module make

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams


def calculate_model(x, energy_0_train_averages):
    meter_reading_log = np.log(x.meter_reading + 1)
    meter_reading_mean = np.log(energy_0_train_averages["Среднее"][x.hour] + 1)
    meter_reading_median = np.log(energy_0_train_averages["Медиана"][x.hour] + 1)
    x["meter_reading_mean_q"] = (meter_reading_log - meter_reading_mean) ** 2
    x["meter_reading_median_q"] = (meter_reading_log - meter_reading_median) ** 2
    x["meter_reading_zero_q"] = (meter_reading_log) ** 2
    return x

def proga():
    rcParams['figure.figsize'] = 16, 8
    print("Step 1 ==== Загрузка данных ======")
    full_path = os.path.dirname(os.path.abspath(__file__))
    energy_0 = pd.read_csv(full_path + "/jupiter_bilder/train.csv")
    energy_0 = energy_0[energy_0["meter_reading"] > 0]
    energy_0["timestamp"] = pd.to_datetime(energy_0["timestamp"])
    energy_0["hour"] = energy_0["timestamp"].dt.hour
    print(energy_0.head())

    print("Step 2 ====== Разделение данных на обучение и проверку ====")

    energy_0_train, energy_0_test = train_test_split(energy_0, test_size=0.2)
    print(energy_0_train.head())

    print("Step 3 ====== Создадим модели ====")
    energy_0_train_hours = energy_0_train.groupby("hour")
    energy_0_train_averages = pd.DataFrame(
        {"Среднее": energy_0_train_hours.mean()["meter_reading"],
         "Медиана": energy_0_train_hours.median()["meter_reading"]})
    print(energy_0_train_averages)

    print("Step 4 ====== Функция проверки модели ====")

    energy_0_test = energy_0_test.apply(calculate_model(energy_0, energy_0_train_averages), axis=1, result_type="expand")
    print(energy_0_test.head())

    energy_0_test_median_rmsle = np.sqrt(energy_0_test["meter_reading_median_q"].sum() / len(energy_0_test))
    energy_0_test_mean_rmsle = np.sqrt(energy_0_test["meter_reading_mean_q"].sum() / len(energy_0_test))
    energy_0_test_zero_rmsle = np.sqrt(energy_0_test["meter_reading_zero_q"].sum() / len(energy_0_test))
    print("Качество медианы:", energy_0_test_median_rmsle)
    print("Качество среднего:", energy_0_test_mean_rmsle)
    print("Качество нуля:", energy_0_test_zero_rmsle)


if __name__ == '__main__':
    proga()