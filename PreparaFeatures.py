from obter_dados import obter_dados
import matplotlib.pyplot as plt
from tratamento_dados import obter_media_alisada, extracao_caracteristicas
from geracao_da_rede  import agrupamento_estados_distintos
from encontrar_comunidades import cria_comundades
# Recebe lista de fechamentos por ordem cronologica
valores, datas = obter_dados()

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
valores, datas = extracao_caracteristicas(valores, datas)
# plt.plot(datas[:250], valores[:250])
# plt.ylabel('some numbers')
# plt.show()
print("caracteristicas discretizadas")
valores, datas, dicionaio_conexoes = agrupamento_estados_distintos(valores, datas)
cria_comundades(dicionaio_conexoes)
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
