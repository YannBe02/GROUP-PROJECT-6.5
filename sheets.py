import gspread #importation of gspread, which allows to link our database (in the creds.json document, which is linked to APIs) and our app.py document
from oauth2client.service_account import ServiceAccountCredentials #quite the same as abovementioned

def get_data_from_google_sheets(modules=None, number_of_members=None, credits=None, languages=None):    #implementation of a function, so that we can use it in the app.py document
#it allows literaly to link the database with the selection of the user on the website
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets" ,"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("Database").sheet1

    data = sheet.get_all_records()

    filtered_data = data #allows to filter the datas of the database with the selection of the website user

    if modules: #filter for the point of interests
        filtered_data = [record for record in filtered_data if record.get("POINT OF INTERESTS") in modules]

    if number_of_members:   #filter for the number of memebers 
        filtered_data = [record for record in filtered_data if record.get("NUMBER OF MEMBERS") ==  number_of_members]
    
    if credits: #filter for the accreditation
        filtered_data = [record for record in filtered_data if record.get("ACCREDITATION") == credits]      

    if languages: #filter for the languages 
        filtered_data = [record for record in filtered_data if record.get("LANGUAGE(S)") in languages]

    return filtered_data





        


    


