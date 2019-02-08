from oauth2client.service_account import ServiceAccountCredentials
import gspread

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES_WITH_WRITE_ENABLED = 'https://www.googleapis.com/auth/spreadsheets'

def get_gspread_service():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/usr/auth/file.txt', scope)

    return gspread.authorize(credentials)