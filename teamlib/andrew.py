def SayHello():
    print('Hello team')

def GetBWC_theta():
    from teamlib import saveload as sl
    from teamlib import WiskiTools as wt
    MyList=wt.searchStation('BWC')
    station_name=MyList[47]
    MyTS=wt.searchTimeseries('',station_name)
    indexes=np.arange(70,77)
    print(indexes)

    # Select a data range to work with:
    Start='2001-08-01 00:00:00'
    End='2060-02-08 00:00:00'

    # Extract data into a pandas dataframe:
    TS_Selection=MyTS[indexes]
    df = wt.getTimeseries(TS_Selection,station_name,Start,End)
    sl.save(df,'BWC_soil')