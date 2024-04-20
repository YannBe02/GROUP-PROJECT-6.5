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
)
    
if {number_of_members} == {"1"}:
    st.write(f"You've selected {number_of_members} member in the club!")
else:
    st.write(f"You've selected {number_of_members} members in the club!")

st.subheader("Who are we?")
if st.button("Us"):
    st.write("We are Group 6.5!")
    st.write("""
             We are a team of 5 students at the University of St. Gallen who decided to create a website to easily find a club when you don't know what to do out 
             out of the University!
             """)
    
#It does not work as it should
st.subheader("How many people in common")
common = st.slider("Select", min_value=1.0, max_value=12.0, step=1.0, value=6.0)
st.write(f"You selected: {common}")

st.subheader("How many people in common")
x = np.linspace(1, 6, 100)

y = 1 / (1 * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - 3.5) / 1) ** 2)

df = pd.DataFrame({"Type of food": x, "Density": y})

fig, ax = plt.subplots(figsize=(8, 5))
ax.fill_between(df["Type of food"], df["Density"], color="green", label="How many people are also interested")
ax.axvline(common, color="red", linestyle="--", label=f"Your selection: {common}")
ax.legend(loc="upper left")
ax.set_xlabel("Type of food")
ax.set_ylabel("Density")
st.pyplot(fig)

def erf_approx(x):
    # Constants
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    sign = 1 if x >= 0 else -1
    x = abs(x)

    t = 1.0 / (1.0 + p * x)
    y = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t

    return sign * (1 - y * np.exp(-x * x))

mu = 6.0  # mean
sigma = 1.7  # standard deviation
percentile = 0.5 * (1 + erf_approx((common - mu) / (sigma * np.sqrt(2))))

st.write(f"With a selection of {common}, you're in the {percentile*100:.2f} percentile.")
