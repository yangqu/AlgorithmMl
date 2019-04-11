import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
"""
n = 100
k = np.arange(0 , 100)
tencent = 0.187981516
gaode = 0.465828033
binomial_tencent =stats.binom.pmf(k,n,tencent)
binomial_gaode =stats.binom.pmf(k,n,gaode)
plt.plot(k,binomial_tencent,'o-',label='tencent')
plt.plot(k,binomial_gaode,'o-',label='gaode')
plt.title('PMF : n=%i, ' % n, fontsize=15)
plt.xlabel('Number of Having House')
plt.ylabel('Probabillity', fontsize=15)
plt.legend(['tencent','gaode'])
plt.show()
"""

n = 100
k = np.arange(0 , 100)
tencent = 0.611796412
gaode = 0.238783015
binomial_tencent =stats.binom.pmf(k,n,tencent)
binomial_gaode =stats.binom.pmf(k,n,gaode)
plt.plot(k,binomial_tencent,'o-',label='tencent')
plt.plot(k,binomial_gaode,'o-',label='gaode')
plt.title('PMF : n=%i, ' % n, fontsize=15)
plt.xlabel('Number of Having Car')
plt.ylabel('Probabillity', fontsize=15)
plt.legend(['tencent','gaode'])
plt.show()