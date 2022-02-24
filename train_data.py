#SVM
#NAIVE BAYES


from sklearn import svm
from sklearn.kernel_approximation import Nystroem
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import tree


def linear_SVC(X_train, X_test, y_train, y_test):
    clf = svm.LinearSVC()
    print(X_train.shape)
    print(y_test)
    feature_map_nystroem = Nystroem(n_components=8)
    data_transformed = feature_map_nystroem.fit_transform(X_train)
    clf.fit(data_transformed, y_train)
    predict = clf.predict(X_test)
    accuracy = accuracy_score(predict, y_test)
    print(accuracy)
    print(classification_report(predict, y_test, labels=None))


def SVC_model(X_train, X_test, y_train, y_test):
    svc_model = SVC()
    svc_model.fit(X_train, y_train)
    _predicted = svc_model.predict(X_test)
    print(classification_report(_predicted, y_test))


def GaussianNB_model(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    _predicted = gnb.predict(X_test)
    print(classification_report(_predicted, y_test))


def decison_tree(X_train, X_test, y_train, y_test):
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    print(classification_report(predicted,y_test))

