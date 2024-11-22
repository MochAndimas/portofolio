import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, subject, message):
    sender_email = st.secrets["CREDS"]["EMAIL"]
    sender_password = st.secrets["CREDS"]["PASSWORD"]

    # Setting up the MIME
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = "mochamad_andimas@yahoo.com"
    msg["Subject"] = f"{email} - {subject}"
    msg.attach(MIMEText(message, "plain"))

    try:
        # Connect to Gmail SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"