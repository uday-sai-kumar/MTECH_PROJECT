from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel


def select_k_best(_data):
    a = ['f'+str(i) for i in range(1, 9)]

    print(a)

    print(_data[0:5][a])
    X_new = SelectKBest(chi2, k=5).fit(_data[a], _data['m_or_b'])
    #print("woowww --- " ,X_new)

    dfscores = pd.DataFrame(X_new.scores_)
    dfcolumns = pd.DataFrame(_data.columns)

    featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    featureScores.columns = ['Feature', 'Score']
    print(featureScores)
    print('____________________')
    print(featureScores.nlargest(8, 'Score'))


def extree_tree_classifier(_data):
    a = ['f' + str(i) for i in range(1, 9)]
    model = ExtraTreesClassifier()
    model.fit(_data[a], _data['m_or_b'])
    print(model.feature_importances_)
    print(_data[a].columns)
    feat_importances = pd.Series(model.feature_importances_, index=_data[a].columns)
    feat_importances.nlargest(8).plot(kind='barh')
    plt.show()


def recursive_feature_elimination(_data):
    a = ['f' + str(i) for i in range(1, 9)]
    model = LogisticRegression(solver='lbfgs')
    #estimator = SVR(kernel="linear")
    selector = RFE(model, n_features_to_select=5)
    selector = selector.fit(_data[a], _data['m_or_b'])
    print(selector.support_)
    print(selector.ranking_)





def select_from_model(_data):
    a = ['f' + str(i) for i in range(1, 9)]
    selector = SelectFromModel(estimator=LogisticRegression()).fit(_data[a], _data['m_or_b'])
    print(selector.estimator_.coef_)
    print(selector.threshold_)
    print(selector.get_support())






