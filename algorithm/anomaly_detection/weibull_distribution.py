import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt


def weib(x, n, a):
    return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)


def main():

    #data = np.loadtxt("stack_data.csv")
    data = [-7, 1, 4, -5, 1, -3, 10, -5, -5, 6, 0, -1, -5, 7, -6, 4, 0, -2, 1, 1, -2, 1, -47, 96, -52, 5, -2, -3, 6, -2, -5, 7, -3, -2, 3, 1, -6, 6, 1, -8, 7, 1, -8, 7, 0, -5, 3, 2, -3, 1, 1, -2, 1, -5, 11, -7, 1, 0, 1, -2, 0, 3, -3, 1, 1, -2, 1, 0, 0, 1, -3, 4, -2, -3, 6, -2, -5, 7, -3, -2, 4, -3, 0, 3, -3, 0, 3, -2, -2, 3, 1, -6, 6, 0, -6, 7, -2, -5, 7, -3, -2, 4, -3, 0, 4, -5, 1, 3, -2, -2, 4, -2, -3, 7, -6, 1, 3, -3, 0, 3, -2, -2, 4, -3, 0, 4, -6, 3, 3, -6, 3, 1, -1, 0, 1, -3, 4, -2, -2, 4, -2, -3, 6, -2, -5, 7, -3, -2, 4, -2, -3, 6, -2, -5, 6, -47, 89, -45, 4, -2, -5, 7, -3, -2, 3, 1, -6, 6, 1, -8, 7, 0, -5, 3, 2, -8, 12, -7, 1, 0, 0, 1, -2, 1, 0, 0, 0, 0, 1, -2, 1, 0, 0, 1, -2, 1, 1, -3, 4, -2, -3, 6, -3, -2, 4, -2, -3, 6, -3, -3, 6, -3, -2, 3, 1, -5, 3, 3, -6, 4, 1, -6, 7, -2, -5, 7, -3, -3, 7, -6, 1, 4, -4, -2, 7, -6, 1, 4, -5, 1, 3, -2, -3, 7, -6, 1, 4, -6, 3, 3, -5, 1, 3, -2, -2, 4, -3, 0, 4, -6, 3, 3, -6, 3, 0, 2, -4, 4, -3, 1, 1, -3, 4, -2, -2, 3, 1, -6, 7, -3, -2, 4, -2, -2, 3, 1, -6, 6, -47, 85, -35, 6, 29, -40, -29, 7, 21, 4, -5, 0, 6, -6, 0, 6, -6, 1, 4, -6, 4, 0, -2, 0, 4, -6, 4, 1, -5, 4, 0, -2, 1, 32, -10, -23, -1, 2, 0, 0, 2, -6, 8, -6, -3, -6, -19, 25, 5, 0, 1, -3, 4, -2, -3, 6, -3, -2, 4, -2, -3, 6, -3, -3, 7, -57, 53]
    (loc, scale) = s.exponweib.fit_loc_scale(data, 0.5, 0.5)
    print(loc, scale)
    x = np.linspace(-57, 96, 2000)
    print(x)
    plt.plot(x, weib(x, loc, scale))
    plt.hist(data, 96, normed=True)
    plt.show()


if __name__ == '__main__':
    main()
