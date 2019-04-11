import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



mu5 = 0
sigma = 1
k = [25.15092049,50.87894527,122.0069389,180.4710891,165.8099861,119.513594,58.93023256,33.87767768,16.99270665,11.91949241,10.11398738,3.609153953] # 6种可能出现的结果
"""
X5=[]
i=0
for num in k:
    if i==0:
        X5 = np.append(X5,np.arange(1, 14, 14 / num))
    if i>0 and i<11:
        X5 = np.append(X5, np.arange(14+(i-1)*5+1, 14+i*5, 14 / num))
    i=i+1

print(X5)

mu5 = 24   # 平均值
sigma = 1 # 标准差


y = stats.norm.pdf(X5,mu5,sigma)"""
mu4 = 66  # 平均值：每天发生2次事故
k4 = 4   # 次数，现在想知道每天发生4次事故的概率
# 发生事故次数，包含0次，1次，2次，3次，4次事故
X4 = np.arange(0,12,1)
X4

print(X4)
# In[12]:

'''
第2步，求对应分布的概率：概率质量函数（PMF）
返回一个列表，列表中每个元素表示随机变量中对应值的概率
分别表示发生0次，1次，2次，3次，4次事故的概率
'''


pList4 = stats.norm.pdf(X4,mu4)
# In[13]:
"""
pList4 = stats.poisson.pmf(X4,mu4)
pList4
# 第3步，绘图
plt.plot(X4,pList4,marker='o',linestyle='None')
plt.vlines(X4,0,pList4)
plt.xlabel('某路口发生k次事故')
plt.ylabel('概率')
plt.title('泊松分布：平均值mu=%i' % mu4 )
plt.show()
# In[16]:

# 第3步，绘图
plt.plot(X5,y)
plt.xlabel('随机变量：x')
plt.ylabel('概率：y')
plt.title('正态分布：$\mu$=%.1f,$\sigma^2$=%.1f' % (mu5,sigma))
plt.grid()
plt.show()"""