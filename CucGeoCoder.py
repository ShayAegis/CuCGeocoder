import geopandas as gpd
from shapely import Point
gdf=gpd.read_file('CucutaGDF.kml',driver="KML")
lat=input("Ingrese la Latitud: ")
long=input("Ingrese la Longitud: ")
point=gpd.GeoSeries([Point(long,lat)],crs="EPSG:4326")
if(gdf.intersects(point.iloc[0]).any()==True):
    intersects=gdf.intersects(point.iloc[0])
    index=list(intersects.loc[intersects==True].index)
    print(f"El barrio es: {gdf.iloc[index[0]].Name}")
else:
    print('El barrio no existe o no es de Cúcuta')