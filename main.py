import streamlit as st
# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="My Portfolio",
    layout="centered",  # Optional: Use "wide" for full-width layout
    initial_sidebar_state="expanded", # Start with the sidebar opened 
)
from app.page import home, certification, contact_us, projects_1, projects_2

# --- Initialize session state ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# -- Pages -- 
page_home = st.Page(page=home, title="About Me", url_path="/home")
page_certification = st.Page(page=certification, title="Certification", url_path="/certification")
page_contact_us = st.Page(page=contact_us, title="Contact Me", url_path="/contact-us")
page_project_1 = st.Page(page=projects_1, title="Dashboard Reporting", url_path="/dashboard-reporting")
page_project_2 = st.Page(page=projects_2, title="Fast API", url_path="/fast-api")

# -- Menu Options -- 
menu_options = {
    "Info": [page_home, page_certification, page_contact_us],
    "Projetcs": [page_project_1, page_project_2]
}

# -- Navigation --
with st.sidebar:
    page = st.navigation(
        menu_options,
        position="sidebar"
    )

# -- Page content -- 
try:
    page_handlres = {
        page_home: lambda: home.home_page(),
        page_certification: lambda: certification.certification_page(),
        page_contact_us: lambda: contact_us.contact_us_page(),
        page_project_1: lambda: projects_1.project_1_page(),
        page_project_2: lambda: projects_2.project_2_page()
    }
    if page in page_handlres:
        page_handlres[page]()
        st.session_state.page = page.url_path

except ZeroDivisionError as e:
    st.error(f"Something error! Please Try Again!")
