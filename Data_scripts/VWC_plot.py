import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import saveload as sl


df=sl.load('../../data/OJP/OJP_NW_VWC.pkl')

# Get depths:
z=[]
for col in df.columns:
    print(col)
    x=np.mean([float(i) for i in col.split('_')[1].split('c')[0].split('to')])
    z.append(x)
z=np.array(z)

# Plot
pl.figure(figsize=(12,5))
for col in df.columns:
    pl.plot(df[col])
pl.grid()
pl.ylabel('Volumetric water content')
pl.legend()
pl.savefig('OJP_NW_Timeseries.png',dpi=300)
