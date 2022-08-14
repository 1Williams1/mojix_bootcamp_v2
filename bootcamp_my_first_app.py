import streamlit as st



st.write(""" # 10 Cool Beginner Python Tricks That Will Make Your Life Easier

 Simple but effective tips for every python lovers

""")

st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg" />
    </a>''',
    unsafe_allow_html=True
)

st.write("""
The compactness of Python can make a developer’s life a lot easier when writing
lines and lines of code. But there are some lesser-known Python tricks that can 
surprise you with their amazing capabilities.

In today’s article, I will discuss 10 Python tips and tricks that will be really
helpful for beginners to write more compact code. Knowing these tips and tricks 
will definitely save you some valuable time.
""")

st.write(" ## 1. Walrus operator")

st.markdown("""<h3>Example </h3>
If we want to check and print the length of a list:""",unsafe_allow_html=True)

code = '''mylist = [1,2,3]
if(l := len(mylist) > 2):
    print(l)'''
st.code(code, language='python')

st.markdown("Output",unsafe_allow_html=True)
st.code("3")

st.write(""" ## 2. Splitting a string
If you want to split the components of a string into a list you can do that easily
using the split() function in python. This will make the string operations a lot easier!
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''string = “hello world”
string.split()'''
st.code(code, language='python')
st.markdown("""Output""",unsafe_allow_html=True)
st.code("[‘hello’, ‘world’]")