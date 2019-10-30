from statistics import mean,pstdev
from scipy.stats import norm
import math




def agrupamento_estados_distintos(valores, datas):
    conta_estados = 0
    mapa_estados = {}
    nos_de_cada_data = []
    for i, valor  in enumerate(valores):
        chave = ""
        for carac in valor:
            # transformando 0, 0.25, 0.5... em 0, 1, 2...
            chave += str(int(4 * carac))
        # chave = int(chave)
        if chave not in mapa_estados.keys():
            mapa_estados[chave] = conta_estados
            nos_de_cada_data.append(conta_estados)
            conta_estados += 1
        else:
            nos_de_cada_data.append(mapa_estados[chave])

    # print(nos_de_cada_data)
    return nos_de_cada_data, valores, datas
