""" Create the statistical features for all the practition
    This use all the files, they are processed in parrallel using all available cores 
"""

import pandas as pd
import pickle
import glob
import numpy as np
from collections import OrderedDict
import time
import os.path
import pickle
import multiprocessing

directory = '../uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/'
# For debugging
#logger = multiprocessing.log_to_stderr()
#logger.setLevel(multiprocessing.SUBDEBUG)

def make_features(f):
  """ Makes the features for a file 
      Saves the output in a pickle file, same as f but with a .pkl extension 
  """
  t0 = time.time()
  data_all = pd.read_csv(f)
  data_all.columns = [c.rstrip() for c in data_all.columns] # Remove trailing spaces from column names...
  features = OrderedDict()
  
  period = data_all['PERIOD'].values[0]
  features[period] = OrderedDict()
  practices = data_all['PRACTICE'].unique()
  print "N practices: ", len(practices)
  
  for p in practices:
    #t00 = time.time()
    data = data_all[data_all['PRACTICE'] == p]
    #print "Time to extract practice data: ", time.time() - t00
    
    if p not in features[period].keys():
      features[period][p] = OrderedDict()
    
    features[period][p]['N'] = len(data)
    bnfs = [b[:9] for b in data['BNF CODE'].values]
    features[period][p]['BNF_NU'] = len(set(bnfs))
    features[period][p]['BNF_NU_N'] = features[period][p]['BNF_NU'] / float(features[period][p]['N'])
        
    c_max = 0
    for b in set(bnfs):
      c = bnfs.count(b[:9])
      if c > c_max:
        c_max = c

    features[period][p]['BNF_MF'] = c_max
    features[period][p]['BNF_MF_N'] = features[period][p]['BNF_MF'] / float(features[period][p]['N'])
    features[period][p]['items_sum'] = data['ITEMS'].sum()
    features[period][p]['items_mean'] = data['ITEMS'].mean()

    if np.isnan(data['ITEMS'].std()):
      features[period][p]['items_std'] = 0
    else:
      features[period][p]['items_std'] = data['ITEMS'].std()
    
    features[period][p]['nic_sum'] = data['NIC'].sum()
    features[period][p]['nic_mean'] = data['NIC'].mean()
    if np.isnan(data['NIC'].std()):
      features[period][p]['nic_std'] = 0
    else:
      features[period][p]['nic_std'] = data['NIC'].std()  

    features[period][p]['act_sum'] = data['ACT COST'].sum()
    features[period][p]['act_mean'] = data['ACT COST'].mean()
    if np.isnan(data['ACT COST'].std()):
      features[period][p]['act_std'] = 0
    else:
      features[period][p]['act_std'] = data['ACT COST'].std()  
    
    act_nic = data['ACT COST'].values - data['NIC'].values
    features[period][p]['act_nic_sum'] = act_nic.sum()
    features[period][p]['act_nic_mean'] = act_nic.mean()
    if np.isnan(act_nic.std()):
      features[period][p]['act_nic_std'] = 0
    else:
      features[period][p]['act_nic_std'] = act_nic.std()  

    
    features[period][p]['qty_sum'] = data['QUANTITY'].sum()
    features[period][p]['qty_mean'] = data['QUANTITY'].mean()
    if np.isnan(data['QUANTITY'].std()):
      features[period][p]['qty_std'] = 0
    else:
      features[period][p]['qty_std'] = data['QUANTITY'].std() 
  file_out = open(os.path.splitext(f)[0] + ".pkl", 'w')
  pickle.dump(features, file_out)
  print "Time for file ", time.time() - t0, f

def combine_features(file_list):
  """ Combine montly features """
  practices = []
  for i, f in enumerate(file_list):
    f = open(os.path.splitext(f)[0] + ".pkl", 'r')
    if i == 0:
      features_raw = pickle.load(f)
    else:
      temp = pickle.load(f)
      period = temp.keys()[0]
      features_raw[period] = temp[period]  
    practices = set(practices + features_raw[period].keys())  
  # Find monthly sum, mean and std for all features
  keys = features_raw[period][features_raw[period].keys()[0]].keys()
  #practices = features_raw[period].keys()
  features = OrderedDict()
  for i_p, p in enumerate(practices):
    features[p] = OrderedDict()
    periods = [peri for peri in features_raw.keys() if p in features_raw[peri]]    
    for k in keys:
      features[p][k + '_MSUM'] = np.sum([features_raw[pp][p][k] for pp in periods])
      features[p][k + '_MMEAN'] = np.mean([features_raw[pp][p][k] for pp in periods])
      if np.isnan(np.std([features_raw[pp][p][k] for pp in periods])):
        features[p][k + '_MSTD'] = 0
      else:
        features[p][k + '_MSTD'] = np.std([features_raw[pp][p][k] for pp in periods])  
      features[p]['N_periods'] = len(periods)

    # Add practitioner to dataframe
    if p == practices[0]:
      features_np = features[p].values()
    else:
      features_np = np.vstack((features_np, features[p].values()))
  return features_np, features[p].keys()    
      

if __name__ == '__main__':
  file_list = glob.glob(directory + "*PDPI BNFT.[cC][sS][vV]")  
  jobs = []
  for f in file_list:
    p = multiprocessing.Process(target=make_features, args=(f,))
    jobs.append(p)
    p.start()
  for j in jobs:
    j.join()  
  features_np, labels = combine_features(file_list)
  features_all = pd.DataFrame(features_np, columns = labels)      
  features_all.to_csv('features_practice_test.csv', index=False) 

        
	
