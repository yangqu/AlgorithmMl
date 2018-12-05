# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

__author__ = 'gloom'
"""这个类多项式回归，主要用作升维来进行非线性的拟合，基本思想为多项式转换，利用次幂的方式让本来属于低维度的方程映射到高维空间，但是多项式回归本身只是特征的处理，生成模型仍旧要带入的线性回归"""
def main():
    #老两样，继续生成X和Y,不一样的地方是不用生成X0，只不过这个把个数放进了m中
    m = 100
    X = 6 * np.random.rand(m, 1) - 3
    y = 0.5 * X ** 2 + X + 2 + np.random.randn(m, 1)
    #画出X和Y，使用蓝色的点绘制
    plt.plot(X, y, 'b.')
    #生成d的字典，不同的参数不同的颜色，分别为一维对应绿色直线，二维对应红色加号，10维对应黄色*
    d = {1: 'g-', 2: 'r+', 10: 'y*'}
    for i in d:
        #使用多项式回归进行转化，degree超参数代表维度，include_bias超参数代表列是否有别名
        poly_features = PolynomialFeatures(degree=i, include_bias=False)
        #生成高维空间的多项式
        X_poly = poly_features.fit_transform(X)
        print(X[0])
        print(X_poly[0])
        print(X_poly[:, 0])
        #使用线性回归，fit_intercept这个默认是true，是否存在截距，也就是X0这块的值
        lin_reg = LinearRegression(fit_intercept=True)
        #进行模型训练
        lin_reg.fit(X_poly, y)
        #打印截距，scikit-learn库中将结果存放为coef_
        print(lin_reg.intercept_, lin_reg.coef_)
        #针对X_poly进行预测
        y_predict = lin_reg.predict(X_poly)
        #生成图，X轴为切片所有的列里边选择第一列，y轴为预测值
        plt.plot(X_poly[:, 0], y_predict, d[i])

    plt.show()

if __name__ == '__main__':
  main()


