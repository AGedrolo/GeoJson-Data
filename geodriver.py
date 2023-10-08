import geopandas as gpd
import geojson
import folium

# Load geospatial data
geo_data = gpd.read_file('suburb-10-vic.geojson')

m = folium.Map(location=[-37.8136, 144.9631], zoom_start=7)

folium.GeoJson(
    geo_data,
    name='postcode'
).add_to(m)
folium.features.GeoJson()
folium.LayerControl().add_to(m)
m.save('victoria_map.html')