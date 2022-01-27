def correlate(code):
    import pandas as pd
    data=pd.read_csv('ghcnm_out/Correlated Data/data/'+code+'.csv')
    mon1=[]
    mon2=[]
    mon3=[]
    mon4=[]
    mon5=[]
    mon6=[]
    mon7=[]
    mon8=[]
    mon9=[]
    mon10=[]
    mon11=[]
    mon12=[]
    years=[]
    for i in range(0,len(data)):
        mon=(data.iloc[i,1])[5:]
        if mon=='01':
            year=(data.iloc[i,1])[0:4]
            years.append(year)
            jan=data.iloc[i,2]
            mon1.append(jan)
        if mon=='02':
            feb=data.iloc[i,2]
            mon2.append(feb)
        if mon=='03':
            mar=data.iloc[i,2]
            mon3.append(mar)
        if mon=='04':
            apr=data.iloc[i,2]
            mon4.append(apr)
        if mon=='05':
            may=data.iloc[i,2]
            mon5.append(may)
        if mon=='06':
            june=data.iloc[i,2]
            mon6.append(june)
        if mon=='07':
            july=data.iloc[i,2]
            mon7.append(july)
        if mon=='08':
            aug=data.iloc[i,2]
            mon8.append(aug)
        if mon=='09':
            sep=data.iloc[i,2]
            mon9.append(sep)
        if mon=='10':
            oct=data.iloc[i,2]
            mon10.append(oct)
        if mon=='11':
            nov=data.iloc[i,2]
            mon11.append(nov)
        if mon=='12':
            dec=data.iloc[i,2]
            mon12.append(dec)
    monthly_data=pd.DataFrame({'year':years, 'Jan':mon1, 'Feb': mon2, 'Mar': mon3, 'April': mon4, 'May': mon5, 'June': mon6, 'July': mon7, 'Aug': mon8, 'Sep': mon9, 'Oct': mon10, 'Nov': mon11, 'Dec': mon12})
    monthly_data=monthly_data.set_index("year")
    data_corr=monthly_data.corr()
    return data_corr



if __name__ == "__main__":
    import pandas as pd, argparse, os
    parser=argparse.ArgumentParser()
    parser.add_argument("-c","--code",metavar="\b" ,type=str,help="Find correlation between temp of months using code", default='1' )
    parser.add_argument("-m","--month",metavar="\b" ,type=int,help="Find correlation between temp of months using code", default=1 )
    args=parser.parse_args()
    stations=pd.read_csv('ghcnm_out/Correlated Data/1950-2000.csv')

    k=0
    corrlist1=[]
    corrlist2=[]
    corrlist3=[]
    corrlist4=[]
    corrlist5=[]
    corrlist6=[]
    corrlist7=[]
    corrlist8=[]
    corrlist9=[]
    corrlist10=[]
    corrlist11=[]
    corrlist12=[]
    for i in range(len(stations)):
        scode=stations.iloc[i,1]
        if args.code=='1':
            print(i)
            data_corr=correlate(scode)
            corrlist1.append(data_corr.iloc[0,1])
            corrlist2.append(data_corr.iloc[1,2])
            corrlist3.append(data_corr.iloc[2,3])
            corrlist4.append(data_corr.iloc[3,4])
            corrlist5.append(data_corr.iloc[4,5])
            corrlist6.append(data_corr.iloc[5,6])
            corrlist7.append(data_corr.iloc[6,7])
            corrlist8.append(data_corr.iloc[7,8])
            corrlist9.append(data_corr.iloc[8,9])
            corrlist10.append(data_corr.iloc[9,10])
            corrlist11.append(data_corr.iloc[10,11])
            corrlist12.append(data_corr.iloc[11,0])
            k=1
        if args.code==scode:
            data_corr=correlate(args.code)
            k=1
    if k==0:
        print('No such station found')
    corr_series1=pd.Series(corrlist1,name='Correlation1')
    corr_series2=pd.Series(corrlist2,name='Correlation2')
    corr_series3=pd.Series(corrlist3,name='Correlation3')
    corr_series4=pd.Series(corrlist4,name='Correlation4')
    corr_series5=pd.Series(corrlist5,name='Correlation5')
    corr_series6=pd.Series(corrlist6,name='Correlation6')
    corr_series7=pd.Series(corrlist7,name='Correlation7')
    corr_series8=pd.Series(corrlist8,name='Correlation8')
    corr_series9=pd.Series(corrlist9,name='Correlation9')
    corr_series10=pd.Series(corrlist10,name='Correlation10')
    corr_series11=pd.Series(corrlist11,name='Correlation11')
    corr_series12=pd.Series(corrlist12,name='Correlation12')
    plotdf=(stations.join(corr_series1)).copy()
    plotdf=(plotdf.join(corr_series2)).copy()
    plotdf=(plotdf.join(corr_series3)).copy()
    plotdf=(plotdf.join(corr_series4)).copy()
    plotdf=(plotdf.join(corr_series5)).copy()
    plotdf=(plotdf.join(corr_series6)).copy()
    plotdf=(plotdf.join(corr_series7)).copy()
    plotdf=(plotdf.join(corr_series8)).copy()
    plotdf=(plotdf.join(corr_series9)).copy()
    plotdf=(plotdf.join(corr_series10)).copy()
    plotdf=(plotdf.join(corr_series11)).copy()
    plotdf=(plotdf.join(corr_series12)).copy()
    print(plotdf)
    path=os.getcwd()
    out="ghcnm_out\Correlated Data"
    path=os.path.join(path,out)
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    path=os.getcwd()
    plotdf.to_csv('50yrscorr.csv')