#SVM
#NAIVE BAYES


from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import tree


def linear_SVC(X_train, X_test, y_train, y_test):
    print("Linear SVC: ")
    clf = svm.LinearSVC(dual=False)
    clf.fit(X_train, y_train)
    predict = clf.predict(X_test)
    accuracy = accuracy_score(predict, y_test)
    print(accuracy)
    print(classification_report(predict, y_test, labels=None))


def SVC_model(X_train, X_test, y_train, y_test):
    print("SVC: ")
    svc_model = SVC()
    svc_model.fit(X_train, y_train)
    _predicted = svc_model.predict(X_test)
    print(classification_report(_predicted, y_test))


def GaussianNB_model(X_train, X_test, y_train, y_test):
    print("GaussianNB: ")
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    _predicted = gnb.predict(X_test)
    print(classification_report(_predicted, y_test))


def decison_tree(X_train, X_test, y_train, y_test):
    print("Decison Tree: ")
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    print(classification_report(predicted,y_test))

