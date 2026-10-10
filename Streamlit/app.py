import streamlit as st
import pandas as pd
st.title("Hello Streamlit")
st.write("This is my streamlit App")
st.header("welcome to streamlit")
st.subheader("This is a subheader")
st.text("This is plain text")
#buttons,checkboxes,and slideders
if st.button("Click"):
    st.write("Button clicked")

agree=st.checkbox("I agree")
if agree:
    st.write("You agreed!")

level=st.slider("Select a level :",1,10,5)
st.write(f"Selected level:{level}")


uploaded_file=st.file_uploader("Upload a File",type=["csv",'txt'])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head(5))
