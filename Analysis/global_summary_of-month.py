import os, pandas as pd
path=os.getcwd()
stations=pd.read_csv('ghcnm_out\stations\stations.csv')
out="ghcnm_out\min_max_data"
path=os.path.join(path,out)
os.chdir(path)
for code in stations['Code']:
    os.system('wget https://www.ncei.noaa.gov/data/global-summary-of-the-month/access/'+code+'.csv')