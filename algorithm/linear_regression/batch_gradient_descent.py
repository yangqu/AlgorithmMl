# -*- coding: UTF-8 -*-

"""使用梯度下降的方式求最优解，主要原因是解析解的方式计算量非常大，涉及到矩阵的转置等操作"""
import numpy as np

__author__ = 'gloom'

def main():
    #仍旧是老套路，先生成一个随机的X，这个X是一个列向量，100个X值组成的列向量，这个X只能说是随机，不能说是完全正态分布
    X = 2 * np.random.rand(100, 1)
    #依然是老套路，使用X和Y构建方程，但是这个方程式向量组成的，不是单个的值，所以y=kx+b中的b是1以内的正太分布随机数值
    y = 4 + 3 * X + np.random.randn(100, 1)
    #构成新的向量，这个向量的意义在意X1仍旧是X，X0默认为1
    X_b = np.c_[np.ones((100, 1)), X]
    # print(X_b)
    #这个超参数是梯度下降中的学习率，可以看作是步长
    learning_rate = 0.1
    #这个是迭代次数，迭代多少次收敛
    n_iterations = 10000
    #平均数，一般为数据个数
    m = 100

    # 1，初始化theta，w0...wn
    theta = np.random.randn(2, 1)
    count = 0

    # 4，不会设置阈值，之间设置超参数，迭代次数，迭代次数到了，我们就认为收敛了
    for iteration in range(n_iterations):
        count += 1
        # 2，接着求梯度gradient
        gradients = 1/m * X_b.T.dot(X_b.dot(theta)-y)
        # 3，应用公式调整theta值，theta_t + 1 = theta_t - grad * learning_rate
        theta = theta - learning_rate * gradients

    print(count)
    print(theta)

if __name__ == '__main__':
  main()








