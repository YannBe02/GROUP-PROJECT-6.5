import streamlit as st #importation of streamlit to have an access to a localhost
import pandas as pd #importation of pandas
import numpy as np #importation of numpy
import sheets #importation of sheets to have a link with sheets.py and to have a working API
import plotly.graph_objects as go #import to have a gauge bar

from collections import Counter

st.set_page_config(page_title="HSG UNICLUBS", page_icon=":computer:") #Title appearing on the research bar of the research motor


st.title('''
         :red[WELCOME TO UNICLUBS]''')         #code to have a visible Title on the website
st.header("""
We designed this website to help you finding the best club corresponding to your criteria         
""")         #explanation of the goal of the website so that the users can understand what is the aim of the website


st.subheader("Point of Interests")           #First selection for the user: one can choose what he is interested in between many point of interests
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
selected_modules = st.multiselect("Select the topics you're interested in:", modules)  #once the user selected what he is interested in, the website shows what has been selected thanks to this code
for module in selected_modules:
    st.write(f"📘 {module}")
    

st.subheader("Language(s)")         #Second selection for the user: one can change which language(s) he wishes to speak with the club
languages = [
    "German",
    "English",
    "French",
    "Italian",
    "Spanish",
    "Arabic",
    "Other",
]


selected_languages = st.multiselect("Select the language(s) you wish to speak in the club", languages) #this code shows what has been selected by the user
for language in selected_languages:
    st.write(f"You've selected {language}")


st.subheader("Number of Members") #Third selection for the user: one can choose how many members he wishes to have in his corresponding club
number_of_members = st.radio(
    "Select the number of members",
    ("11-30", "31-50", "51-100", "101 & more","No preference")
)
if number_of_members=="No preference":           #block of code to give different responses depending on the choice of the user concerning the number of members selected above
    number_of_members=None
    st.write(f"You don't have any preference for the amount of club members")
else:
    st.write(f"You've selected {number_of_members} members in the club!")


st.subheader("Accreditation")         #Fourth selection for the user: one can choose if he wishes to get credits when being in the board of the club
st.write("Do you wish to find a club who are giving credits for work?")
credits = st.radio(
    "Select:",
    ("Yes", "No", "No preference")
)

if credits=="No preference":  #block of code to give different responses depending on the choice of the user concerning the accreditation selected above
    credits=None
    st.write(f"You don't have any preference")
else:
    st.write(f"You've selected {credits}!")


c1, c2 =st.columns([3,1])                  #implementation of the search button to trigger the research and to position it on the right side of the page
with c1:
    st.write("")
with c2:
    search=st.button("Search") #create a search button to trigger the search

if search:
    st.subheader("Results after taking into account your selection")



data = sheets.get_data_from_google_sheets(selected_modules, number_of_members, credits, selected_languages)    #link with the database which is also connected to Google Drive and Google Sheets API
                  
#the following block of code allows to have a nice format of the responses given with the informations of the corresponding clubs according to the choices made by the user
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
    st.markdown(f"**Language(s):** {record['LANGUAGE(S)']}")



# Assume 'data' is a list of records from the database for a specific category
#Return the information of the selected club with a limit of 10 clubs
limit = 10

