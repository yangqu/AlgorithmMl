import numpy as np
import matplotlib.pyplot as plt
k = [25.15092049,50.87894527,122.0069389,180.4710891,165.8099861,119.513594,58.93023256,33.87767768,16.99270665,11.91949241,10.11398738,3.609153953] # 6种可能出现的结果
k2=[7.075387274,47.62927681,205.9088245,292.3070451,273.2913841,238.8250092,174.6591487,135.3161958,82.04496155,63.20359386,48.49936609,45.33279942]
X5=[]
X6=[]
i=0

#pp=
for num in k:
    num=num*100
    if i==0:
        X5 = np.append(X5,np.arange(1, 14, 14 / num))
        #X5 = np.append(X5, np.random.normal(1, 14, int( num)))
    if i>0 and i<11:
        X5 = np.append(X5, np.arange(14+(i-1)*5, 14+i*5, 14 / num))
        #X5 = np.append(X5, np.random.normal(14 + (i - 1) * 5 + 1, 14 + i * 5,  int( num)))
    i=i+1
i=0
for num in k2:
    num = num*100
    if i==0:
        X6 = np.append(X5,np.arange(1, 14, 14 / num))
        #X6 = np.append(X5, np.random.normal(1, 14,  int( num)))
    if i>0 and i<11:
        X6 = np.append(X5, np.arange(14+(i-1)*5, 14+i*5, 14 / num))
        #X6 = np.append(X5, np.random.normal(14 + (i - 1) * 5 + 1, 14 + i * 5,  int( num)))
    i = i + 1
mu5=np.mean(X5)
sigma5 =np.std(X5)
mu6=np.mean(X6)
sigma6 =np.std(X6)

print(X5)
# = np.random.normal(mu, sigma, num)
count5, bins5, ignored5 = plt.hist(X5, 12, normed=True,label='tt')
plt.plot(bins5, 1/(sigma5 * np.sqrt(2 * np.pi)) *np.exp( - (bins5 - mu5)**2 / (2 * sigma5**2)), linewidth=2, color='orange',label='tencent')
count6, bins6, ignored6 = plt.hist(X6, 12, normed=True,label='gg')
plt.plot(bins6, 1/(sigma6 * np.sqrt(2 * np.pi)) *np.exp( - (bins6 - mu6)**2 / (2 * sigma6**2)), linewidth=2, color='blue',label='gaode')
plt.legend(['tt','gg'])
plt.show()