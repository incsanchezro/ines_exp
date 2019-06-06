import saveload as sl
import WiskiTools as wt
import numpy as np
import shutil
import glob

# Select a data range to work with:
Start='1900-08-01 00:00:00'
End='2060-02-08 00:00:00'

# List of stations
MyList=wt.searchStation('OJP')

# Station for AE:
station_name=MyList[3]
MyTS=wt.searchTimeseries('',station_name)
indexes=np.arange(8,9)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_AE')

# Station for precipitation:
station_name=MyList[5]
MyTS=wt.searchTimeseries('',station_name)
indexes=np.arange(0,5)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_Precip')

# Station for snow depth:
station_name=MyList[6]
MyTS=wt.searchTimeseries('',station_name)
indexes=np.arange(0,3)
TS_Selection=MyTS[indexes]
df = wt.getTimeseries(TS_Selection,station_name,Start,End)
sl.save(df,'OJP_Snow')



# Move pkl files to the data folder:
destinationfolder='../../data/OJP'
for f in glob.glob('*.pkl'):
    shutil.move(f,destinationfolder)
