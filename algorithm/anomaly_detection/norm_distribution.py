from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time


def main():
    norm_exp_detect()


def my_norm():
    x = [-7, 1, 4, -5, 1, -3, 10, -5, -5, 6, 0, -1, -5, 7, -6, 4, 0, -2, 1, 1, -2, 1,
         -47, 96, -52, 5, -2, -3, 6, -2, -5, 7, -3, -2, 3, 1, -6, 6, 1, -8, 7, 1, -8,
         7, 0, -5, 3, 2, -3, 1, 1, -2, 1, -5, 11, -7, 1, 0, 1, -2, 0, 3, -3, 1, 1, -2,
         1, 0, 0, 1, -3, 4, -2, -3, 6, -2, -5, 7, -3, -2, 4, -3, 0, 3, -3, 0, 3, -2,
         -2, 3, 1, -6, 6, 0, -6, 7, -2, -5, 7, -3, -2, 4, -3, 0, 4, -5, 1, 3, -2, -2,
         4, -2, -3, 7, -6, 1, 3, -3, 0, 3, -2, -2, 4, -3, 0, 4, -6, 3, 3, -6, 3, 1, -1,
         0, 1, -3, 4, -2, -2, 4, -2, -3, 6, -2, -5, 7, -3, -2, 4, -2, -3, 6, -2, -5, 6,
         -47, 89, -45, 4, -2, -5, 7, -3, -2, 3, 1, -6, 6, 1, -8, 7, 0, -5, 3, 2, -8, 12,
         -7, 1, 0, 0, 1, -2, 1, 0, 0, 0, 0, 1, -2, 1, 0, 0, 1, -2, 1, 1, -3, 4, -2, -3,
         6, -3, -2, 4, -2, -3, 6, -3, -3, 6, -3, -2, 3, 1, -5, 3, 3, -6, 4, 1, -6, 7, -2,
         -5, 7, -3, -3, 7, -6, 1, 4, -4, -2, 7, -6, 1, 4, -5, 1, 3, -2, -3, 7, -6, 1, 4,
         -6, 3, 3, -5, 1, 3, -2, -2, 4, -3, 0, 4, -6, 3, 3, -6, 3, 0, 2, -4, 4, -3, 1,
         1, -3, 4, -2, -2, 3, 1, -6, 7, -3, -2, 4, -2, -2, 3, 1, -6, 6, -47, 85, -35, 6,
         29, -40, -29, 7, 21, 4, -5, 0, 6, -6, 0, 6, -6, 1, 4, -6, 4, 0, -2, 0, 4, -6,
         4, 1, -5, 4, 0, -2, 1, 32, -10, -23, -1, 2, 0, 0, 2, -6, 8, -6, -3, -6, -19,
         25, 5, 0, 1, -3, 4, -2, -3, 6, -3, -2, 4, -2, -3, 6, -3, -3, 7, -57, 53]
    x.sort()
    y = norm.cdf(x, np.mean(x), np.std(x))
    print(norm.sf(x, np.mean(x), np.std(x)))

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def my_detect():
    file_list = ["result"]
    for file in file_list:
        df = pd.read_csv("../../resource/{0}.csv".format(file))
        device_df = df.drop_duplicates(subset=['device'], keep='first', inplace=False)
        for device in device_df.values:
            df_simple = df[(df.device == device[0])]
            df_simple = df_simple.rename(index=str, columns={"time": "ds", "stat": "y"})
            dz = df_simple[['ds', 'y']]
            dz_copy = dz.copy()
            dz_org = dz_copy.iloc[0: 250, :]
            dz_train = dz.iloc[0: 250, :]
            # dz_test = dz.iloc[251:, :]

            if True:
                fig, axes = plt.subplots(2, 2, figsize=(20, 12))
                dz_train = dz_train[dz_train['y'] > 0]
                dz_train['y'] = dz_train['y'].diff().diff()
                dz_train = dz_train.dropna()
                dz_diff = dz_train.sort_values(by='y', ascending=True)
                print(np.mean(dz_diff['y']), np.std(dz_diff['y']))

                dz_org['ds'] = pd.to_datetime(dz_org['ds'], format="%Y-%m-%d %H:%M:%S")
                dz_diff['ds'] = pd.to_datetime(dz_diff['ds'], format="%Y-%m-%d %H:%M:%S")
                dz_diff.plot(title="{0}".format(device[0]), ax=axes[0][1], x="ds", y="y")
                dz_org.plot(title="{0}".format(device[0]), ax=axes[0][0], x="ds", y="y")

                dz_diff['ds'] = norm.pdf(dz_diff['y'], np.mean(dz_diff['y']), np.std(dz_diff['y']))
                dz_diff.plot(title="{0}".format(device[0]), ax=axes[1][0], x="y", y="ds")
                dz_diff['ds'] = norm.cdf(dz_diff['y'], np.mean(dz_diff['y']), np.std(dz_diff['y']))
                dz_diff.plot(title="{0}".format(device[0]), ax=axes[1][1], x="y", y="ds")

                plt.show()


