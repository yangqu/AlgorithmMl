# -*- coding: UTF-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression

__author__ = 'gloom'
def main():
    #z这个地方和使用线性代数函数的线性回归一样，用来生成X和Y训练集
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    #使用sklearn的线性回归模块
    lin_reg = LinearRegression()
    #输入X和Y矩阵带入函数进行训练
    lin_reg.fit(X, y)
    print(lin_reg.intercept_, lin_reg.coef_)
    #生成测试集，这里边不用人为的去添加X0，是因为该函数的优化，当没有输入X0的时候默认为1
    X_new = np.array([[0], [2]])
    print(lin_reg.predict(X_new))

if __name__ == '__main__':
  main()
