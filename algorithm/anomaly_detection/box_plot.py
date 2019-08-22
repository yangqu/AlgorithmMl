import pandas as pd
import matplotlib.pyplot as plt

ratio_zero = 1.0 / 24
ratio_exp = 2.0 / 24
ratio_combine = 0.9
ratio_zero_top = 12.0 / 24

"""
def main():
    file_list = ["gap_alert_normal", "gap_alert_exp", "gap_alert_test"]
    for file in file_list:
        df = pd.read_csv("../../resource/{0}.csv".format(file))
        if ~detect(df, file):
            data = df.plot.box(title="Box Plot", return_type='dict')
            plt.grid(linestyle="--")
            y = data['fliers'][0].get_ydata()
            y.sort()
            plt.show()
"""


def main():

    file_list = ["result"]
    for file in file_list:
        df = pd.read_csv("../../resource/{0}.csv".format(file))
        device_df = df.drop_duplicates(subset=['device'], keep='first', inplace=False)
        for device in device_df.values:
            df_simple = df[(df.device == device[0])]

            df_simple = df_simple.rename(index=str, columns={"time": "ds", "stat": "y"})
            dz = df_simple[['ds', 'y']]
            is_exp = detect(dz, device[0])
            if True:
                name = is_exp
                fig, axes = plt.subplots(2, 1, figsize=(10, 6))
                data = dz.plot.box(title="{0} {1}".format(device[0], name), return_type='dict',
                                   ax=axes[0], fontsize=10)
                plt.grid(linestyle="--")
                y = data['fliers'][0].get_ydata()
                y.sort()
                dz['ds'] = pd.to_datetime(dz['ds'], format="%Y-%m-%d %H:%M:%S")
                max_value = df_simple.max()
                dz.plot(title="{0}".format("Max ------ " + str(max_value[2])), ax=axes[1], x="ds", y="y")
                plt.show()


def detect(df, name):

    result = cal(df)
    if result.startswith("OK!"):
        print("{0} 设备未发现异常 {1}".format(name, result))
    else:
        print("{0} 设备存在异常 {1}".format(name, result))
    return result


def cal(df):

    iqr = df.quantile(0.75) - df.quantile(0.25)
    top = df.quantile(0.75) + 1.5 * iqr
    bottom = df.quantile(0.25) - 1.5 * iqr
    normal = df[(df.y <= top[0]) & (df.y >= bottom[0])]
    exp = df[(df.y > top[0]) | (df.y < bottom[0])]

    less = df[df.y < bottom[0]]
    more = df[df.y > top[0]]
    zero = df[df.y == 0]

    avg_normal = normal.mean()
    avg_exp = exp.mean()
    avg_all = df.mean()

    less_zize = less.size
    more_zize = more.size
    zero_zize = zero.size

    zero_ = zero_zize / df.size
    exp_ = (less_zize + more_zize) / df.size

    if (zero_ > ratio_zero) & (avg_normal[0] * ratio_combine <= avg_exp[0]):
        pass

    if (exp_ > ratio_exp) & (avg_normal[0] * ratio_combine <= avg_exp[0]):
        pass

    if (zero_ > ratio_zero) | (exp_ > ratio_exp):
        if zero_ > ratio_zero_top:
            return "Exception more zero ------ zero: {0} / all: {1}".format(str(zero_zize), str(df.size))
        if avg_normal[0] * ratio_combine <= avg_all[0]:
            return "OK! ------ " + "exp: " + str(round(avg_exp[0], 2)) + \
                   " / normal: " + str(round(avg_normal[0], 2)) + \
                   " / all: " + str(round(avg_all[0], 2))
        else:
            return "Exception data missing ------ " + "exp: " + str(round(avg_exp[0], 2)) + \
                   " / normal: " + str(round(avg_normal[0], 2)) + \
                   " / all: " + str(round(avg_all[0], 2))

    return "OK!"


if __name__ == '__main__':
    main()
