from obter_dados import obter_dados
import matplotlib.pyplot as plt
from tratamento_dados import obter_media_alisada, extracao_caracteristicas
from geracao_da_rede  import agrupamento_estados_distintos
from encontrar_comunidades import cria_comundades
from classificadores import classifica, calcula_ganhos
import hashlib
import base64
import numpy as np



# Recebe lista de fechamentos por ordem cronologica
valores, datas = obter_dados()


plt.plot(datas, valores)
plt.title('Dados Brutos')
plt.show()

valores, datas = obter_media_alisada(valores, datas, 5)

plt.plot(datas, valores)
plt.title('Medias alisadas')
plt.show()

valores, datas, valores_originais = extracao_caracteristicas(valores, datas)

print("caracteristicas discretizadas")
valores, datas, dicionaio_conexoes = agrupamento_estados_distintos(valores, datas)
comunidades = cria_comundades(dicionaio_conexoes)


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
plt.title('Comunidades detectadas')
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
        rotulo_comunidade.append(-1)
    print(printable_string)

up_or_down = []
for comunidade in comunidade_valor:
    up_or_down.append(rotulo_comunidade[comunidade])

plt.scatter(datas, valores_originais, c=up_or_down)
plt.title('Comunidades anotadas')
plt.show()

# rodar os classificadores com 'valores' (X) e 'up_or_down' (Y)
for alpha in range(1000, len(valores), 500):
    classifica(valores, up_or_down, alpha)
    # calcula_ganhos(valores, up_or_down,valores_originais, datas, 0.1*alpha, 10000)
