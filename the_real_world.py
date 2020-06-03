import folium


map = folium.Map(location=[51, 71.4321], zoom_start=10)

folium.Marker(location=[51.12321, 71.4121], popup='The real world',
              icon=folium.Icon(color='gray')).add_to(map)


[folium.Marker(location=coordinates, icon=folium.Icon(color='green')).add_to(
    map) for coordinates in [[51.12321, 71.4121], [51.15321, 71.5121]]]


map.save('map1.html')
