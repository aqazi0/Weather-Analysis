from cgi import print_environ_usage


def get_station(code):
    import os
    import pandas as pd
    data=pd.DataFrame({'Date [YYYY-MM]':[],'Temperature [°C]':[],'QCFLAG':[]})
    os.chdir('..')
    os.chdir('..')
    path=os.getcwd()
    out='data_qcf'
    path=os.path.join(path, out)
    os.chdir(path)
    station_data=pd.read_csv(code+'.csv')
    print(len(station_data))
    if(len(station_data)!=0 and int(station_data.iloc[0,0][0:4])<1950 and int(station_data.iloc[-1,0][0:4])>2000):
        for i in range(len(station_data)):
            if(int(station_data.iloc[i,0][0:4])<1950):
                continue
            elif(int(station_data.iloc[i,0][0:4])>2000):
                break
            else:
                data.loc[len(data.index)]=station_data.iloc[i,:]
    else:
        pass
    os.chdir('..')
    path=os.getcwd()
    out='Correlated Data/qcf50data'
    path=os.path.join(path, out)
    os.chdir(path)
    if(int(station_data.iloc[0,0][0:4])<1950 and int(station_data.iloc[-1,0][0:4])>2000):
        data.to_csv(code+'.csv')
    

import pandas as pd
import numpy as np
import os
stations=pd.read_csv('ghcnm_out\stations\stations_qcf.csv')
stations.reset_index(drop=True, inplace=True)
print(stations)
path=os.getcwd()
out='ghcnm_out/Correlated Data/50data'
path=os.path.join(path, out)
os.chdir(path)
for i in range(len(stations)):
    print(i)
    print(stations.iloc[i,0])
    get_station(stations.iloc[i,0])