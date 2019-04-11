# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'gloom'

def main():
    x = np.array([[1], [2], [3]])
    y = np.array([4, 5, 6])

    # 对 y 广播 x
    b = np.broadcast(x, y)
    # 它拥有 iterator 属性，基于自身组件的迭代器元组

    print('对 y 广播 x：')
    r, c = b.iters

    # Python3.x 为 next(context) ，Python2.x 为 context.next()
    #print(next(r), next(c))
    #print(next(r), next(c))
    for zzo in c:
        print(zzo)
    print('\n')
    # shape 属性返回广播对象的形状
if __name__ == '__main__':
    main()