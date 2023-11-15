import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

file_name = 'attendence.json'
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

sheet = client.open('attendence').sheet1 # google sheet name
python_sheet = sheet.get_all_records()

df_main = pd.DataFrame(python_sheet)
date = pd.to_datetime("today").strftime("%m/%d/%Y")
df = pd.read_excel('atten.xlsx') # Excel file of attendence
df[date] = 'Present'

df_main.merge(df,how = 'left',on = 'Name')

