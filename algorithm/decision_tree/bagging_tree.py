from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

__author__ = 'gloom'
"""也称为 bootstrap aggregating，简单的来说，就是从原始训练数据集中，有放回的采样出若干个小集合，然后在每个小集合上train model，对所有的model output取平均（regression）或者投票（classification）"""
def main():
    #使用逻辑回归
    log_clf = LogisticRegression()
    #使用随机森林
    rnd_clf = RandomForestClassifier()
    #使用支持向量机
    svm_clf = SVC()

    voting_clf = VotingClassifier(
        estimators=[('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf)],
        voting='hard'
    )

    iris = load_iris()
    X = iris.data[:, :2]  # 花萼长度和宽度
    y = iris.target
    # X, y = make_moons()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    voting_clf.fit(X, y)


    for clf in (log_clf, rnd_clf, svm_clf, voting_clf):
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print(clf.__class__.__name__, accuracy_score(y_test, y_pred))


    bag_clf = BaggingClassifier(
        DecisionTreeClassifier(), n_estimators=500,
        max_samples=1.0, bootstrap=True, n_jobs=1
    )
    bag_clf.fit(X_train, y_train)
    y_pred = bag_clf.predict(X_test)
    print(y_pred)
    y_pred_proba = bag_clf.predict_proba(X_test)
    print(y_pred_proba)
    print(accuracy_score(y_test, y_pred))


    # oob
    bag_clf = BaggingClassifier(
        DecisionTreeClassifier(), n_estimators=500,
        bootstrap=True, n_jobs=1, oob_score=True
    )
    bag_clf.fit(X_train, y_train)
    print(bag_clf.oob_score_)
    y_pred = bag_clf.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    print(bag_clf.oob_decision_function_)

if __name__ == '__main__':
  main()
