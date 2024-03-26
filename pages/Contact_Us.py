import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv("topics.csv")

st.header("Contact US:")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address:")
    user_choice = st.selectbox('What topic do you want to discuss?',
                               df["topic"])
    user_message = st.text_area("Message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
Topic: {user_choice}
Message: {user_message}
"""
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully")