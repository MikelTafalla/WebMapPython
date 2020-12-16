import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
name = list(data["NAME"])
kind = list(data["TYPE"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
# For loop to create multiple markers in the map
for lt, ln, nm, kd, el in zip(lat, lon, name, kind, elev):
    html= f"""
        <h4>Volcano {nm}</h4><br>
        Type: {kd} <br>
        Height: {str(el)}m
        """
    iframe = folium.IFrame(html = html, width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
