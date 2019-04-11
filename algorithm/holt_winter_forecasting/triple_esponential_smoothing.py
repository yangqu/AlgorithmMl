import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('example.csv')
    playoffs1 = pd.DataFrame({
        'holiday': 'newyear',
        'ds': pd.to_datetime(['2019-02-04']),
        'lower_window': -3,
        'upper_window': 7,
    })
    playoffs2 = pd.DataFrame({
        'holiday': 'start',
        'ds': pd.to_datetime(['2019-01-01']),
        'lower_window': -2,
        'upper_window': 1,
    })
    holidays = pd.concat((playoffs1, playoffs2))
    df['y'] = np.log(df['y'])
    print(df['ds'])
    df['ds'] = pd.to_datetime(df['ds'])

    # 定义模型
    # growth 线性增长和逻辑斯蒂增长
    """ 数据框
        cap饱和上限程度，floor饱和下限程度
        future['cap'] = 6
        future['floor'] = 1.5
        m = Prophet(growth='logistic')

    """
    # changepoints 突变点
    """  突变点的列表，如果没有会自动选择
            changepoints=['2019-02-11'],
    """

    # n_changepoints 突变点个数
    """  突变点的个数
            如果使用了changepoints，则这个参数不会被使用，默认25个，如果没有指定changepoints，则会根据changepoint_range这个比例选取前80%中的25个
    """

    # changepoint_range 突变点范围
    """  突变点的个数
            如果使用了changepoints，则这个参数不会被使用，默认*0%
    """
    # seasonality季节性变化
    """ yearly_seasonality: 年周期
        weekly_seasonality: 周周期
        daily_seasonality: 天周期
    """
    # holidays 假期
    """
    传入pd.dataframe格式的数据。这个数据包含有holiday列 (string)和ds(date类型）和可选列lower_window和upper_window来指定该日期的lower_window或者upper_window范围内都被列为假期。lower_window=-2将包括前2天的日期作为假期
    """

    # scale调节强度
    """ seasonality_prior_scale：季节性模型的调节强度，较大的值允许模型以适应更大的季节性波动，较小的值抑制季节性。
        holidays_prior_scale:假期组件模型的调节强度。
        changepoints_prior_scale:自动的潜在改变点的灵活性调节参数，较大值将允许更多的潜在改变点，较小值将允许更少的潜在改变点。
    """

    # interval_width不确定性区间宽度
    """ 浮点数，给预测提供不确定性区间宽度
    """

    # uncertainty_samples
    """ 模拟绘制数，用于估计不确定的时间间隔
    """
    m = Prophet(holidays=holidays, interval_width=0.95, growth='linear', weekly_seasonality=True)
    # m = Prophet(holidays=holidays, interval_width=1, growth='linear',changepoints=['2019-02-11', '2019-02-12', '2019-02-13', '2019-02-14'],n_changepoints=4)
    """    m = Prophet(holidays=holidays,
                growth='linear',
                #changepoints=['2019-02-11', '2019-02-12', '2019-02-13', '2019-02-14'],
                n_changepoints=25,
                changepoint_range=0.8,
                seasonality_mode='multiplicative',
                interval_width=0.95,
                yearly_seasonality='auto',
                weekly_seasonality='auto',
                daily_seasonality='auto',
                seasonality_prior_scale=10.0,
                holidays_prior_scale=10.0,
                changepoint_prior_scale=0.05,
                uncertainty_samples=1000
                )
"""
    m.add_seasonality(name='weekly', period=7, fourier_order=1, prior_scale=0.1)

    # 训练模型
    m.fit(df)

    # 构建预测集
    future = m.make_future_dataframe(periods=22)

    # 进行预测
    forecast = m.predict(future)

    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10)

    pc = pd.merge(df, forecast, on='ds')
    result = pc.query('y<yhat_lower or y>yhat_upper')
    print(result[['ds', 'y', 'yhat', 'yhat_lower', 'yhat_upper']].sort_values(by="ds"))
    m.plot(forecast)
    plt.show()


if __name__ == '__main__':
    main()