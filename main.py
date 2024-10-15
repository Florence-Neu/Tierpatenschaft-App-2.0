import osmnx as ox
import geopandas as gpd

# Funktion zum Abrufen der Stadtteile und deren Mittelpunkte
def get_stadtteile_und_zentren(stadt_name):
    # Abrufen der Stadtteile als Polygone
    tags = {"place": "neighbourhood"}
    gdf = ox.geometries_from_place(stadt_name, tags=tags)

    # Berechnen der Mittelpunkte der Polygone
    gdf['centroid'] = gdf.geometry.centroid

    # Extrahieren der Koordinaten der Mittelpunkte
    gdf['latitude'] = gdf['centroid'].y
    gdf['longitude'] = gdf['centroid'].x

    # Rückgabe von Stadtteilnamen und deren Koordinaten
    return gdf[['name', 'latitude', 'longitude']]

if __name__ == "__main__":
    stadt_name = "Karlsruhe, Germany"  # Name der Stadt
    stadtteile_und_zentren = get_stadtteile_und_zentren(stadt_name)

    # Ausgabe der Koordinaten
    print(stadtteile_und_zentren)