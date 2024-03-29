import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("SF on Folium map")
trees_df = pd.read_csv("trees.csv")
trees_df = trees_df.dropna(subset=["latitude", "longitude"])
trees_df = trees_df.head(n=100)
lat_avg = trees_df["latitude"].mean()
lon_avg = trees_df["longitude"].mean()
m = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)
for _, row in trees_df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
               
    ).add_to(m)
events = st_folium(m)
st.write(events)

