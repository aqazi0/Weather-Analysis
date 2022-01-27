import pandas as pd
import numpy as np
import os
stations=pd.read_csv('ghcnm_out\Correlated Data\Monthly_Correlated_Data.csv')
stations_time=pd.read_csv('ghcnm_out\Time Series\Time_series.csv')
stations['Time']=stations_time['Time']
stations['Time Range']=stations_time['Time Range']
stations.reset_index(drop=True, inplace=True)
stations.to_csv('Monthly_Correlated_Data.csv')
print(stations)
station_data30=pd.DataFrame()
station_data50=pd.DataFrame()
path=os.getcwd()
out='ghcnm_out/Correlated Data'
path=os.path.join(path, out)
os.chdir(path)
for i in range(len(stations)):
    print (i)
    if(stations.iloc[i,19]=='1970-2020'):
        station_data1970 = station_data1970.append(stations.iloc[i,:])
    if (int((stations.iloc[i,18])[0:2]))>30:
        # os.chdir(os.path.dirname(os.getcwd()))
        station_data30 = station_data30.append(stations.iloc[i,:])
        # data=pd.read_csv('''data/'''+ stations.iloc[i,1] +'''.csv''')
        # path=os.getcwd()
        # out='30 years data'
        # path=os.path.join(path, out)
        # os.chdir(path)
        # data.to_csv(stations.iloc[i,1]+'.csv')
    if (int((stations.iloc[i,18])[0:2]))>50:
        # os.chdir(os.path.dirname(os.getcwd()))
        station_data50 = station_data50.append(stations.iloc[i,:])
        # data=pd.read_csv('''data/'''+ stations.iloc[i,1] +'''.csv''')
        # path=os.getcwd()
        # out='50 years data'
        # path=os.path.join(path, out)
        # os.chdir(path)
        # data.to_csv(stations.iloc[i,1]+'.csv')
# os.chdir(os.path.dirname(os.getcwd()))
# path=os.getcwd()
# out='50 years data'
# path=os.path.join(path, out)
# os.chdir(path)

station_data50.reset_index(drop=True, inplace=True)
station_data50.to_csv('Stations 50 year data.csv')

station_data1970.reset_index(drop=True, inplace=True)
station_data1970.to_csv('Stations data.csv')

# os.chdir(os.path.dirname(os.getcwd()))
# path=os.getcwd()
# out='30 years data'
# path=os.path.join(path, out)
# os.chdir(path)

station_data30.reset_index(drop=True, inplace=True)
station_data30.to_csv('Stations 30 year data.csv')