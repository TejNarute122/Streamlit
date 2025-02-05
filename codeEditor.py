import streamlit as st 

#Diplaying s code like editor 
st.write("Python Code :")
code="""import pandas as pd
print("Hello word",)"""
st.code(code)