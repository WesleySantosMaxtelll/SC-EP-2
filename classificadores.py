from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt

def devolve_classificador(name):
    if (name == 'LogReg'):
        return linear_model.LogisticRegression(solver='lbfgs',n_jobs=1, C=100)
    if (name == 'Baseline'):
        return DummyClassifier(strategy="most_frequent", random_state=None, constant=None)
    elif (name == 'KNN'):
        return KNeighborsClassifier(n_neighbors=7, n_jobs=1, algorithm='brute')
    elif (name == 'NB'):
        return MultinomialNB(alpha=0.1)
    elif (name == 'MLP'):
        return MLPClassifier(solver='lbfgs',hidden_layer_sizes=(25,), alpha=1e-5, max_iter=300,
                             learning_rate_init=0.05, power_t=0.1, learning_rate='constant',  random_state=45)
    else:
        raise NameError('Classifier Unavailable')




def classifica(X, Y, alpha, valores_originais):
    x_treino, y_treino = X[:alpha], Y[:alpha]
    x_teste, y_teste = X[alpha:], Y[alpha:]
    print ('\n\n\nCom um alpha de {}, existe {} instancias de treino e {} instancias de teste'.format(alpha, len(x_treino), len(x_teste)))
    classificadores = ['Baseline', 'MLP', 'LogReg']
    for c in classificadores:
        print ('Classificando com {}'.format(c))
        clf = devolve_classificador(c)
        clf.fit(x_treino, y_treino)
        pred = clf.predict(x_teste)
        # 
        # result = [0 if x1==x2 else 1 for x1, x2 in zip(pred, y_teste)]
        # plt.scatter([x for x in range(len(pred))], valores_originais[alpha:], c=result)
        # plt.title('Indice Bovesp comunidades anotadas como alta e baixa')
        # plt.ylabel('Valor')
        # plt.xlabel('Datas')
        # plt.show()
        # print list(pred)
        # print y_teste
        report = classification_report(y_teste,pred, target_names=['baixa', 'alta'])
        print(report)
        print('\n')


def calcula_ganhos(X, Y, valor_indice, datas, alpha, valor_investimento_inicial):
    x_treino, y_treino = X[:alpha], Y[:alpha]
    x_teste, y_teste = X[alpha:], Y[alpha:]
    valor_dia_a_dia = valor_indice[alpha:]
    print (datas[alpha])
    print (
        '\nCom um alpha de {}, existe {} instancias de treino e {} instancias de teste'.format(alpha, len(x_treino),
                                                                                                   len(x_teste)))
    classificadores = ['LogReg', 'MLP']
    esta_investido = False
    indice_momento_compra = None

    for c in classificadores:
        print ('Classificando com {}'.format(c))
        clf = devolve_classificador(c)
        clf.fit(x_treino, y_treino)
        valor_investimento = valor_investimento_inicial
        for x_t, y_t, v_t in zip(x_teste, y_teste, valor_dia_a_dia):
            pred = clf.predict([x_t])

            # print ('{} {}'.format(pred[0], y_t))
            if (pred[0] == -1 or pred[0]==0) and esta_investido:
                ind = v_t/indice_momento_compra
                # print ind
                # ind*=0.999
                valor_investimento *=ind
                esta_investido = False

            elif pred[0] == 1 and not esta_investido:
                indice_momento_compra = v_t
                esta_investido = True


        print (valor_investimento)
        # report = classification_report(y_teste, pred, target_names=['baixa', 'estavel', 'alta'])
        # print(report)
        print('\n')