counter=0 #creation of a counter to limit the amount of findings to the 'limit', which is set at 10
if search: #only triggers the search if the search button is clicked
    for record in data:
        counter+=1
        format_database_record(record) #use of created formula to deploy the data in a visually nice way
        fig = go.Figure(go.Indicator(mode = "gauge+number",
        value = 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': 'Compatibility to criterias'},
        gauge = {
            'axis': {'range':[0, 100]},
            'bar': {'color':"#45d01b"},
            'steps' : [
                {'range':[0, 50], 'color':"gray"},
                {'range':[50, 100], 'color':"lightgray"}]}))
        st.plotly_chart(fig)
        st.write('Your search is 100% accurate')#Visualisation of accuracy of findings with a text and a bar
        st.markdown("---")  # Add a horizontal line between records to add readability

        if counter==limit:
            break 

    #Return information of similar demands if less than 5 clubs correspond to demand
    #For this part, I could have created a formula which would have made everything easier, but the idea only came up when I had finished coding

    if counter <limit:
        st.markdown("Sadly, there is no other club which fulfills all your criterias. However, you might be interested by these similar clubs: ") 
        st.markdown("---")  # Add a horizontal line between records
        data2=sheets.get_data_from_google_sheets(selected_modules, number_of_members, None, selected_languages)#same requests but no regards to accreditation
        
        datax2=data+data2 #all data 2 elements are already in data, but some more too, add them together and only select the ones which are unique
        club_countsx2 = Counter([club["NAME"] for club in datax2]) #to see which clubs are unique, count the amount of time a club appears in datax2
        unique_data_list = [club for club in datax2 if club_countsx2[club["NAME"]] == 1] #only select the unique clubs which appear only once in club_countsx2

        for record in unique_data_list:
            counter+=1 #increase the counter to approach limit
            format_database_record(record) #return the list of club infos
            fig = go.Figure(go.Indicator(mode = "gauge+number",
            value = 92,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': 'Compatibility to criterias'},
            gauge = {
            'axis': {'range':[0, 100]},
            'bar': {'color':'#8fb200'},
            'steps' : [
                {'range':[0, 50], 'color':"gray"},
                {'range':[50, 100], 'color':"lightgray"}]}))
            st.plotly_chart(fig)
            st.write('Search is 92% accurate, only the accreditation does not match')#Visualisation of accuracy of findings with a text and a bar
            st.markdown("---")  # Add a horizontal line between records
            if counter==limit: #if counter is at limit, no more iteration shall be made
                break

    if counter<limit: #if the counter still has not attained the limit, go on with a broader search
        data3=sheets.get_data_from_google_sheets(selected_modules, None, None, selected_languages) #same requests but no regards to members and accreditation
        datax3=data2+data3
        club_countsx3= Counter([club["NAME"] for club in datax3])
        uniquex3=[club for club in datax3 if club_countsx3[club["NAME"]] == 1]
        for record in uniquex3:
            counter+=1
            format_database_record(record) #return the list of club infos
            fig = go.Figure(go.Indicator(mode = "gauge+number",
            value = 78,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': 'Compatibility to criterias'},
            gauge = {
            'axis': {'range':[0, 100]},
            'bar': {'color':'#ba8f00'},
            'steps' : [
                {'range':[0, 50], 'color':"gray"},
                {'range':[50, 100], 'color':"lightgray"}]}))
            st.plotly_chart(fig)
            st.write('Search is 78% accurate, the accreditation and the number of participants do not match')#Visualisation of accuracy of findings with a text and a bar
            st.markdown("---")  # Add a horizontal line between records
            if counter==limit:
                break

    if counter<limit: #if the counter still has not attained the limit, go on with a broader search
        data4=sheets.get_data_from_google_sheets(selected_modules, number_of_members, None, None)#request with no preference for credits and languages, but request for number of members
        datax4=data2+data3+data4
        club_countsx4= Counter([club["NAME"] for club in datax4])
        uniquex4=[club for club in datax4 if club_countsx4[club["NAME"]] == 1]
        for record in uniquex4:
            counter+=1
            format_database_record(record) #return the list of club infos
            fig = go.Figure(go.Indicator(mode = "gauge+number",
            value = 63,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': 'Compatibility to criterias'},
            gauge = {
            'axis': {'range':[0, 100]},
            'bar': {'color':'#ba8f00'},
            'steps' : [
                {'range':[0, 50], 'color':"gray"},
                {'range':[50, 100], 'color':"lightgray"}]}))
            st.plotly_chart(fig)
            st.write('Search is 63% accurate, the accreditation and the language requested do not match')#Visualisation of accuracy of findings with a text and a bar
            st.markdown("---")  # Add a horizontal line between records
            if counter==limit:
                break

    if counter<limit: #if the counter still has not attained the limit, go on with a broader search
        data5=sheets.get_data_from_google_sheets(selected_modules, None, None, None) #request with no preferences for credits, languages and number of members, last research, after that no more answers
        datax5=datax4+data5
        club_countsx5= Counter([club["NAME"] for club in datax5])
        uniquex5=[club for club in datax5 if club_countsx5[club["NAME"]] == 1]
        for record in uniquex5:
            counter+=1
            format_database_record(record)#return the list of club infos
            fig = go.Figure(go.Indicator(mode = "gauge+number",
            value = 50,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': 'Compatibility to criterias'},
            gauge = {
            'axis': {'range':[0, 100]},
            'bar': {'color':'#e51f1f'},
            'steps' : [
                {'range':[0, 50], 'color':"gray"},
                {'range':[50, 100], 'color':"lightgray"}]}))
            st.plotly_chart(fig)
            st.write('Search is 50% accurate, only the point of interest is matching') #Visualisation of accuracy of findings with a text and a bar
            st.markdown("---")  # Add a horizontal line between records
            if counter==limit:
                break

    if counter<limit: #return a text if no more club more or less fulfils your criterias, this should not be possible in theory if limit is set at 5
        st.write("There is no other club which more or less fulfils your criterias")


st.markdown("---")  # Add a horizontal line between records
st.subheader("Who are we?") #adding of a button to get information on the team which created this website
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
    
# if st.button("Easter Egg"):
#     limit=st.slider("Slide to the amount of clubs you want to see, feature only for Lea and Shasha",0,150)
