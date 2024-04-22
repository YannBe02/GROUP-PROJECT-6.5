import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="UNICLUBS", page_icon=":computer:")

st.title("WELCOME TO UNICLUBS")
st.write("""
We designed this website to help you find the best club corresponding to your criteria
""")

st.subheader("Point of interests")
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

selected_languages = st.multiselect("Select the language(s) you wish to speak", languages)
for language in selected_languages:
    st.write(f"You've selected {language}")

st.subheader("Other languages")
other_language = st.text_input("If you did not find the desired languages, which ones do you wish?", placeholder="Type the language(s)...")
if other_language != "":
    st.write(f"You are looking for a club speaking {other_language}! We are looking forward to help you finiding your dreamed club!")

st.subheader("How big should be the club?")
number_of_members = st.radio(
    "Select the number of members",
    ("1", "10", "50", "100", "200", "300+")
) #could even use a slider

    
if {number_of_members} == {"1"}:
    st.write(f"You've selected {number_of_members} member in the club!")
else:
    st.write(f"You've selected {number_of_members} members in the club!") #why the if condition? for the "s" if the mf choose 1 member lol

st.subheader("Who are we?")
if st.button("Us"):
    st.write("We are Group 6.5!")
    st.write("""
             We are a team of 5 students at the University of St. Gallen who decided to create a website to easily find a club when you don't know what to do out 
             out of the University!
             Shania Metrailler, 
             Léa Hurther,
             Frédéric De Buys,
             Sascha Huber,
             Edouard Vouillamoz,
             Yann Bernasconi             
             
             """)
    

