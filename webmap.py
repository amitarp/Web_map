
import folium
import pandas

data= pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation<1500:
        return "green"
    elif 1500<=elevation<3000:
        return "orange"
    else:
        return "red"


map1=folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))

fgp=folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save("map1.html")
