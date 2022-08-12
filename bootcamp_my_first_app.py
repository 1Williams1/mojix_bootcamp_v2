import streamlit as st

st.write("1. Walrus operator")

st.write("mylist = [1,2,3]")
st.write("if(l := len(mylist) > 2):")
st.write("print(l)")
st.write("Output")
mylist = [1,2,3]
if(l := len(mylist) > 2):
    st.write(l.toString())


