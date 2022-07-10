from asyncore import write
from calendar import calendar
import imp
from multiprocessing import context
from pickle import NONE
from django.shortcuts import redirect, render
from django.http import HttpResponse
import os.path
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


SCOPES = ["https://www.googleapis.com/auth/calendar.acls.readonly", "https://www.googleapis.com/auth/calendar.events.readonly"]

def landing(request):
    return render(request, 'home.html')

def getCreds(request):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        service = build('calendar', 'v3', credentials=creds)
        events = service.events().list(calendarId = 'primary').execute()
        context = {
            'events' : events,
        }
        return render(request, "ListEvents.html", context)

