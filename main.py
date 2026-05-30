import streamlit as st
from functions import converter, len_finder


st.title("Doc-To-Text Converter")

user_file = st.file_uploader("Upload your file here - ")

if user_file:
    limit = len_finder(user_file)

    #Setting up slider values
    targets = st.slider("Till which page would you like to convert - ", 0, limit, (0, 0))
    start = targets[0]
    end = targets[1]

    if targets:
        result = converter(user_file, targets)

        #Expandable displayer
        for i in range(len(result)):
            with st.expander(f"Page {start+i} :"):
                st.text("\n\n".join(result[i]))