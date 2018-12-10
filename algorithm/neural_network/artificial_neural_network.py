# -*- coding: UTF-8 -*-
from sklearn.neural_network import MLPClassifier

__author__ = 'gloom'
"""这个类是进行人工神经网络预测的类"""
def main():
    #构建X向量
    X = [[0., 0.], [1., 1.]]
    #构建Y向量
    y = [0, 1]
    #使用人工神经网络，solver求解方式为地图下降alpha默认0.0001,正则化项参数，activation激活函数为逻辑回归，hidden_layer_sizes神经元，两个隐藏层，第一个为五个神经元，第二个为两个神经元，max_iter最大迭代次数，tol可选，默认1e-4，优化的容忍度
    clf = MLPClassifier(solver='sgd', alpha=1e-5, activation='logistic',
                        hidden_layer_sizes=(5, 2), max_iter=2000, tol=1e-4)
    clf.fit(X, y)

    predicted_value = clf.predict([[2., 2.], [-1., -2.]])
    print(predicted_value)
    predicted_proba = clf.predict_proba([[2., 2.], [-1., -2.]])
    print(predicted_proba)

    print([coef.shape for coef in clf.coefs_])
    print([coef for coef in clf.coefs_])
if __name__ == '__main__':
  main()
