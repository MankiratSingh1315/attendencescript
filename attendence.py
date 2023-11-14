import gspread
from oauth2client.service_account import ServiceAccountCredentials

file_name = 'attendence.json'
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

sheet = client.open('attendence').sheet1 # google sheet name
python_sheet = sheet.get_all_records()

import pandas as pd
dataframe1 = pd.read_excel('atten.xlsx') # Excel file of attendence
for i in range(len(dataframe1)):
    for j in range(len(python_sheet)):
        if dataframe1['Names'][i] == python_sheet[j]['Name']:
            sheet.update_cell(j+2, 3, 'Present') # attendence marker
            break
        else:
            continue