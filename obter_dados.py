import pandas as pd

def obter_dados():
    df = pd.read_csv('BVSP.csv', parse_dates=['Date'])
    return list(df.Close), list(df.Date)