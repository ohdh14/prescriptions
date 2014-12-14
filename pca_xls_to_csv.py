# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


import numpy as np
import pandas as pd
from glob import glob
from os import path
from datetime import datetime


months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


files = glob('uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/*.xls*')
files = glob('/Users/wellermatt/data/prescriptions/*.xls*')

def read_file(fname):
    basename = path.split(fname)[-1].split('.')[0]
    _, month, year = basename.split('_')
    date = datetime(2000 + int(year), months[month], 1)
    for sn in [0, 1]:
      df = pd.read_excel(fname, header=1, sheetname=sn)    
      df['date'] = pd.Series(date, np.arange(len(df)))
      df['sheet'] = [sn] * len(df)
      if (sn == 0):
          df_out = df
      else:
          df_out = pd.concat([df_out, df])
    return df_out

read_file(files[1])
df = pd.concat([read_file(f) for f in files])

df.to_csv('aggregated_pca.csv', index=False)
