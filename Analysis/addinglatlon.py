import pandas as pd
import numpy as np
import os
stations1=pd.read_csv('ghcnm_out\Correlated Data\\50yrscorr.csv')
stations=pd.read_csv('ghcnm_out\Correlated Data\qcfgooddatacorr.csv')
lat=[]
lon=[]
stations.reset_index(drop=True, inplace=True)
path=os.getcwd()
out='ghcnm_out/Correlated Data/'
path=os.path.join(path, out)
os.chdir(path)
for i in  range(len(stations)):
    print(i)
    for j in range(len(stations1)):
        if(stations1.iloc[j,1]==stations.iloc[i,1][0:11]):
            lat.append(stations1.iloc[j,3])
            lon.append(stations1.iloc[j,4])
            # print(lat)
            break
latitude=pd.Series(lat,name='latitude')
longitude=pd.Series(lon,name='longitude')
adddf=(stations.join(latitude)).copy()
adddf=(adddf.join(longitude)).copy()
print(adddf)
adddf.to_csv('qcf_good_final_data.csv')