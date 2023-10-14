# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

# семинар 1

import pandas as pd
from pandas import read_csv

import seaborn as sns
from pandas import read_csv
import matplotlib.pyplot as plt


# df = pd.read_csv('california_housing_test.csv', sep=',')
df = pd.read_csv('penguins.csv', sep=',')
# #print(data.columns)
# print(data.info())
# # print(data.dtypes)
print(df.shape)
# print(data.head())
# DataFrame.head(n=5)

# # 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000


# print(data.isnull().sum())
# print(data["population"].max)
# print(data.columns)

import seaborn as sns
from pandas import read_csv
import matplotlib.pyplot as plt

# задача 1

# df = read_csv('california_housing_test.csv')
# sns.scatterplot(data=df, x='households', y='population')
# plt.show()
# print(data.columns)

# задача  2
# sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
# plt.show()


# #  задача 3

# sns.histplot(data=df, x="housing_median_age")
# plt.show()


# задача 4
# sns.displot(data=df, x="median_house_value", hue="housing_median_age")
# plt.show()


# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

# f_1()

# def f_2():
#  sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue='sex', size=5, style='island')
# plt.show()


# # f_2()

# def f_3():
# x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
# y_vars = ['sex']
# g = sns.PairGrid(penguins, x_vars=x_vars, y_vars=y_vars, hue='species')
# g.map(sns.scatterplot)
# plt.show()
# #
# # f_3()


# def f_4():
# sns.displot(penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
# plt.show()


# # f_4()

# def f_5():
#    penguins['bill_depth_mm'].hist(bins=10)
#    plt.show()

# import seaborn as sns
# from random import randint

# penguins = sns.load_dataset('penguins')

# def f(row):
#   res = randint(1,60)
#   val = None
#   if res < 35:
#    val = 'low'
#   elif 35 < res < 42:
#    val = 'middle'
#   elif res > 42:
#    val = 'high'
#   return val

# penguins['len'] = penguins.apply(f, axis=1)

# print(penguins)


# import seaborn as sns
# import matplotlib.pyplot as plt
# import csv
# penguins = sns.load_dataset('penguins')


# with open('penguins.csv', 'w') as f_n:
   
#    F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(DATA[0].keys()),
#    quoting=csv.QUOTE_NONNUMERIC)
#    F_N_WRITER.writeheader()
#    for d in DATA:
#       F_N_WRITER.writerow(d)


# sns.histplot(penguins, x='flipper_length_mm', hue='len')
# plt.show()

import pandas as pd 
import numpy as np 
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)
print('')


data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)