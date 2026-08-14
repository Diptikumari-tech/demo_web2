import streamlit as st
import pandas as pd
st.title("Welcome to streamlit")
# dataset = pd.read_csv("starbucks.csv")
# st.dataframe(dataset)

name = st.text_input("Enter your name ")
fname = st.text_input("Enter your father name ")
adr = st.text_area("Enter your text")
classdata = st.selectbox("Enter your class:",(1,2,3,4,5,6,7))

button = st.button("Done")
if button:
    st.markdown(f"""
                name : {name}
                father name : {fname}
                address: {adr}
                class : {classdata}
                """)