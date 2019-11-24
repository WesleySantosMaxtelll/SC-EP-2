from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report

def devolve_classificador(name):
    if (name == 'LogReg'):
        return linear_model.LogisticRegression(n_jobs=1, C=100)
    if (name == 'Baseline'):
        return DummyClassifier(strategy="most_frequent", random_state=None, constant=None)
    elif (name == 'KNN'):
        return KNeighborsClassifier(n_neighbors=3, n_jobs=1, algorithm='brute', metric='cosine')
    elif (name == 'NB'):
        return MultinomialNB(alpha=0.1)
    elif (name == 'MLP'):
        return MLPClassifier(solver='lbfgs',hidden_layer_sizes=(25,), alpha=1e-5, max_iter=300, learning_rate_init=0.05, power_t=0.1, learning_rate='constant',  random_state=1)
    else:
        raise NameError('Classifier Unavailable')




def classifica(X, Y, alpha):
    x_treino, y_treino = X[:int(alpha*len(X))], Y[:int(alpha*len(Y))]
    x_teste, y_teste = X[int(alpha * len(X)):], Y[int(alpha * len(Y)):]
    print ('\n\n\nCom um alpha de {}, existe {} instancias de treino e {} instancias de teste'.format(alpha, len(x_treino), len(x_teste)))
    classificadores = ['Baseline', 'LogReg', 'KNN', 'NB', 'MLP']
    for c in classificadores:
        print ('Classificando com {}'.format(c))
        clf = devolve_classificador(c)
        clf.fit(x_treino, y_treino)
        pred = clf.predict(x_teste)
        report = classification_report(y_teste,pred, target_names=['baixa', 'alta'])
        print(report)
        print('\n')
