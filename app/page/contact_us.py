import streamlit as st
from app.utils.functions import send_email


def contact_us_page():
    """
    """
    # Streamlit form to send email
    st.title("Contact Me")

    # Variables to hold form inputs
    email = ""
    subject = ""
    message = ""

    with st.form("email_form"):
        # Input fields
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        
        # Submit button
        submitted = st.form_submit_button("Send Email")

    # Validation after submission
    if submitted:
        if not email.strip():
            st.error("Email is required.")
        elif not subject.strip():
            st.error("Subject is required.")
        elif not message.strip():
            st.error("Message is required.")
        else:
            # Call the email sending function if all fields are valid
            status = send_email(email, subject, message)
            st.success(status)