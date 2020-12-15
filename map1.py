import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
name = list(data["NAME"])
kind = list(data["TYPE"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
# For loop to create multiple markers in the map
for lt, ln, nm, kd in zip(lat, lon, name, kind):
    fg.add_child(folium.Marker(location=[lt, ln], popup=f"Name: {nm}; Type: {kd}", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
