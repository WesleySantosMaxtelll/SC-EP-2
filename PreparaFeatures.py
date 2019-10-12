import numpy as np
from statistics import mean
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd

print("oi galera")




myfile = open('test.csv', 'r')
inputdict= {}



# df = pd.read_csv('test.csv', parse_dates=['Date'])
df = pd.read_csv('BVSP_nomissing.csv', parse_dates=['Date'])
print(df.head())
print(df.Close)

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Close', dpi=100):
    plt.figure(figsize=(12,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


plot_df(df, x=df.Date, y=df.Close, title='Indice Bovespa desde 1993.')

