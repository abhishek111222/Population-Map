import folium
import extract_files
import color

html = """<h4>Volcano information:</h4>
Height: %s m
"""


map = folium.Map(location = [37.0902, 95.7129], zoom_start = 2, tiles = "Stamen Terrain")


fgv = folium.FeatureGroup(name = "Volcanoes")

for i,j,k in zip(extract_files.lat, extract_files.lon, extract_files.elev):
    iframe = folium.IFrame(html=html % str(k), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location = [i,j], popup = folium.Popup(iframe),radius = 3,  color = color.myFun(k), fill = True, fill_capacity = 3))



fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read(), style_function = lambda x : {"fillColor" : "yellow" if x["properties"]["POP2005"] < 100000000 else "black"}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")