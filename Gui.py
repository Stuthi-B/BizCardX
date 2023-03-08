import streamlit as st
import Backend as b

def handleClick():
    b.extractData(file)


file = st.file_uploader("Upload visiting card", accept_multiple_files=True)
st.button("Upload", key=None, help="Click to upload and extract information", on_click=handleClick, type="primary")


