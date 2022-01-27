import pandas as pd
url="https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-summary-of-the-month&dataTypes=TMAX,TMIN&startDate=1899-01-01&endDate=2021-08-31&format=csv&stations="
station=pd.read_csv('ghcnm_out\stations\stations.csv')
for code in station['Code']:
    print(code)
    url=url+code+','
print(url)