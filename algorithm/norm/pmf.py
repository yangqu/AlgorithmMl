import pandas
import numpy as np

from collections import Counter
import copy
import logging


class _DictWrapper(object):

    # 此处代码请参考《统计思维（实例1）》
    # 下面为该类新加代码

    def __iter__(self):
        return iter(self.d)

    # 返回keys迭代器
    def iterkeys(self):
        return iter(self.d)

    # 返回浅拷贝
    def Copy(self, label=None):
        new = copy.copy(self)
        new.d = copy.copy(self.d)
        new.label = label if label is not None else self.label
        return new

    # 计算值和频率乘积
    def Mult(self, x, factor):
        self.d[x] = self.d.get(x, 0) * factor

    # 返回Map中频率的总和
    def Total(self):
        total = sum(self.d.values())
        return total


# Pmf对象
class Pmf(_DictWrapper):

    def Prob(self, x, default=0):
        return self.d.get(x, default)

    # 计算PMF的均值
    def Mean(self):
        mean = 0.0
        for x, p in self.d.items():
            mean += p * x
        return mean

    # PMF的归一化
    def Normalize(self, fraction=1.0):
        if self.log:
            raise ValueError("Normalize: Pmf is under a log transform")

        total = self.Total()
        if total == 0.0:
            raise ValueError('Normalize: total probability is zero.')

        factor = fraction / total
        for x in self.d:
            self.d[x] *= factor

        return total

d = {7: 8, 12: 8, 17: 14, 22: 4,
     27: 6, 32: 12, 37: 8, 42: 3, 47: 2}


def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, p)

    new_pmf.Normalize()
    return new_pmf
