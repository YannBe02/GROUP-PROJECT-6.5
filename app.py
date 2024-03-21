import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="GROUP 6.5", page_icon=":computer:")

st.title("WELCOME TO GROUP 6.5")
st.write("""
Here is the place where we will develop our website for the Computer Science Project
""")

st.subheader("Who are we?")
if st.button("Us"):
    st.write("We are Group 6.5!")
    st.write("""
             We are a team of 5 students at the University of St. Gallen who decided te create a develop to easily find a restaurant when you don't know what and where to eat!
             """)

st.subheader("Type of Food")
food = st.text_input("Enter the type of food you want to enjoy", placeholder="Your food here...")
if food != "":
    st.write(f"You want to eat {food}! Thank you for choosing our website, we will help you to find your desired food!")

st.subheader("Location")
location = st.text_input("Where do you want to eat?", placeholder="Where you want to eat...")
if location != "":
    st.write(f"You are looking to eat in {location}! We are finding your food!")

st.subheader("Who is eating?")
number_of_people = st.radio(
    "Select the number of people",
    ("1", "2", "3", "4", "5+")
)
if {number_of_people} == {"1"}:
    st.write(f"You've selected {number_of_people} person is eating!")
else:
    st.write(f"You've selected {number_of_people} people are eating!")


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
