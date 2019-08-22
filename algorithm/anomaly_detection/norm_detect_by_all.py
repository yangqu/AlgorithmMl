from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time


def main():
    norm_exp_detect()




def norm_exp_detect():
    mean = 237.14045663761172
    std = 10816.295512031003
    fig, axes = plt.subplots(2, 2, figsize=(21, 12))
    exp_x = np.linspace(-80000, 80000, 5000)
    exp_pdf_y = norm.pdf(exp_x, mean, std)
    exp_cdf_y = norm.cdf(exp_x, mean, std)
    dz_simulator_pdf = pd.DataFrame({'y': exp_x, 'ds': exp_pdf_y})
    dz_simulator_cdf = pd.DataFrame({'y': exp_x, 'ds': exp_cdf_y})
    dz_simulator_pdf.plot(title="{0}".format("test"), ax=axes[0][0], x="y", y="ds")
    dz_simulator_cdf.plot(title="{0}".format("test"), ax=axes[0][1], x="y", y="ds")

    print(norm.cdf(7200, mean, std))
    print(7200.0/3600)

    plt.show()





if __name__ == '__main__':
    main()