def my_series_detect():
    file_list = ["device3"]
    for file in file_list:
        df = pd.read_csv("../../resource/{0}.csv".format(file))
        device_df = df.drop_duplicates(subset=['device'], keep='first', inplace=False)
        for device in device_df.values:
            df_simple = df[(df.device == device[0])]
            df_simple = df_simple.rename(index=str, columns={"time": "ds", "device": "y"})
            dz = df_simple[['ds', 'y']]
            # dz_train = dz.iloc[0: 2500, :]
            dz_train = dz
            # dz_test = dz.iloc[2501:, :]

            if True:
                fig, axes = plt.subplots(2, 2, figsize=(20, 12))
                dz_train['y'] = dz_train['ds'].apply(lambda x: time.mktime(time.strptime(str(x), '%Y%m%d%H%M%S')))
                dz_train['ds'] = pd.to_datetime(dz_train['ds'], format="%Y%m%d%H%M%S")
                dz_train = dz_train.sort_values(by='ds', ascending=True)
                dz_train['y'] = dz_train['y'].diff().diff()
                dz_train = dz_train.dropna()
                # dz_train = dz_train.drop_duplicates(subset=None, keep='first', inplace=False)

                mean_r = np.mean(dz_train['y'])
                std_r = np.std(dz_train['y'])
                print(3 * std_r)
                dz_train = dz_train[abs(dz_train['y']) < 3 * std_r]
                print(dz_train)
                dz_train.plot(title="{0}".format(device[0]), ax=axes[0][1], x="ds", y="y")
                # dz_org.plot(title="{0}".format(device[0]), ax=axes[0][0], x="ds", y="y")
                print(norm.cdf([600], mean_r, std_r))
                dz_train['ds'] = norm.pdf(dz_train['y'], mean_r, std_r)
                dz_train = dz_train.sort_values(by='y', ascending=True)
                dz_train.plot(title="{0}".format(device[0]), ax=axes[1][0], x="y", y="ds")
                dz_train['ds'] = norm.cdf(dz_train['y'], mean_r, std_r)
                dz_train.plot(title="{0}".format(device[0]), ax=axes[1][1], x="y", y="ds")

                plt.show()


