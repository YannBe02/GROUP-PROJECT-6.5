import streamlit as st 
import pandas as pd
import numpy as np
import sheets

st.set_page_config(page_title="HSG UNICLUBS", page_icon=":computer:")



st.title('''
         :red[WELCOME TO UNICLUBS]''')
st.header("""
We designed this website to help you finding the best club corresponding to your criteria
""")


st.subheader("Point of Interests")   
modules = [
    "AV",
    "Networking and Think Tanks",
    "Culture and Interests",
    "Sports",
    "Business and Investments",
    "International Networks",
    "Social and Political Engagement",
    "Student Union",
    "Cantons",
    "Industry Focus",
]
selected_modules = st.multiselect("Select the topics you're interested in:", modules)
for module in selected_modules:
    st.write(f"📘 {module}")
    

st.subheader("Language(s)")
languages = [
    "English",
    "German",
    "French",
    "Spanish",
    "Italian",
    "Chinese",
    "Portuguese",
    "Arabic",
]

selected_languages = st.multiselect("Select the language(s) you wish to speak in the club", languages)
for language in selected_languages:
    st.write(f"You've selected {language}")

st.subheader("Number of Members")
number_of_members = st.radio(
    "Select the number of members",
    ("11-30", "31-50", "51-100", "101 & more")
)
st.write(f"You've selected {number_of_members} members in the club!")


st.subheader("Accreditation")
st.write("Do you wish to find a club who are giving credit for work?")
credits = st.radio(
    "Select:",
    ("Yes", "No")
)
st.write(f"You've selected {credits}!")

data = sheets.get_data_from_google_sheets(selected_modules, number_of_members, credits)



def format_database_record(record):
    st.markdown(f"**Name:** {record['NAME']}")
    st.markdown(f"**Description:** {record['DESCRIPTION']}")
    st.markdown(f"**Category:** {record['CATEGORY']}")
    st.markdown(f"**Instagram:** [{record['INSTAGRAM']}]({record['INSTAGRAM']})")
    st.markdown(f"**Facebook:** [{record['FACEBOOK']}]({record['FACEBOOK']})")
    st.markdown(f"**LinkedIn:** [{record['LINKEDIN']}]({record['LINKEDIN']})")
    st.markdown(f"**Website:** [{record['WEBSITE']}]({record['WEBSITE']})")
    st.markdown(f"**Email:** {record['EMAIL']}")
    st.markdown(f"**Is Recruiting:** {record['IS RECRUITING']}")
    st.markdown(f"**Number of Members:** {record['NUMBER OF MEMBERS']}")
    st.markdown(f"**Accreditation:** {record['ACCREDITATION']}")
    st.markdown(f"**Point of Interests:** {record['POINT OF INTERESTS']}")
    st.markdown(f"**Languages:** {record['LANGUAGE(S)']}")

    st.markdown("---")  # Add a horizontal line between records

# Assume 'data' is a list of records from the database for a specific category
for record in data:
    format_database_record(record)







st.subheader("Who are we?")
if st.button("Team"):
    st.write("We are Group 6.5!")
    st.write("""
             We are a team of 5 students at the University of St. Gallen who decided to create a website to easily find a club when you don't know what to do out 
             out of the University!
             Shania Metrailler,
             Léa Hurther,
             Frédéric de Buys,
             Sascha Huber,
             Edouard Vouillamoz,
             Yann Bernasconi
            
             """)
    

