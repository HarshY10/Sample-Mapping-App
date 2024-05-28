import streamlit as st
import folium
from streamlit_folium import st_folium

#App Title
st.header(':blue[Address Mapping App] :world_map:', divider='rainbow')
st.write("A Demonstration app developed by Harsh Y for the CODE HR Summit.")
st.write("Click on the marker to view popup!")
def_loc = [12.9915, 80.2337] #default IIT Madras 12.9915° N, 80.2337° E
def_map = folium.Map(location = def_loc, zoom_start=20) 
#Setting the marker
#Using HTML Tags to enlarge text and the width of popup box to fit text
folium.Marker([12.9915, 80.2337], popup=folium.Popup("<h5>IIT Madras</h5>", max_width=200)).add_to(def_map) 
# Display the map
st_folium(def_map, width=1000)
