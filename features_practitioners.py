import pandas as pd
import pickle
import glob
import numpy as np

directory = '../uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/'
features = {}
# Get all unique pratitioners
#practices = []
#for f in glob.glob(directory + "*PDPI BNFT.???"):
#  print f
#  data = pd.read_csv(f)
#  practices.append(data['PRACTICE'].unique())    
#practices = list(set(practices))
#print len(practices)

for f in glob.glob(directory + "*PDPI BNFT.???")[:5]:
  data_all = pd.read_csv(f)
  # Remove trailing spaces from column names...
  data_all.columns = [c.rstrip() for c in data_all.columns]
  period = data_all['PERIOD'].values[0]
  practices = data_all['PRACTICE'].unique()
  print "N practices: ", len(practices)
  
  for p in practices[:20]:
    data = data_all[data_all['PRACTICE'] == p]
    if p not in features.keys():
      features[p] = {}
    features[p][period] = {}
    
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
    features[p][period]['items_std'] = data['ITEMS'].std() or 0
    
    features[p][period]['nic_sum'] = data['NIC'].sum()
    features[p][period]['nic_mean'] = data['NIC'].mean()
    features[p][period]['nic_std'] = data['NIC'].std() or 0
    
    features[p][period]['act_sum'] = data['ACT COST'].sum()
    features[p][period]['act_mean'] = data['ACT COST'].mean()
    features[p][period]['act_std'] = data['ACT COST'].std() or 0

    act_nic = data['ACT COST'].values - data['NIC'].values
    features[p][period]['act_nic_sum'] = act_nic.sum()
    features[p][period]['act_nic_mean'] = act_nic.mean()
    features[p][period]['act_nic_std'] = act_nic.std() or 0
    
    features[p][period]['qty_sum'] = data['QUANTITY'].sum()
    features[p][period]['qty_mean'] = data['QUANTITY'].mean()
    features[p][period]['qty_std'] = data['QUANTITY'].std() or 0


    
# Find monthly std for all features
keys = features[p][period].keys()
practices = features.keys()
for i_p, p in enumerate(practices):
  #if p in features:
  periods = features[p].keys()
  print "Periods: ", periods
  for k in keys:     
    if k == "N":
      print [features[p][pp][k] for pp in periods]
      print "Sum: ",  np.sum([features[p][pp][k] for pp in periods])
      print "mean: ",  np.mean([features[p][pp][k] for pp in periods])
      print "Std: ",  np.std([features[p][pp][k] for pp in periods])
    features[p][k + '_sum'] = np.sum([features[p][pp][k] for pp in periods])
    features[p][k + '_mean'] = np.mean([features[p][pp][k] for pp in periods])
    features[p][k + '_std'] = np.std([features[p][pp][k] for pp in periods]) or 0
    features[p]['N_periods'] = len(periods)
  for pp in periods:
    del(features[p][pp])

  # Add practitioner to dataframe
  if p == practices[0]:
    features_np = features[p].values()
    #features_all = pd.DataFrame(np.array([features[p].values()]), columns = features[p].keys())
  else:
    features_np = np.vstack((features_np, features[p].values()))
    
    #features_all.loc[i_p] = features[p].values()
    #features_all.loc[i_p] = features[p].values()
features_all = pd.DataFrame(features_np, columns = features[p].keys())      
features_all.to_csv('features_practice.csv', index=False) 
        
	
