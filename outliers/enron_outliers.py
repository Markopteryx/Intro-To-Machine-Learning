#!/usr/bin/python


import matplotlib.pyplot as plt
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

plt.scatter(data[:,0], data[:,1])
plt.xlabel("salary")
plt.ylabel("bonus")

import pandas as pd
df = pd.DataFrame(data_dict)
df.loc['salary',:] = pd.to_numeric(df.loc['salary',:], errors='coerce')
df.loc['bonus',:] = pd.to_numeric(df.loc['bonus',:], errors='coerce')

print df.loc['salary',:].idxmax(axis=1)

print [name for name in df.columns if df.loc['salary', name] > 10**6 and df.loc['bonus',name] > 5*10**6]
