import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
name = list(data["NAME"])
kind = list(data["TYPE"])
elev = list(data["ELEV"])

# Function to change color markers depending on elevation
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

def map_color(country):
    if country["properties"]["POP2005"] < 10000000:
        return "green"
    elif 10000000 <= country["properties"]["POP2005"] < 20000000:
        return "orange"
    else:
        return "red"

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
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = folium.Popup(iframe), fill_color = color_producer(el), color = "grey", fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor": map_color(x)}))

map.add_child(fg)
map.save("Map1.html")
