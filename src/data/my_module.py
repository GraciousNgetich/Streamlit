import geopandas as gp
import pandas as pd
import numpy as np
import folium as folium
import json as json
import boto3 as boto3
import branca.colormap as cm
from io import BytesIO


colormap = cm.linear.YlOrRd_09.scale(0, 100)

# Load the data GeoJSON fiber data


def style_function(feature):
    data_value = feature['properties']['devices']
    return {'fillColor': colormap(data_value)}


def highlight_boundary(feature):
    return {
        'fillColor': '#98abc5',
        'fillOpacity': 0.7,
        'color': '#000000',
        'weight': 1.5
    }
