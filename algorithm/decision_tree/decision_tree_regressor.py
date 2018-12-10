import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

__author__ = 'gloom'
"""这是一个最简单的决策树"""
def main():
    #生成列向量的数量
    N = 100
    #生成X
    x = np.random.rand(N) * 6 - 3
    #Xp排序
    x.sort()
    print(x)
    #生成y
    y = np.sin(x) + np.random.rand(N) * 0.05
    print(y)
    #重新调整，变成一列
    x = x.reshape(-1, 1)
    print(x)

    #生成基于回归的决策树，最大深度为3，损失函数为最小二乘法
    dt_reg = DecisionTreeRegressor(criterion='mse', max_depth=3)
    dt_reg.fit(x, y)
    #构建测试集，构建-3到3的30个连续均差样本，变成列向量
    x_test = np.linspace(-3, 3, 50).reshape(-1, 1)
    y_hat = dt_reg.predict(x_test)

    plt.plot(x, y, "y*", label="actual")
    plt.plot(x_test, y_hat, "b-", linewidth=2, label="predict")
    #解释图标出现在左上方
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()
    # plt.savefig("./temp_decision_tree_regressor")


    # 比较不同深度的决策树
    #构建五种深度的树
    depth = [2, 4, 6, 8, 10]
    #每种树结果的颜色不同
    color = 'rgbmy'
    dt_reg = DecisionTreeRegressor()
    plt.plot(x, y, "ko", label="actual")
    x_test = np.linspace(-3, 3, 50).reshape(-1, 1)
    #使用拉链同时取出深度和颜色
    for d, c in zip(depth, color):
        dt_reg.set_params(max_depth=d)
        dt_reg.fit(x, y)
        y_hat = dt_reg.predict(x_test)
        plt.plot(x_test, y_hat, '-', color=c, linewidth=2, label="depth=%d" % d)
    plt.legend(loc="upper left")
    plt.grid(b=True)
    plt.show()
    # plt.savefig("./temp_compare_decision_tree_depth")

if __name__ == '__main__':
  main()
