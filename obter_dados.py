import pandas as pd
import json
from statistics import mean
import numpy as np
import requests
import random
from datetime import datetime, timedelta
import time
from pickle import dump, load

def dados():

    ts = time.time()
    for i in range(10):
        url = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=2000&toTs={}'.format(int(ts))
        print i
        res = requests.get(url)
        hist = pd.DataFrame(json.loads(res.content)['Data'])
        ts = hist['Data'][0]['time'] -1
        fechamentos = [x['close'] for x in hist['Data']]
        datas = [datetime.fromtimestamp(x['time']) for x in hist['Data']]
        estrutura = (datas, fechamentos)
        dump(estrutura, open('dados_minutos/dados_bitcoin_{}.plk'.format(ts), 'wb'))
        time.sleep(5)

    # hist = hist.set_index('TimeFrom')
    # hist.index = pd.to_datetime(hist.index, unit='s')
    # print 'fim'


import os
def organiza():
    fechs = {}
    
    for arq in os.listdir('dados_minutos/'):
        d = load(open('dados_minutos/'+arq, 'rb'))
        dt, fech = d
        for i, j in zip(dt, fech):
            fechs[i] = j

    els = fechs.keys()
    els.sort()
    fechamentos_saida = [fechs[x] for x in els]
    # estrutura = (els, fechamentos_saida)
    # dump(estrutura, open('dados_minutos/dados_bitcoin_{}.plk'.format(1577000698), 'wb'))
    
    return fechamentos_saida, els
# organiza()
# dados()


def obter_dados():
    df = pd.read_excel('/home/maxtelll/Downloads/BVSP.xlsx', parse_dates=['Date'])
    df.fillna(method='ffill', inplace=True)
    return list(df.Close), list(df.Date)


def obter_dados_btc():
    endpoint = 'https://min-api.cryptocompare.com/data/histoday'
    res = requests.get(endpoint + '?fsym=LTC&tsym=USD&limit=1800')
    hist = pd.DataFrame(json.loads(res.content)['Data'])
    hist = hist.set_index('time')
    hist.index = pd.to_datetime(hist.index, unit='s')
    return list(hist['close']), list(hist.index)
