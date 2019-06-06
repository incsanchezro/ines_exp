import saveload as sl
import WiskiTools as wt
import numpy as np
import shutil
import glob

MyList=wt.searchStation('OJP')
station_name=MyList[8]
MyTS=wt.searchTimeseries('',station_name)

# Select a data range to work with:
Start='1900-08-01 00:00:00'
End='2060-02-08 00:00:00'

# NW VWC data
indexes=np.arange(21,33,2)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_NW_VWC')

# SW VWC data
indexes=np.arange(22,33,2)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_SW_VWC')

# NW Temperature data
indexes=np.arange(0,12,2)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_NW_T')

# SW Temperature data
indexes=np.arange(1,12,2)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_SW_T')

# Move pkl files to the data folder:
destinationfolder='../../data/OJP'
for f in glob.glob('*.pkl'):
    shutil.move(f,destinationfolder)
