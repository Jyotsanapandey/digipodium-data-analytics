import streamlit as st
from random import choice

st.title('Name generator')

fnames = ['Alex', 'Bob', 'Charlie', 'David', 'Eve']

lnames = ['Anderson', 'Baker', 'Clark']

btn = st.button('random name generator')
if btn:
    fn = choice(fnames)
    ln = choice(lnames)
    fullname = f'{fn} {ln}'
    st.success(fullname)

# streamlit run ui/app1.py     (write this in terminal then we get our browser open)
# control+c ya del se delete ho sakta h

