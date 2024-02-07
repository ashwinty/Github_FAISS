import streamlit as st
import main
    
st.title("Project Search Engine")

# set Logging to DEBUG for more detailed outputs
query = st.text_input("Enter your query:")
if st.button("Search"):
    output=main.to_run(query)
    st.write(output.response)
