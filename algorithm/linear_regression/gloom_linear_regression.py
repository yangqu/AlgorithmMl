# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'gloom'

def main():
    # 这里相当于是随机X维度X1，rand是随机均匀分布
    # ps:np.random.rand(100, 1)为100个小于1的数值
    X = 2 * np.random.rand(100, 1)
    # 人为的设置真实的Y一列，np.random.randn(100, 1)是设置error，randn是标准正太分布
    # ps:这里4是一个常数，np.random.randn(100, 1)是为了让X0这个参数也是一个正太分布的数值
    y = 4 + 3 * X + np.random.randn(100, 1)
    # 整合X0和X1
    # ps:这里之所以要生成X_b,是因为最后的等式是y=X0*b+k*X1,这里需要构造出[X0,X1]的矩阵，自然X0等于1，X1就是之前生成的X
    X_b = np.c_[np.ones((100, 1)), X]
    #print(X_b)

    # 常规等式求解theta
    # linalg是numpy的一个线性代数函数，里边包含了线性代数很多相关运算，np.linalg.inv是矩阵取逆，使用dot函数检查求得的解是否正确
    # 这里用来计算模型的方式是解析解方式，计算量较大
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    print(theta_best)

    # 创建测试集里面的X1，此处是生成一个1维的矩阵
    X_new = np.array([[0], [2]])
    # 和之前的操作一样，添加X0为1
    X_new_b = np.c_[(np.ones((2, 1))), X_new]
    print(X_new_b)
    #使用之前训练的模型来预测y的值
    y_predict = X_new_b.dot(theta_best)
    print(y_predict)

    #使用绘图工具，plot是生成图，第一个参数为x轴，第二个参数为y轴，第三个参数为颜色和展现形式，r-为公司线，b. 为蓝色点
    plt.plot(X_new, y_predict, 'r-')
    plt.plot(X, y, 'b.')
    #画布的大小xmin, xmax, ymin, ymax = axis(xmin, xmax, ymin, ymax)
    plt.axis([0, 2, 0, 15])
    #展示画布
    plt.show()

if __name__ == '__main__':
  main()

