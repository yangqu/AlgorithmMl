# -*- coding: UTF-8 -*-

import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import SGDRegressor

__author__ = 'gloom'
"""这个是使用lasso进行回归，L1正则化"""
def main():

    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    lasso_reg = Lasso(alpha=0.15)
    lasso_reg.fit(X, y)
    print(lasso_reg.predict([[1.5]]))
    print(lasso_reg.coef_)

    sgd_reg = SGDRegressor(penalty='l1', max_iter=1000)
    sgd_reg.fit(X, y.ravel())
    print(sgd_reg.predict([[1.5]]))
    print(sgd_reg.coef_)
if __name__ == '__main__':
  main()






