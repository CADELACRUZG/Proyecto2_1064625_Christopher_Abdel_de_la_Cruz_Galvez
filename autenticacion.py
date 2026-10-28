import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/drive'
]

def conectar_drive():
    credenciales = None
    if os.path.exists('token.json'):
        credenciales = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not credenciales or not credenciales.valid:
        if (credenciales and credenciales.expired
            and credenciales.refresh_token):
            credenciales.refresh(Request())
        else:
            flujo = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credenciales = flujo.run_local_server(port=0)
        with open('token.json', 'w', encoding = 'utf-8') as archivo:
            archivo.write(credenciales.to_json())
    return build('drive', 'v3', credentials=credenciales)