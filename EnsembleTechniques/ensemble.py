import feature_selection
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import train_data
from sklearn.ensemble import VotingClassifier
from xgboost import XGBClassifier
import re
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


def xg_boost(_data):
    regex = re.compile(r"\[|\]|<", re.IGNORECASE)
    _data.columns = [regex.sub("_", col) if any(x in str(col) for x in set(('[', ']', '<'))) else col for col in
                       _data.columns.values]
    for randomstate in range(11, 12):
        #print('state is -->',randomstate)
        x_train, x_test, y_train, y_test = train_test_split(_data[_data.columns[:-1]], _data['b_or_m'], test_size=0.40,
                                                            random_state=randomstate)
        # original random is 42
        # _rate = [0.1, 0.2, 0.3]
        # _depth = [3, 4, 5, 6, 7, 8, 9, 10]
        # _child = [1]
        # _gamma = [0, 0.1, 0.2]
        # _sample = [0.8]
        # _col_sample = [0.8]
        # state is --> 11
        # 0.2 - - 6 - - 1 - - 0.1 - - 0.8 - - 0.8
        # Accuracy: 97.04 %
        _rate = [0.2]
        _depth = [6]
        _child = [1]
        _gamma = [0.1]
        _sample = [0.8]
        _col_sample = [0.8]
        # 0.2 - - 6 - - 1 - - 0.1 - - 0.8 - - 0.8
        for p in _rate:
            for q in _depth:
                for r in _child:
                    for s in _gamma:
                        for t in _sample:
                            for u in _col_sample:
                                model = XGBClassifier(learning_rate=p,
                                                      max_depth=q,
                                                      min_child_weight=r,
                                                      gamma=s,
                                                      subsample=t,
                                                      colsample_bytree=u,
                                                      objective='binary:logistic',
                                                      booster='gbtree',
                                                      nthread=4,
                                                      scale_pos_weight=1,
                                                      seed=27
                                                      )
                                model.fit(x_train, y_train)
                                y_pred = model.predict(x_test)
                                predictions = [round(value) for value in y_pred]
                                accuracy = accuracy_score(y_test, predictions)
                                #print('learning_rate -- ',p, q, r, s, t, u, sep=' -- ')
                                print('learning_rate -- ', p)
                                print('max_depth -- ', q)
                                print('min_child_weight -- ', r)
                                print('gamma -- ', s)
                                print('subsample -- ', t)
                                print('colsample_bytree -- ', u)
                                print(classification_report(predictions, y_test, labels=None))
                                print("Accuracy: %.3f%%" % (accuracy * 100.0))
                                print('Precision: %.3f' % precision_score(y_test, predictions))
                                print('Recall Score: %.3f' % recall_score(y_test, predictions))
                                print('F1 Score: %.3f' % f1_score(y_test, predictions))


def ensemble_technique(_data):
    x_train, x_test, y_train, y_test = train_test_split(_data[_data.columns[:-1]], _data['b_or_m'], test_size=0.40,
                                                        random_state=42)
    #model1 = tree.DecisionTreeClassifier(random_state=1)
    model2 = SVC()
    #model3 = KNeighborsClassifier()

    #model4 = LogisticRegression(random_state=1)
    #model5 = GaussianNB()

    # model1.fit(x_train, y_train)
    # model2.fit(x_train, y_train)
    # model3.fit(x_train, y_train)

    # pred1 = model1.predict(x_test)
    # pred2 = model2.predict(x_test)
    # pred3 = model3.predict(x_test)
    #model = VotingClassifier(estimators=[('1', model1), ('2', model2),('3', model3),('4', model4),('5', model5)], voting='hard')
    model2.fit(x_train, y_train)
    # predicted = model1.predict(x_test)
    # print(classification_report(predicted, y_test))
    y_pred = model2.predict(x_test)
    predictions = [round(value) for value in y_pred]
    accuracy = accuracy_score(y_test, predictions)
    print(classification_report(predictions, y_test, labels=None))
    print("Accuracy: %.3f%%" % (accuracy * 100.0))
    print('Precision: %.3f' % precision_score(y_test, predictions))
    print('Recall Score: %.3f' % recall_score(y_test, predictions))
    print('F1 Score: %.3f' % f1_score(y_test, predictions))
    #print(model2.score(x_test, y_test))


