from obter_dados import obter_dados
import matplotlib.pyplot as plt
from tratamento_dados import obter_media_alisada, extracao_caracteristicas
from geracao_da_rede  import agrupamento_estados_distintos
from encontrar_comunidades import cria_comundades
from classificadores import classifica
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

comunidade_valor = []
for i in valores:
    comunidade_valor.append(comunidades[make_hash_sha256(i)])

plt.scatter(datas, valores_originais, c=comunidade_valor)
plt.show()

media_comunidade = {}

for comunidade in set(comunidades.values()):
    media_comunidade[comunidade] = 0

for i in range(0, len(valores_originais)-1):
    delta_cp_i = (valores_originais[i+1] - valores_originais[i] ) / valores_originais[i]
    # print(i)
    # print( str(comunidade_valor[i]) + " " + str(media_comunidade[comunidade]))
    media_comunidade[comunidade_valor[i]] += delta_cp_i

rotulo_comunidade = []
for comunidade in set(comunidades.values()):
    printable_string = str(comunidade) + " -> " + str(media_comunidade[comunidade])
    if(media_comunidade[comunidade] > 0):
        printable_string += " UP"
        rotulo_comunidade.append(1)
    else:
        printable_string += " DOWN"
        rotulo_comunidade.append(0)
    print(printable_string)

up_or_down = []
for comunidade in comunidade_valor:
    up_or_down.append(rotulo_comunidade[comunidade])

plt.scatter(datas, valores_originais, c=up_or_down)
plt.show()

# rodar os classificadores com 'valores' (X) e 'up_or_down' (Y)
for alpha in range(2, 10):
    classifica(valores, up_or_down, alpha*0.1)


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
