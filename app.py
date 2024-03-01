import streamlit as st
import main
    
st.title("Case Vault")

# set Logging to DEBUG for more detailed outputs
query = st.text_input("Enter your query:")
if st.button("Search"):
    output=main.to_run(query)
    for i in output:
        for item in i:
        # If the current item is a list, traverse through it
            if isinstance(item, list):
                for element in item:
                    highlighted_element = element.replace(query, f"<span style='background-color: yellow; color: black'>{query}</span>")
                    st.write(highlighted_element, unsafe_allow_html=True)
                    # st.write(element)
            else:
                highlighted_item = item.replace(query, f"<span style='background-color: yellow; color: black'>{query}</span>")
                st.write("case: ", highlighted_item, unsafe_allow_html=True)
                # st.write("case: ",item)
