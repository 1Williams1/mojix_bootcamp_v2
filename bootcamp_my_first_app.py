import streamlit as st

import Image

myImage = Image.open("https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg");
myImage.show();

st.write("1. Walrus operator")

st.write("mylist = [1,2,3]")
st.write("if(l := len(mylist) > 2):")
st.write("print(l)")
st.write("Output")
st.write(3)


