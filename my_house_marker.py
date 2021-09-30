import folium

map = folium.Map(location=[23.018729, 72.535957 )
fg=folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[23.018729, 72.535957], popup="your house", icon=folium.Icon(color="red")))
map.add_child(fg)
map.save("mymap.html")
