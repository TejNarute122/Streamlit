import streamlit as st 

#Metric funtion diplay in positivly
st.metric(label="Weend ",value="120Ms",delta="10.2")

#Metric funtion diplay in nagativly
st.metric(label="Weend ",value="120Ms",delta="-10.2")