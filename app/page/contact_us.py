import streamlit as st
from app.utils.functions import send_email


def contact_us_page():
    """
    """
    # Streamlit form to send email
    st.title("Contact Me")

    with st.form("email_form"):
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Email")

        if submitted:
            status = send_email(email, subject, message)
            st.success(status)