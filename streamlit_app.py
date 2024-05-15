import streamlit as st

st.title('This is :green[My Assignment]')
st.title(':red[_Streamlit_] is :blue[cool] :sunglasses:')

number = st.number_input("Insert a number")
st.write("The current number is ", number)

st.write("The answer of mutiple '7' is ",7*number)
