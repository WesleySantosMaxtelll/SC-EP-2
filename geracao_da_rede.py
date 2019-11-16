from statistics import mean,pstdev
from scipy.stats import norm
import math
import hashlib
import base64

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



def agrupamento_estados_distintos(valores, datas):
    mapa_estados = {}
    for i in range(len(valores)-1):
        valor = valores[i]
        # acha o hash para i e i +1
        chave_i = make_hash_sha256(valor)
        chave_ip1 = make_hash_sha256(valores[i+1])

        # se a chave i nao esta no mapa, insere o dicionario de i+1 com o valor de 1
        if chave_i not in mapa_estados.keys():
            mapa_estados[chave_i] = {chave_ip1:1}
        else:
            # se ele ja existe, procura se i+1 esta nas adjacencias de i, se estiver apenas incrementa
            # caso contraro, insere i+1 na adjacencia de i com o valor de 1
            if chave_ip1 in mapa_estados[chave_i]:
                mapa_estados[chave_i][chave_ip1]+=1
            else:
                mapa_estados[chave_i][chave_ip1] = 1
    return valores, datas, mapa_estados
