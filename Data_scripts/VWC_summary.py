import matplotlib.pyplot as pl
import pandas as pd
import saveload as sl


df=sl.load('../../data/OJP/OJP_NW_VWC.pkl')

print(df.describe())
