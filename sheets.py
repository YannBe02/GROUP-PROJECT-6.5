import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def get_data_from_google_sheets(modules=None, number_of_members=None, credits=None):

    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets" ,"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("Database").sheet1

    data = sheet.get_all_records()

    filtered_data = data

    if modules:
        filtered_data = [record for record in filtered_data if record.get("POINT OF INTERESTS") in modules]
        
    if number_of_members:   
        filtered_data = [record for record in filtered_data if record.get("NUMBER OF MEMBERS") ==  number_of_members]
        
    if credits:
        filtered_data = [record for record in filtered_data if record.get("ACCREDITATION") == credits]   

    return filtered_data
        


    


