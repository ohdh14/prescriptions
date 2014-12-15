import pandas as pd
import pickle
import glob
import numpy as np
from collections import OrderedDict
import time

directory = '../uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/'
features = OrderedDict()

for f in glob.glob(directory + "*PDPI BNFT.???"):
  t0 = time.time()
  data_all = pd.read_csv(f)
  # Remove trailing spaces from column names...
  data_all.columns = [c.rstrip() for c in data_all.columns]
  period = data_all['PERIOD'].values[0]
  practices = data_all['PRACTICE'].unique()
  print "N practices: ", len(practices)
  
  for p in practices:
    data = data_all[data_all['PRACTICE'] == p]
    if p not in features.keys():
      features[p] = {}
    features[p][period] = OrderedDict()
    
    features[p][period]['N'] = len(data)
    features[p][period]['BNF_NU'] = len(data['BNF CODE'].unique())
    features[p][period]['BNF_NU_N'] = features[p][period]['BNF_NU'] / features[p][period]['N']
    bnfs = list(data['BNF CODE'].values)
    c_max = 0
    for b in data['BNF CODE'].unique():
      c = bnfs.count(b)
      if c > c_max:
        c_max = c
    features[p][period]['BNF_MF'] = c_max
    features[p][period]['BNF_MF_N'] = features[p][period]['BNF_MF'] / features[p][period]['N']
    features[p][period]['items_sum'] = data['ITEMS'].sum()
    features[p][period]['items_mean'] = data['ITEMS'].mean()
    if np.isnan(data['ITEMS'].std()):
      features[p][period]['items_std'] = 0
    else:
      features[p][period]['items_std'] = data['ITEMS'].std()
    
    features[p][period]['nic_sum'] = data['NIC'].sum()
    features[p][period]['nic_mean'] = data['NIC'].mean()
    if np.isnan(data['NIC'].std()):
      features[p][period]['nic_std'] = 0
    else:
      features[p][period]['nic_std'] = data['NIC'].std()  

    features[p][period]['act_sum'] = data['ACT COST'].sum()
    features[p][period]['act_mean'] = data['ACT COST'].mean()
    if np.isnan(data['ACT COST'].std()):
      features[p][period]['act_std'] = 0
    else:
      features[p][period]['act_std'] = data['ACT COST'].std()  
    
    act_nic = data['ACT COST'].values - data['NIC'].values
    features[p][period]['act_nic_sum'] = act_nic.sum()
    features[p][period]['act_nic_mean'] = act_nic.mean()
    if np.isnan(act_nic.std()):
      features[p][period]['act_nic_std'] = 0
    else:
      features[p][period]['act_nic_std'] = act_nic.std()  

    
    features[p][period]['qty_sum'] = data['QUANTITY'].sum()
    features[p][period]['qty_mean'] = data['QUANTITY'].mean()
    if np.isnan(data['QUANTITY'].std()):
      features[p][period]['qty_std'] = 0
    else:
      features[p][period]['qty_std'] = data['QUANTITY'].std()  
  print "Time for file: ", time.time() - t0
  
# Find monthly std for all features
keys = features[p][period].keys()
practices = features.keys()
for i_p, p in enumerate(practices):
  periods = features[p].keys()
  for k in keys:     
    features[p][k + '_sum'] = np.sum([features[p][pp][k] for pp in periods])
    features[p][k + '_mean'] = np.mean([features[p][pp][k] for pp in periods])
    if np.isnan(np.std([features[p][pp][k] for pp in periods])):
      features[p][k + '_std'] = 0
    else:
      features[p][k + '_std'] = np.std([features[p][pp][k] for pp in periods])  

    features[p]['N_periods'] = len(periods)
  for pp in periods:
    del(features[p][pp])

  # Add practitioner to dataframe
  if p == practices[0]:
    features_np = features[p].values()
  else:
    features_np = np.vstack((features_np, features[p].values()))
features_all = pd.DataFrame(features_np, columns = features[p].keys())      
features_all.to_csv('features_practice_all.csv', index=False) 
        
	
