import streamlit as st



st.write(""" ## 10 Cool Beginner Python Tricks That Will Make Your Life Easier

 Simple but effective tips for every python lovers

""")

st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg" />
    </a>''',
    unsafe_allow_html=True
)

""" c1 = st.columns([8])
c1.caption("https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg") """

st.write("1. Walrus operator")

st.write("mylist = [1,2,3]")
st.write("if(l := len(mylist) > 2):")
st.write("print(l)")
st.write("Output")
st.write(3)


"""Nota solo streamlit no python

tutorial de python usando streamlit"""