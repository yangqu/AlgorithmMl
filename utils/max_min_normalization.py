import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

__author__ = 'gloom'
def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
def main():
    np.random.seed(1)
    df = pd.read_csv('D:\\tmp\\male.txt', encoding='utf8',sep='\t')
    print(df)

    df_norm = (df['label_count'] - df['label_count'] .min()) / (df['label_count'] .max() - df['label_count'] .min())
    #df_norm = (df[label_count'] - df['tencent_label_parquet.label_count'].mean()) / (df['label_count'].std())
    print(df['label_count'].std)
    stakes = df_norm

    #print(stake)
    std = stakes.std()
    mean = stakes.mean()
    x = np.arange( 0, 1 , 0.02)
    #print(x)
    y = normfun(x, mean, std)
    plt.plot(x, y, 'g', linewidth=3)
    plt.hist(stakes, bins=200, color='b', alpha=0.5, rwidth=0.9, normed=True)
    plt.title('label distribution')
    plt.xlabel('label arrange')
    plt.ylabel('Probability')
    plt.show()


if __name__ == '__main__':
  main()