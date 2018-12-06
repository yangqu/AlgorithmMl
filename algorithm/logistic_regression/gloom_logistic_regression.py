# -*- coding: UTF-8 -*-

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from time import time

__author__ = 'gloom'
"""这个类是进行逻辑回归测试的类别"""
def main():
    #加载鸢尾花数据，这个只要有网络就可以
    iris = datasets.load_iris()
    #打印所有的列名
    #print(list(iris.keys()))
    #打印描述
    #print(iris['DESCR'])
    #打印数据集有哪些特征['sepal length (cm)'花萼长度, 'sepal width (cm)'花萼宽度, 'petal length (cm)'花瓣长度, 'petal width (cm)花瓣宽度']
    #print(iris['feature_names'])
    #切片操作，生成X，从头到尾，取第四列
    X = iris['data'][:, 3:]
    #打印X
    #print(X)
    #打印原本的种类
    #print(iris['target'])
    #设置y，就是原来数据集的target列组成的列向量
    y = iris['target']
    # y = (iris['target'] == 2).astype(np.int)
    #print(y)
    #使用逻辑回归，这里边multi_class='ovr'是one-vs-rest的意思，对应的multinomial是softmax的多分类，而ovr也支持多分类，只不过方法不一样而已，ovr是此类别/不是此类别的二分箱，如果要多分类，则每个类别都做一遍即可
    #Note that 'sag' and 'saga' 要快速收敛需要保证特征在同一个数量级，比较适合现在的场景
    log_reg = LogisticRegression(multi_class='ovr', solver='sag')
    #使用网格搜索，这个好处在于可以自动调整参数，log_reg是算法选择，选择逻辑回归，cv代表验证方式是cross validation交叉验证
    #grid_search = GridSearchCV(log_reg, cv=3)
    #训练模型
    log_reg.fit(X, y)
    #建立一维数组，0到3的1000个等差数据列，reshape（-1）是变成一行，reshape（-1,1）是变成一列
    X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
    #print(X_new)
    #预测新的y分类的概率
    y_proba = log_reg.predict_proba(X_new)
    #预测新的y的类别
    y_hat = log_reg.predict(X_new)
    print(y_proba)
    #print(y_hat)
    #由于此数据集有三个类别所以生成三列的列向量，分别为三种类别的概率
    plt.plot(X_new, y_proba[:, 2], 'g-', label='Iris-Virginica')
    plt.plot(X_new, y_proba[:, 1], 'r-', label='Iris-Versicolour')
    plt.plot(X_new, y_proba[:, 0], 'b--', label='Iris-Setosa')
    plt.show()

    #print(log_reg.predict([[1.7], [1.5]]))

if __name__ == '__main__':
  main()
