import streamlit as st
import requests
import uuid
from datetime import datetime

# Function to send data via webhook
def send_webhook(category, request):
    url = "https://www.x.com"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "1": "Internal Submission",
        "2": "GMG",
        "3": "clittle@garberauto.com",
        "4": category,
        "5": request,
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "id": f"I-{uuid.uuid4()}",
        "form_id": "33",
        "post_id": None,
        "date_created": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    response = requests.post(url, json=data, headers=headers)
    return response

# Streamlit user interface
st.title('Webhook Sender')

category = st.text_input("Category", value="")
request = st.text_area("Request", value="")

if st.button('Send Webhook'):
    result = send_webhook(category, request)
    if result.ok:
        st.success("Webhook sent successfully!")
    else:
        st.error("Failed to send webhook")

