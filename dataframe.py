import streamlit as st 
import pandas as pd

#Creating a dataframe which having the 2 column and 5  rows 

st.write("Creating a dataframe which having the 2 column and 5  rows and Printing the whole dataframe")
table = pd.DataFrame({"column No - 1":[1,2,3,4,5],"column No - 2":[2,3,4,6,7]})

#Printing the whole dataframe in table format on web
st.write(table)

#Printing the first 2 row/record of dataframe in table 
st.write("Printing the first 2 row/record of  dataframe")
st.write(table.head(2))

##Printing the last 2 row/record dataframe in table
st.write("Printing the last 2 row/record of  dataframe")
st.write(table.tail(2))

#Origianal table 
st.write("This is a origianl priniting of table above other are the orgianal dataframe format view")
st.table(table)
st.write("\n \n **Note:** All the opration performed on dataframe these also worked for the table function in streamlit, st.dataframe(table) and st.write(table) both are ok  ")

