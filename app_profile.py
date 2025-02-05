import streamlit as st
import pandas as pd

# Title of the app
st.set_page_config(page_title="Researcher Profile and Publication Data Explorer", layout="wide")

left, right = st.columns(2, border=True)

left.image("https://raw.githubusercontent.com/sophakama2025/my_profile/refs/heads/main/Sophakama_Zabo.jpg", width=200)
# Collect basic information
name = "Mr Sophakama Zabo"
field = "Bioinformatics"
institution = "Rhodes University"
# Display basic profile information

right.header("Researcher Overview")
right.write(f"**Name:** {name}")
right.write(f"**Field of Research:** {field}")
right.write(f"**Institution:** {institution}")

with st.container():
    tab1, tab2, tab3, tab4 = st.tabs(["Bio", "Publications", "Publication Trends", "Contact Details"])

    with tab1:
        st.header("Biography")
        st.write("I am alive until further notice...\n\n\n...and it's not that serious...\n\n\n...like at all!")
    with tab2:
        st.header("Publications")
        uploaded_file = "./publications.csv" #st.file_uploader("Upload a CSV of Publications", type="csv")
    
        if uploaded_file:
            publications = pd.read_csv(uploaded_file)
            st.dataframe(publications)
    
            # Add filtering for year or keyword
            keyword = st.text_input("Filter by keyword", "")
            if keyword:
                filtered = publications[
                    publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
                ]
                st.write(f"Filtered Results for '{keyword}':")
                st.dataframe(filtered)
            else:
                st.write("Showing all publications")
    
    with tab3:
        st.header("Publication Trends")
        if uploaded_file:
            publications = pd.read_csv(uploaded_file)
            if "Year" in publications.columns:
                year_counts = publications["Year"].value_counts().sort_index()
                st.bar_chart(year_counts)
            else:
                st.write("The CSV does not have a 'Year' column to visualize trends.")
    with tab4:
        st.header("Contact Information")
        email = "g15z3394@campus.ru.ac.za"
        st.write(f"You can reach {name} at {email}.")
        st.page_link("http://www.google.com", label="Google", icon="🌎")
    
        # Add a section for visualizing publication trends
       
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)


