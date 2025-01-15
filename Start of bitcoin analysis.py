import pandas as pd
import numpy as np
from datetime import datetime 
import matplotlib.pyplot as plt

## link for dataset: https://www.kaggle.com/datasets/jkraak/bitcoin-price-dataset?resource=download

#### this dataset is by the minute

## 3 Goals for this dataset
## so I want to look into grouping this by day, for a long term analysis and regression later on

## but also want to look into day by day, is there a certain time of day when it's different?

## I also want to join other datasets on, to get the full timeline. as this only starts in 2017



##TO BE NOTED
#these markets do not close at any point. So open/close values will need to be calculated by end and start of the grouped timeframe
#i/e first and last, not 9am/5pm

df = pd.read_csv(r"C:\Users\Oliver\OneDrive\Documents\bitcoin_2017_to_2023.csv")

## First grouping by day, with the end result being a graph over time 

## checking data quality
########################

# =============================================================================
# print(df.head())
# print(df.isnull().mean())
#  no null values! Amazing
# =============================================================================

########################



## turn into a datetime to allow easy grouping later on


df["timestamp"] = pd.to_datetime(df["timestamp"])

#df = datetime.fromtimestamp(df["timestamp"], tz = None) this did not work as csv file uses series
## gets opening and closing time for start and end of each day. And max/min high and low. 

df = df.groupby(df["timestamp"].dt.date).agg({'open': 'last', 'close': 'first','high': 'max','low': 'min','number_of_trades': 'sum'}).rename_axis('date').reset_index()

## Simple plot, can see the large spike in 2021... if only had brought any....

x_plot = df['date']
y_plot = df['close']
plt.plot(x_plot,y_plot,label='Close Price', color='blue')
plt.legend()
plt.xticks(rotation = 45)
plt.title("Closing Price Over Time For Bitcoin")
plt.show()


## stats about the data

max_price = df['high'].max()
min_price =  df['low'].min()
max_high_date = df.loc[df['high'].idxmax(), 'date']
min_low_date = df.loc[df['low'].idxmin(), 'date']
df['daily change'] = df['open'] - df['close']
biggest_drop = df['daily change'].max()
biggest_jump = (df['daily change']).min()
biggest_drop_date = df.loc[df['daily change'].idxmax(), 'date']
biggest_jump_date = df.loc[df['daily change'].idxmin(), 'date']


max_price = round(max_price, 0)
min_price = round(min_price, 0)
biggest_drop = round(biggest_drop, 2)
biggest_jump = round(biggest_jump, 2)


print("Max price: $" + str(max_price) + " on " + str(max_high_date))
print("Min price: $" + str(min_price) + " on " + str(min_low_date))


print("The biggest drop was: $" + str(biggest_drop) + " on " + str(biggest_drop_date))
print("The biggest jump was: $" + str(abs(biggest_jump)) + " on " + str(biggest_jump_date))



##### Tried to dual plot, but didn't show anything as too close together day by day, maybe month by month?
####### 
# =============================================================================
# x_plot = df['date']
# y_plot = df['close']
# y_plot2 = df['open']
# fig, ax = plt.subplots()
# 
# ax.plot(x_plot,y_plot,label='Close Price', color='blue')
# ax.plot(x_plot,y_plot2,label='Open Price', color='yellow')
# plt.legend()
# plt.xticks(rotation = 45)
# plt.title("Closing And Opening Price Over Time For Bitcoin")
# plt.show()
# =============================================================================
######




