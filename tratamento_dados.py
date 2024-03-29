from numpy import mean, std
from scipy.stats import norm
import math


def obter_media_alisada(dados, datas, j=5):
    vetor_alisado = []
    for el in range(j, len(dados)+1):
        v = dados[el-j:el]
        vetor_alisado.append(round(mean(v), 2))
    return vetor_alisado, datas[-len(vetor_alisado):], dados[-len(vetor_alisado):]



def _calcule_media_movel(dados, t, q):
    r = dados[t-q:t]
    return round(mean(r),2)

def _arredonda_em_passos(n):
    return round(n*8)/8

def extracao_caracteristicas(dados, datas, j=5):
    f = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    q_short, q_long = 5, 25

    for i in range(q_short, len(dados)+1):
        mm = _calcule_media_movel(dados, i, q_short)
        f[1].append(round((dados[i-1]-mm)/mm, 2))

    for i in range(q_long, len(dados)+1):
        mm = _calcule_media_movel(dados, i, q_long)
        f[2].append(round((dados[i-1]-mm)/mm,2))

    for i in range(q_short+1, len(dados)+1):
        mmt = _calcule_media_movel(dados, i, q_short)
        mmtm1 = _calcule_media_movel(dados, i-1, q_short)
        f[3].append(round((mmt-mmtm1)/mmtm1,2))

    for i in range(q_long+1, len(dados)+1):
        mmt = _calcule_media_movel(dados, i, q_long)
        mmtm1 = _calcule_media_movel(dados, i-1, q_long)
        f[4].append(round((mmt-mmtm1)/mmtm1,2))


    for i in range(q_short-1, len(dados)):
        minimo = min(dados[i-q_short+1:i+1])
        maximo = max(dados[i-q_short+1:i+1])
        if maximo == minimo:
            minimo = maximo-1
        f[5].append(round((dados[i]-minimo)/(maximo-minimo),2))

    for i in range(q_long-1, len(dados)):
        minimo = min(dados[i - q_long + 1:i + 1])
        maximo = max(dados[i - q_long + 1:i + 1])
        if maximo == minimo:
            minimo = maximo-1
        f[6].append(round((dados[i] - minimo) / (maximo - minimo),2))


    fz = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}

    for i in range(1, 7):
        media, desvio_padrao = mean(f[i]), std(f[i])
        for j in range(len(f[i])):
            fp = (f[i][j]-media)/desvio_padrao
            if math.isnan(fp):
                fp = 0
            fz[i].append(_arredonda_em_passos(norm.cdf(fp)))

    # print(fp)
    # print(fz)
    comprimento_minimo = min([len(fz[x]) for x in fz])
    V = []
    for i in range(1, comprimento_minimo+1):
        V.insert(0, [fz[x][-i] for x in range(1,7)])
    return V, datas[-len(V):], dados[-len(V):]