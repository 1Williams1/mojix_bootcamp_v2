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

st.markdown("<strong>Output</strong>",unsafe_allow_html=True)
st.code("3")

st.write(""" ## 2. Splitting a string
If you want to split the components of a string into a list you can do that easily
using the split() function in python. This will make the string operations a lot easier!
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''string = “hello world”
string.split()'''
st.code(code, language='python')
st.markdown("""<strong>Output</strong>""",unsafe_allow_html=True)
st.code("[‘hello’, ‘world’]")

st.write(""" ## 3. Reversing a string
If you want to reverse a given string, you can do that with only one line of code using
the negative indexing of the string.
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''str=”hello world!”
a=str[::-1]
print(a)'''
st.code(code, language='python')
st.markdown("""<strong>Output</strong>""",unsafe_allow_html=True)
st.code("!dlrow olleh")

st.write(""" ## 4. Merging two dictionaries
This amazing trick will help you merge two dictionaries with just 1 line of code.
We just need to use ** in front of the name of the two dictionaries like below two merge 
them into a single dictionary:
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
st.code(code, language='python')
st.markdown("""<strong>Output</strong>""",unsafe_allow_html=True)
st.code("{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}")

st.write(""" ## 5. The zip() function
The zip() function in python can make your life a lot easier when working with lists and
dictionaries. It is used to combine several lists of the same length.
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
st.code(code, language='python')
st.markdown("""<strong>Output</strong>""",unsafe_allow_html=True)
st.code("""red apple
yellow banana
green mango""")
st.write("""
The zip() function can also be used for combining two lists into a dictionary. This method
can be really helpful while grouping data from the list.
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''
st.code(code, language='python')
st.markdown("""<strong>Output</strong>""",unsafe_allow_html=True)
st.code("""{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}""")

st.write(""" ## 6. Assigning multiple list values to a variable
If you want to assign some specific values of a list to a variable and all the remaining
values to another variable in a list format, you can use the following technique:
""")
st.markdown(""" <h3>Example </h3>""",unsafe_allow_html=True)
code = '''mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)'''
st.code(code, language='python')
st.markdown("""<strong>Output</strong>""",unsafe_allow_html=True)
st.code("""a = 1
b = [2, 3, 4, 5]""")
st.write("""
This process is also called list unpacking and you can apply this method for more than 
2 variables also!""")