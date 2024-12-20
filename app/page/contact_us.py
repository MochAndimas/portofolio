import streamlit as st
from app.utils.functions import send_email


def contact_us_page():
    """
    """
    # Streamlit form to send email
    st.title("Contact Me")

    with st.form("email_form"):
        # Input fields
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")

        # Check if all fields are filled
        all_fields_filled = bool(email.strip()) and bool(subject.strip()) and bool(message.strip())

        # Submit button, enabled only if all fields are filled
        submitted = st.form_submit_button("Send Email", disabled=not all_fields_filled)

        if submitted:
            # Call the email sending function
            status = send_email(email, subject, message)
            st.success(status)