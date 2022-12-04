"""

Streamlit web app for electrification of maritime vessels hackathon project 

"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import plotly.graph_objects as go
import mpld3
import plotly.express as px


st.set_page_config(
    page_title="Marina Charging Station Calculator")

st.title("Marina Charging Station Calculator")


# Enter marina information 

st.header("**Marina Information**")
st.subheader("Boats")

col_motorboats, col_sailboats = st.columns(2)

with col_motorboats:
    num_motorboats = st.number_input("Enter the number of motorboats: ", min_value=0.0, format='%f')

with col_sailboats:
    num_sailboats = st.number_input("Enter the number of sailboats: ", min_value=0.0, format='%f')

# dictionary 

marina_dict = {
    'boat_type': ['motorboats', 'sailboats'], 
    'boat_count': [num_motorboats, num_sailboats]
    # 'boat_count': [num_motorboats, num_sailboats]
}
# save to a dataframe 

marina_df = pd.DataFrame(marina_dict)

# st.dataframe(marina_df)

# def convert_df(df):
#     return df.to_csv(index=False).encode('utf-8')
    
# csv = convert_df(marina_df)

# st.download_button("Press to Download", 
#                   csv, 
#                   "file.csv", 
#                   "text/csv",
#                   key='download-csv')
    
# Report marina information 

if num_motorboats or num_sailboats > 0:
    
    # define variables 
    total_boats = round(num_motorboats + num_sailboats, 0)
    percent_motorboats = round(num_motorboats/total_boats * 100, 0)
    percent_sailboats = round(num_sailboats/total_boats * 100, 0)
    
    # report results 
    st.subheader("You have " + str(total_boats) + " total boats in your marina")

    st.subheader("You have " + str(percent_motorboats) + "% motorboats and " + str(percent_sailboats) + "% sailboats in your marina.")
    
    # figure 
    
    fig = px.bar(marina_df, x='boat_type', y='boat_count', title='Bar Chart')
    
    st.plotly_chart(fig)
    
st.markdown("---")

