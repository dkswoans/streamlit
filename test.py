import firebase_admin
from firebase_admin import credentials

from firebase_admin import db
import streamlit as st
import json
# Fetch the service account key JSON file contents
key_dict = json.loads(st.secrets["textkey"])
cred = credentials.Certificate(key_dict)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://drfs-5b213-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('TEST')
print(ref.get())
ref.set({"py":"ㅇ"})