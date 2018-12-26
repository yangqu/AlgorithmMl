# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'gloom'

def main():
    # 这里相当于是随机X维度X1，rand是随机均匀分布
    X =  np.random.rand(100, 1)
    print(np.ones((100, 1)))
def test_array():
    result = ['basic_info','gender/female','0.5','262727688','0.5411']
    result.insert(2, '' if not result[1].__contains__('/') else result[1].split('/')[1])
    result[1]=result[1] if not result[1].__contains__('/') else result[1].split('/')[0]
    print(result)


if __name__ == '__main__':
    print(list(filter(lambda x: x % 2 == 0, range(1, 21))))
    test_array()

