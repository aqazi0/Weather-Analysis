if __name__ == "__main__":
    import pandas as pd, os
    stations=pd.read_csv('ghcnm_out\stations\stations.csv')
    k=0
    yearrange=[]
    years=[]
    for i in range(len(stations)):    
        scode=stations.iloc[i,0]
        print(i)
        data=pd.read_csv('ghcnm_out/data/'+scode+'.csv')
        startyear=data.iloc[0,0][:4]
        endyear=data.iloc[-1,0][:4]
        yearrange.append(startyear+"-"+endyear)
        years.append(str(int(endyear)-int(startyear))+' years')
    range_series=pd.Series(yearrange,name='Time Range')
    year_series=pd.Series(years,name='Time')
    timedf=(stations.join(range_series)).copy()
    timedf=(timedf.join(year_series)).copy()
    print(timedf)
    path=os.getcwd()
    out="ghcnm_out\Time Series"
    path=os.path.join(path,out)
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    path=os.getcwd()
    timedf.to_csv('Time_series.csv')