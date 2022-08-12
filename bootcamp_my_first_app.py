import streamlit as st

st.write("1. Walrus operator")

mylist = [1,2,3]
if(l := len(mylist) > 2):
    print(l)

