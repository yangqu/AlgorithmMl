import pandas as pd
from pandas.core.frame import DataFrame

def main():
    file_list = ["gap_400"]
    for file in file_list:
        df = pd.read_csv("../resource/{0}.csv".format(file))
        df['time'] = pd.to_datetime(df['time'], format="%Y-%m-%d %H:%M:%S")
        #df = df.set_index('time', 'device')
        device_df = df.drop_duplicates(subset=['device'], keep='first', inplace=False)
        #print(df)
        rng = pd.date_range(start='2019/07/15 00:00:00', end="2019/07/19 00:20:00", freq='10T').get_values()

        frame_rng = {"time": rng}
        data = DataFrame(frame_rng)
        da = getMergeAB(data, device_df)
        #print(da)
        ra = pd.merge(da, df, how='left', on=['time', 'device'])
        print(ra.fillna(0))
        ra.fillna(0).to_csv('../resource/result.csv', index=False, sep=',')

def getMergeAB(A, B):
    new_df = DataFrame(columns=['time', 'device'])
    i = 0
    for _, A_row in A.iterrows():
        i = i+1
        for _, B_row in B.iterrows():

            a_data = A_row['time']
            print(a_data)
            b_data = B_row['device']
            row = DataFrame([dict(time=a_data, device=b_data)])
            new_df = new_df.append(row, ignore_index=True)
        #if i > 5:
         #   break
    return new_df


def etl(df, name):
    pass


if __name__ == '__main__':
    main()