def norm_exp_detect():
    file_list = ["device3"]
    for file in file_list:
        df = pd.read_csv("../../resource/{0}.csv".format(file))
        device_df = df.drop_duplicates(subset=['device'], keep='first', inplace=False)
        for device in device_df.values:
            df_simple = df[(df.device == device[0])]
            df_simple = df_simple.rename(index=str, columns={"time": "ds", "device": "y"})
            dz = df_simple[['ds', 'y']]
            dz_train = dz.copy()

            if True:
                fig, axes = plt.subplots(4, 2, figsize=(21, 12))
                dz_train['y'] = dz_train['ds'].apply(lambda x: time.mktime(time.strptime(str(x), '%Y%m%d%H%M%S')))
                dz_train['ds'] = pd.to_datetime(dz_train['ds'], format="%Y%m%d%H%M%S")
                dz_train = dz_train.sort_values(by='ds', ascending=True)
                dz_exp_tail = dz_train.iloc[-3:-1]

                dz['y'] = dz['ds'].apply(lambda x: time.mktime(time.strptime(str(x), '%Y%m%d%H%M%S')))
                dz['ds'] = pd.to_datetime(dz_train['ds'], format="%Y%m%d%H%M%S")
                dz = dz.sort_values(by='ds', ascending=True)
                dz['y'] = dz['y'].diff()

                dz_train['y'] = dz_train['y'].diff().diff()
                dz_train = dz_train.dropna()

                # mean_r = np.mean(dz_train['y'])
                std_r = np.std(dz_train['y'])
                dz_exp = dz_train[abs(dz_train['y']) >= 3 * std_r]
                dz_train = dz_train[abs(dz_train['y']) < 3 * std_r]
                mean_r = np.mean(dz_train['y'])
                std_r = np.std(dz_train['y'])

                dz_exp['y'] = dz_exp['y'].apply(lambda x: abs(x))

                mean_exp = np.mean(dz_exp['y'])
                std_exp = np.std(dz_exp['y'])
                # dz_exp['y'] = dz_exp['y'].apply(lambda x: abs(x) - mean_exp)
                # print(dz_exp)

                dz.plot(title="{0}".format(device[0]), ax=axes[0][0], x="ds", y="y")
                dz_train.plot(title="{0}".format(device[0]), ax=axes[0][1], x="ds", y="y")

                dz_train['ds'] = norm.pdf(dz_train['y'], mean_r, std_r)
                dz_train = dz_train.sort_values(by='y', ascending=True)
                dz_train.plot(title="{0}".format(device[0]), ax=axes[1][0], x="y", y="ds")
                dz_train['ds'] = norm.cdf(dz_train['y'], mean_r, std_r)
                dz_train.plot(title="{0}".format(device[0]), ax=axes[1][1], x="y", y="ds")

                dz_exp['ds'] = norm.pdf(dz_exp['y'], mean_exp, std_exp)
                dz_exp = dz_exp.sort_values(by='y', ascending=True)
                dz_exp.plot(title="{0}".format(device[0]), ax=axes[2][0], x="y", y="ds")
                dz_exp['ds'] = norm.cdf(dz_exp['y'], mean_exp, std_exp)
                dz_exp.plot(title="{0}".format(device[0]), ax=axes[2][1], x="y", y="ds")
                test_detect(dz_train, dz_exp, dz_exp_tail)

                exp_x = np.linspace(0, 2 * mean_exp, 10)
                exp_pdf_y = norm.pdf(exp_x, mean_exp, std_exp)
                exp_cdf_y = norm.cdf(exp_x, mean_exp, std_exp)
                dz_simulator_pdf = pd.DataFrame({'y': exp_x, 'ds': exp_pdf_y})
                dz_simulator_cdf = pd.DataFrame({'y': exp_x, 'ds': exp_cdf_y})
                dz_simulator_pdf.plot(title="{0}".format(device[0]), ax=axes[3][0], x="y", y="ds")
                dz_simulator_cdf.plot(title="{0}".format(device[0]), ax=axes[3][1], x="y", y="ds")


                plt.show()


def test_detect(dz_train, dz_exp, dz_exp_tail):
    test = "2019-07-25 17:20:48"
    print(dz_exp_tail)
    my_time = time.strptime(test, "%Y-%m-%d %H:%M:%S")
    my_stamp = int(time.mktime(my_time)) + 28800
    dz_exp_tail_array = dz_exp_tail['ds'].values.tolist()

    st2 = my_stamp
    st1 = int(dz_exp_tail_array[1] / 1e9)
    st0 = int(dz_exp_tail_array[0] / 1e9)

    diff_st = st2 - 2 * st1 + st0

    prob_norm = dz_train['ds'] = norm.cdf(diff_st, np.mean(dz_train['y']), np.std(dz_train['y']))
    prob_exp = dz_exp['ds'] = norm.cdf(diff_st, np.mean(dz_exp['y']), np.std(dz_exp['y']))
    prob_r = (prob_norm + prob_exp) / 2

    print("st2: " + str(st2))
    print("st1: " + str(st1))
    print("st0: " + str(st0))
    print("diff_st: " + str(diff_st))
    print("normal: " + str(prob_norm))
    print("exp: " + str(prob_exp))
    print("complex: " + str(prob_r))


if __name__ == '__main__':
    main()
