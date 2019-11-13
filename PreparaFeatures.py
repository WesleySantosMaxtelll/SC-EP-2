from obter_dados import obter_dados
import matplotlib.pyplot as plt
from tratamento_dados import obter_media_alisada, extracao_caracteristicas
from geracao_da_rede  import agrupamento_estados_distintos
from encontrar_comunidades import cria_comundades
# Recebe lista de fechamentos por ordem cronologica
valores, datas = obter_dados()
import hashlib
import base64

# plt.plot(datas, valores)
# plt.ylabel('some numbers')
# plt.show()
# valores, datas = [15, 11, 3, 8, 7, 20, 1, 5, 8, 4, 3, 12], list(range(0,12))

# print(valores)
# plt.plot(datas, valores)
# plt.ylabel('some numbers')
# plt.show()

valores, datas = obter_media_alisada(valores, datas, 3)
# print(valores)
# plt.plot(datas, valores)
# plt.ylabel('some numbers')
# plt.show()
valores, datas, valores_originais = extracao_caracteristicas(valores, datas)
# plt.plot(datas[:250], valores[:250])
# plt.ylabel('some numbers')
# plt.show()
print("caracteristicas discretizadas")
valores, datas, dicionaio_conexoes = agrupamento_estados_distintos(valores, datas)
comunidades = cria_comundades(dicionaio_conexoes)

import numpy as np

# Generate data...
# t = np.linspace(0, 2 * np.pi, 20)
# print (t)
# x = np.sin(t)
# y = np.cos(t)

def make_hash_sha256(o):
    hasher = hashlib.sha256()
    hasher.update(repr(make_hashable(o)).encode())
    return base64.b64encode(hasher.digest()).decode()

def make_hashable(o):
    if isinstance(o, (tuple, list)):
        return tuple((make_hashable(e) for e in o))

    if isinstance(o, dict):
        return tuple(sorted((k,make_hashable(v)) for k,v in o.items()))

    if isinstance(o, (set, frozenset)):
        return tuple(sorted(make_hashable(e) for e in o))

    return o

a = []
for i in valores:
    a.append(comunidades[make_hash_sha256(i)])
plt.scatter(datas,valores_originais, c=a)
plt.show()


#
# for i in range(len(valores)):
#     print(str(nos_de_cada_data[i]) + ' ' + str(valores[i]))

# plt.plot(datas, valores)
# plt.ylabel('some numbers')
# plt.show()

# def plot_df(df, x, y, title="", xlabel='Date', ylabel='Close', dpi=100):
#     plt.figure(figsize=(12,5), dpi=dpi)
#     plt.plot(x, y, color='tab:red')
#     plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
#     plt.show()
#
#
# plot_df(df, x=df.Date, y=df.Close, title='Indice Bovespa desde 1993.')
#
