import folium
from folium.map import LayerControl
import pandas


GreekMap = folium.Map( location = [38 , 23] , zoom_start= 8)

data = pandas.read_csv("EarthquakesGR.csv")


lat=list(data['LATATITUDE (N)'])
lon= list(data['LONGITUDE  (E)'])
MAG = list(data['MAGNITUDE (Richter)'])
Date = list(data['Year'])

def Color(richter):

    if richter <= 6.5:
        return 'green'
    elif richter < 7:
        return 'orange'
    elif richter >= 7:
        return 'red'


Markers = folium.FeatureGroup(name = 'Earthquakes')

for lt,ln,MMAG,Year  in zip(lat,lon,MAG,Date):
    
    if MMAG > 6 :

        Markers.add_child(folium.Marker( location= [lt,ln], radius = 6, popup= str(Year)  + ' %sR' %str(MMAG), icon=folium.Icon(color=Color(MMAG))))
        
CustomBorders = folium.FeatureGroup(name = 'Borders')   

CustomBorders.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000 else 'orange'  if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))    


GreekMap.add_child(Markers)
GreekMap.add_child(CustomBorders)
GreekMap.add_child(folium.LayerControl())

GreekMap.save('GreeceMap.html')