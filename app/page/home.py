import streamlit as st

def home_page():
    """
    """
    st.title("Welcome to My Portfolio Page! 📊")

    # Header
    st.title("My Name is Mochamad Andimas")
    st.write("**Data Analyst | Data Engineer**")

    # Contact Information
    st.markdown("""
    📧 **Email:** mochamadandimas@gmail.com  
    🌐 [GitHub](https://github.com/MochAndimas) | [LinkedIn](https://www.linkedin.com/in/mochamad-andimas-83146514a/)  
    """)
    # Add a Download Button
    with open("./app/assets/CV - Mochamad Andimas.pdf", "rb") as file:
        resume_pdf = file.read()

    st.download_button(
        label="📄 Download My Resume",
        data=resume_pdf,
        file_name="CV_Mochamad_Andimas.pdf",
        mime="application/pdf"
    )

    # Profile Summary
    st.header("Profile Summary")
    st.write("""
    Hi, I'm Mochamad Andimas—Dimas for short—a dedicated and results-driven Data Analyst with a background in Management, E-Business, and over 6 years of professional experience, including 4 years in Business Development and 2 years specializing in Data Analysis. From experiance enables me to bridge business strategy with data-driven insights to create value and drive decision-making.

    In my current role at Gooddreamer.id, I specialize in transforming raw data into actionable insights. I am responsible for compiling, cleaning, and analyzing data from diverse internal and external sources, utilizing advanced tools and techniques to support business growth. My key achievements include designing and implementing dynamic data visualizations and dashboards using Python and its powerful libraries, allowing stakeholders to uncover trends, monitor KPIs, and make informed decisions.

    As a professional, I am a fast learner, detail-oriented problem solver, and enthusiastic about embracing emerging technologies to solve complex business challenges. I thrive in collaborative environments and i can turning data into impactful business strategies.
    """)

    # Education
    st.header("Education")
    st.write("""
    ****Bina Nusantara University | 2011 - 2017****
             
        - Bachelor Degree, Management E-Business  
             
    ****SMAN 3 Jakarta | 2008 - 2011****
    """)

    # Additional Education
    st.header("Additional Education")
    st.write("""
    ****Zero To Mastery Academy | March 2022****
             
        - Complete Machine Learning & Data Science Bootcamp  
             
    ****Zero To Mastery Academy | February 2022****
             
        - Complete SQL and Databases Bootcamp  
             
    ****Zero To Mastery Academy | January 2022****
             
        - Complete Python Developer in 2022  
    """)

    # Work Experience
    st.header("Work Experience")
    st.write("""
    ****Gooddreamer.id | Data Analyst | Oct 2022 - Present****
       
        - Compiling internal and external data  
        - Data processing, analysis, and visualization  
        - Created internal reporting dashboards using Python 
     
    ****Sisi Sini Coffee | Social Media & Marketing | Jun 2021 - Jan 2022****
             
        - Created promotional content 
        - Managed ads using Facebook Ads Manager  
    
    ****PT. BINA USAHA LIMA PRIMA | Business Development | Aug 2019 - Jun 2021****
    
        - Data entry and data processing using Microsoft Excel  
        - search/maintain clients  
        - Logistics coordination
    """)

    # Skills
    st.header("Skills")
    st.write("""
    ****Programming Languages:**** 
             
        - Python  
    ****Libraries/Tools:**** 
             
        - Pandas
        - NumPy
        - FastAPI
        - Flask
        - PostgreSQL
        - MySQL  
        - streamlit
        - SQLalchemy
    ****Soft Skill:**** 
        
        - Data Processing
        - Data Cleaning
        - Data Analysis
        - Data Visualization
    """)

