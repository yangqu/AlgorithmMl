# -*- coding: UTF-8 -*-

import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor

__author__ = 'gloom'
"""这个类是栅格搜索，他们只是来源于不同的两个类，这个方法主要是为了能够在lasso和岭回归中选择到最好方法和参数"""
def main():
    #老两样，继续生成X和Y,不一样的地方是不用生成X0
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    #1 / (2 * n_samples) * ||y - Xw||^2_2+ alpha * l1_ratio * ||w||_1+ 0.5 * alpha * (1 - l1_ratio) * ||w||^2_2
    #由这个目标函数可以看出来，alpha用来确定正则化程度，1l_ratio用来确定1L和2L的权重
    elastic_net = ElasticNet(alpha=0.0001, l1_ratio=0.15)
    elastic_net.fit(X, y)
    print(elastic_net.predict([[1.5]]))

    sgd_reg = SGDRegressor(penalty='elasticnet', max_iter=1000)
    #raval()数据拉平
    sgd_reg.fit(X, y.ravel())
    print(sgd_reg.predict([[1.5]]))

if __name__ == '__main__':
  main()


