def get_station(code):
    import os
    import pandas as pd
    data=pd.DataFrame({'Date [YYYY-MM]':[],'Temperature [°C]':[],'QCFLAG':[]})
    os.chdir('..')
    os.chdir('..')
    path=os.getcwd()
    out='data'
    path=os.path.join(path, out)
    os.chdir(path)
    print(path)
    station_data=pd.read_csv(code)
    # print(station_data)
    for i in range(len(station_data)):
        if(int(station_data.iloc[i,0][0:4])<1950):
            continue
        elif(int(station_data.iloc[i,0][0:4])>2000):
            break
        else:   
            data.loc[len(data.index)]=station_data.iloc[i,:]
    print(data)
    os.chdir('..')
    path=os.getcwd()
    out='Correlated Data/good50data'
    path=os.path.join(path, out)
    os.chdir(path)
    data.to_csv(code)
    

import pandas as pd
import numpy as np
import os
stations=pd.read_csv('ghcnm_out\Time Series\Gooddata_Time_series.csv')
stations.reset_index(drop=True, inplace=True)
print(stations)
path=os.getcwd()
out='ghcnm_out/Correlated Data/good50data'
path=os.path.join(path, out)
os.chdir(path)
for i in range(len(stations)):
    print(stations.iloc[i,1])
    get_station(stations.iloc[i,1])