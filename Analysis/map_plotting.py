# import matplotlib
# from shapely.geometry import Point, Polygon
# import geopandas as gpd
import matplotlib.pyplot as plt
# from mpl_toolkits import basemap


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
geo_df=pd.read_csv('ghcnm_out/Correlated Data/Monthly_Correlated_Data.csv')
# print(geo_df)
geometry=[Point(xy) for xy in zip(geo_df['Longitude'], geo_df['Latitude'])]
print(geometry)