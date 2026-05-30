import streamlit as st
from functions import converter, len_finder


st.title("Doc-To-Text Converter")

user_file = st.file_uploader("Upload your file here - ")

if user_file:
    limit = len_finder(user_file)

    #Setting slider max value
    target = st.slider("Till which page would you like to convert - ", 0, limit)

    if target:
        result = converter(user_file, target)

        #Expandable displayer
        for i in range(len(result)):
            with st.expander(f"Page {i+1} :"):
                st.info("\n\n".join(result[i]))