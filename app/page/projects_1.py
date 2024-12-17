import streamlit as st

def project_1_page():
    """
    """
    st.title(
        """
        ****Internal Dashboard Reporting Gooddreamer****

            I build this dashboard using Streamlit python libraries 
            and for the visualization i used pyhthon Plotly libraries.
        """)
    
    main_code = """
        # --- App Settings ---
        session_id = get_session(cookie_controller.get("session_id"))
        HOST = st.secrets["api"]["HOST"] if config("ENV") == "production" else st.secrets["api"]["DEV_HOST"]
        footer(st)

        # --- Initialize session state ---
        if 'page' not in st.session_state:
            st.session_state.page = 'login'
        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False
        if 'role' not in st.session_state:
            st.session_state.role = None

        # --- PAGE DEFINITIONS ---
        # Logger Page
        logger_page = st.Page(page=logger, title="Update Data", url_path="/update-date")

        # Login Page
        login_page = st.Page(page=login, title="Login")

        # Overview data page
        overall_page = st.Page(page=overall, title="Overall Data", url_path="/overall-page", icon="🗃")
        aggregated_page = st.Page(page=aggregated, title="Aggregated Data", url_path="aggregated", icon="📋")
        data_all_time_page = st.Page(page=data_all_time, title="Data All Time", url_path="data-all-time", icon="📊")
        all_user_activity = st.Page(page=user_activity, title="User Activity", url_path="all-user-activity", icon="👣")
        all_retention = st.Page(page=retention, title="Retention", url_path="all-retention", icon="📉")
        novel_details_page = st.Page(page=novel_details, title="Novel Details", url_path="novel-details", icon="📖")
        all_novel_page = st.Page(page=all_novel, title="Novel Analytics", url_path="novel-analytics", icon="📑")

        # Acquisition page
        new_install_page = st.Page(page=new_install, title="New Install", url_path="new-install", icon="🆕️")
        seo_page = st.Page(page=seo, title="SEO", url_path="seo", icon="⌨️")
        sem_page = st.Page(page=sem, title="SEM", url_path="sem", icon="💻")

        # App data page
        app_revenue_page = st.Page(page=revenue, title="💵 Revenue Coin & Admob", url_path="app-revenue", icon="📱")
        app_chapter_page = st.Page(page=chapter, title="📚 All Novel Reader & Purchase",url_path="app-chapter-data", icon="📱")
        app_chapter_read_page = st.Page(page=chapter_read, title="📖 Chapter Reader", url_path="app-chapter-read", icon="📱")
        app_chapter_purchase = st.Page(page=chapter_purchase, title="📕 Chapter Purchase Types", url_path="app-chapter-purchase", icon="📱")
        app_user_activity = st.Page(page=user_activity, title="👣 User Activity", url_path="app-user-activity", icon="📱")
        app_retention = st.Page(page=retention, title="📉 Retention", url_path="app-retention", icon="📱")

        # Web data Page
        web_revenue_page = st.Page(page=revenue, title="💵 Revenue Coin & Adsense", url_path="web-revenue", icon="🖥️")
        web_chapter_page = st.Page(page=chapter, title="📚 All Novel Reader & Purchase",url_path="web-chapter-data", icon="🖥️")
        web_chapter_read_page = st.Page(page=chapter_read, title="📖 Chapter Reader", url_path="web-chapter-read", icon="🖥️")
        web_chapter_purchase = st.Page(page=chapter_purchase, title="📕 Chapter Purchase Types", url_path="web-chapter-purchase", icon="🖥️")
        web_user_activity = st.Page(page=user_activity, title="👣 User Activity", url_path="web-user-activity", icon="🖥️")
        web_retention = st.Page(page=retention, title="📉 Retention", url_path="web-retention", icon="🖥️")

        # Feature Data
        redeem_code_page = st.Page(page=redeem_code, title="Redeem Code", url_path="redeem-code", icon="🎟")
        illustration_page = st.Page(page=illustration_transaction, title="Illustration Transaction", url_path="illustration-transaction", icon="🎨")
        offline_mode_page = st.Page(page=offline_mode, title="Offline Mode", url_path="offline-mode", icon="📴")

        # show menu only for spesific role
        if st.session_state.role in ['developer', 'superadmin']:
            menu_options = {
                "🗂 Overview Data" : [
                    overall_page, aggregated_page, data_all_time_page, 
                    all_user_activity, all_retention, novel_details_page, 
                    all_novel_page],
                "🔎 Acquisition Data" : [new_install_page, seo_page, sem_page],
                "📱 App Data" : [
                    app_revenue_page, app_chapter_page, app_chapter_read_page,
                    app_chapter_purchase, app_user_activity,
                    app_retention],
                "🖥️ Web Data" : [
                    web_revenue_page, web_chapter_page, web_chapter_read_page,
                    web_chapter_purchase, web_user_activity, 
                    web_retention],
                "📲 Feature Data" : [redeem_code_page, illustration_page, offline_mode_page]
            }
            if st.session_state.role == 'developer':
                menu_options["Update Data"] = [logger_page]
        elif st.session_state.role == 'growth':
            menu_options = {
                "🗂 Overview Data" : [
                    overall_page, aggregated_page, all_user_activity, 
                    all_retention, novel_details_page, all_novel_page],
                "🔎 Acquisition Data" : [new_install_page, seo_page, sem_page],
                "📱 App Data" : [
                    app_chapter_page, app_chapter_read_page, app_chapter_purchase,
                    app_user_activity, app_retention],
                "🖥️ Web Data" : [
                    web_chapter_page, web_chapter_read_page, web_chapter_purchase,
                    web_user_activity, web_retention],
                "📲 Feature Data" : [redeem_code_page, illustration_page, offline_mode_page]
            }
        elif st.session_state.role == 'operation':
            menu_options = {
            "🗂 Overview Data" : [aggregated_page, novel_details_page, all_novel_page],
            "📱 App Data" : [
                app_chapter_page, app_chapter_read_page, app_chapter_purchase],
            "🖥️ Web Data" : [
                web_chapter_page, web_chapter_read_page, web_chapter_purchase],
            "📲 Feature Data" : [redeem_code_page, illustration_page, offline_mode_page]
            }

        # --- NAVIGATION ---
        with st.sidebar:
            if st.session_state["logged_in"]:
                st.image("./streamlit_app/page/gd_wide.png", use_column_width=True)
                page = st.navigation(
                    menu_options,
                    position='sidebar'
                )
                asyncio.run(logout(st, HOST, session_id))
            else:
                page = st.navigation(
                    [login_page],
                    position='sidebar'
                )

        # --- PAGE CONTENT ---
        try:
            if not st.session_state['logged_in']:
                asyncio.run(login.show_login_page(HOST))
            else:
                page_handlers = {
                    overall_page: lambda: overall.show_overall_page(HOST),
                    aggregated_page: lambda: aggregated.show_aggregated_page(HOST),
                    data_all_time_page: lambda: data_all_time.show_data_all_time_page(HOST),
                    all_user_activity: lambda: user_activity.show_user_activity_page(HOST, source='all'),
                    all_retention: lambda: retention.show_retention_page(HOST, source='all'),
                    novel_details_page: lambda: novel_details.show_novel_details_page(HOST),
                    all_novel_page: lambda: all_novel.show_all_novel_page(HOST),
                    new_install_page: lambda: new_install.show_new_install_page(HOST),
                    seo_page: lambda: seo.show_seo_page(HOST),
                    sem_page: lambda: sem.show_sem_page(HOST),
                    app_chapter_page: lambda: chapter.show_chapter_page(HOST, source='app'),
                    web_chapter_page: lambda: chapter.show_chapter_page(HOST, source='web'),
                    app_revenue_page: lambda: revenue.show_revenue_page(HOST, source='app'),
                    web_revenue_page: lambda: revenue.show_revenue_page(HOST, source='web'),
                    app_chapter_read_page: lambda: chapter_read.show_chapter_reader_page(HOST, source="app"),
                    web_chapter_read_page: lambda: chapter_read.show_chapter_reader_page(HOST, source="web"),
                    app_chapter_purchase: lambda: chapter_purchase.show_chapter_purchase_page(HOST, source='app'),
                    web_chapter_purchase: lambda: chapter_purchase.show_chapter_purchase_page(HOST, source='web'),
                    app_user_activity: lambda: user_activity.show_user_activity_page(HOST, source='app'),
                    web_user_activity: lambda: user_activity.show_user_activity_page(HOST, source='web'),
                    app_retention: lambda: retention.show_retention_page(HOST, source='app'),
                    web_retention: lambda: retention.show_retention_page(HOST, source='web'),
                    redeem_code_page: lambda: redeem_code.show_redeem_code_page(HOST),
                    illustration_page: lambda: illustration_transaction.show_illustration_transaction_page(HOST),
                    offline_mode_page: lambda: offline_mode.show_offline_mode_page(HOST),
                    logger_page: lambda: logger.show_logger_page(HOST)
                }
                if page in page_handlers:
                    asyncio.run(page_handlers[page]())  # Call the appropriate function based on the page
                    st.session_state.page = page.url_path
        except Exception as e:
            st.error(f"Error Fetching Data!")
    """
    
    st.write("")
    st.write("")
    st.write("")

    with st.expander("View Main Code"):
        st.code(main_code, language="python")

    st.write("")
    st.write("")
    st.write("")

    st.image("app/assets/login.png")
    login_code = """
        st.image("./streamlit_app/page/gd_wide.png", width=300)
        st.title('Gooddreamer Analytics')
        
        with st.form("log-in", border=False):
            email = st.text_input('Email')
            password = st.text_input('Password', type='password')
            remember = st.checkbox('Remember Me!')
            submit = st.form_submit_button("Login")
            
        if submit:
            with st.spinner("Loggin in!"):
                async with httpx.AsyncClient(timeout=120) as client:
                    # Make a GET request to initialize the CSRF token
                    csrf_response = await client.post(
                        f"{host}/api/login/csrf-token",
                        data={"username": email, "password": password})
                    
                    # Check if the CSRF cookie is set
                    csrf_token = csrf_response.cookies.get("csrf_token", None)

                    if csrf_token is None:
                        return st.error("CSRF token initialization failed. Please try again!")
                    
                    response = await client.post(
                        f"{host}/api/login",
                        data={"username": email, "password": password},
                        cookies={"csrf_token": csrf_token}
                    )
                    response_data = response.json()

                if response_data.get("success", False):
                    user = get_user(response.headers["Authentication"])
                    st.session_state.role = response_data['role']
                    st.session_state.logged_in = True
                    st.session_state.page = 'home'
                    st.session_state._user_id = response.headers['Authentication']

                    if remember:
                        cookie_controller.set(
                            name="session_id", 
                            value=user.session_id,
                            path="/",
                            expires=datetime.now()+timedelta(days=7),
                            domain=st.secrets["api"]["HOST"],
                            same_site="strict",
                            secure=True
                        )
                    st.rerun()
                else:
                    st.error(f"{response_data.get("detail", "Invalid email or password! Please try again!")}")
    """
    with st.expander("View Login Code"):
        st.code(login_code, language="python")

    st.write("")
    st.write("")
    st.write("")

    st.image("app/assets/menu.png")
    st.image("app/assets/chart1.png")
    st.image("app/assets/chart2.png")
    st.image("app/assets/chart3.png")
    st.image("app/assets/chart4.png")
    st.image("app/assets/chart5.png")

    menu_code = """
        with st.container(border=True):
            # Calculate preset date ranges
            today = datetime.date.today()
            this_month_start = today.replace(day=1)
            last_month_start = (this_month_start - datetime.timedelta(days=1)).replace(day=1)
            last_month_end = this_month_start - datetime.timedelta(days=1)
            this_week_start = today - datetime.timedelta(days=today.weekday())
            last_week_start = this_week_start - datetime.timedelta(days=7)  # Monday of the previous week
            last_week_end = this_week_start - datetime.timedelta(days=1)    # Last Sunday
            last_7days_start = today - datetime.timedelta(days=7)
            last_7days_end  = today - datetime.timedelta(days=1)
            preset_date = {
                None: (last_week_start, last_week_end),
                "Custom Range" : "custom_range",
                "This Month" : (this_month_start, today),
                "Last Month" : (last_month_start, last_month_end),
                "This Week" : (this_week_start, today),
                "Last Week" : (last_week_start, last_week_end),
                "Last 7 Days": (last_7days_start, last_7days_end) 
            }
            period_options = st.selectbox("Periods", list(preset_date.keys()), placeholder="Choose a Periods", index=None, key=f"period_sem")
            if preset_date[period_options] != "custom_range":
                from_date, to_date = preset_date[period_options]
            else : 
                try:
                    from_date, to_date = st.date_input(
                        "Select Date Range",
                        value=(get_date_range(days=7, period='days')),
                        min_value=datetime.date(2022, 1, 1),
                        max_value=get_date_range(days=2, period='days')[1],
                        key="sem_date_range")
                except ValueError:
                    st.warning("Please Select A Range of date!")
            submit_button = st.button(label="Apply Filters", disabled=False, key="submit_button_sem")
        
        # Data Fetching with Loading State
        if submit_button:
            with st.spinner('Fetching data...'):  # Display loading spinner
                params = {
                    "from_date": from_date,
                    "to_date": to_date
                }
                    
                # Use partial application for cleaner task creation
                fetch_data_partial = partial(fetch_data, st, host=host)
                tasks = [
                    fetch_data_partial(uri=f'sem', params=params),
                    fetch_data_partial(uri=f'sem/daily-growth', params=params),
                    fetch_data_partial(uri=f'sem/chart', params=params)
                ]
                try:
                    data_text, data_persentase, data_chart = await asyncio.gather(*tasks)
                except httpx.RequestError as e:  # Handle potential exceptions
                    st.error(f"Error fetching data: {e}")
                    
                card_style(st)
                try:
                    if data_text and data_persentase and data_chart:
                        st.markdown(f'''<h1 align="center">Google SEM Performance</h1>''', unsafe_allow_html=True)

                        # -- google sem performance section -- 
                        col1, col2, col3, col4, col5, col6 = st.columns(6)
                        with col1:
                            create_card(
                                st,
                                card_title="Cost Spend",
                                card_value=data_text["google_sem"]["spend"],
                                card_daily_growth=data_persentase["google_sem"]["spend"],
                                class_name="google-sem-spend"
                            )
                        with col2:
                            create_card(
                                st,
                                card_title="Impressions",
                                card_value=data_text["google_sem"]["impressions"],
                                card_daily_growth=data_persentase["google_sem"]["impressions"],
                                class_name="google-sem-impressions"
                            )
                        with col3:
                            create_card(
                                st,
                                card_title="Clicks",
                                card_value=data_text["google_sem"]["clicks"],
                                card_daily_growth=data_persentase["google_sem"]["clicks"],
                                class_name="google-sem-clicks"
                            )
                        with col4:
                            create_card(
                                st,
                                card_title="Click Through Rate (CTR)",
                                card_value=data_text["google_sem"]["ctr"],
                                card_daily_growth=data_persentase["google_sem"]["ctr"],
                                types="persentase",
                                class_name="google-sem-ctr"
                            )
                        with col5:
                            create_card(
                                st,
                                card_title="Cost / Impressions (CPM)",
                                card_value=data_text["google_sem"]["cpm"],
                                card_daily_growth=data_persentase["google_sem"]["cpm"],
                                class_name="google-sem-cpm"
                            )
                        with col6:
                            create_card(
                                st,
                                card_title="Cost / Click (CPC)",
                                card_value=data_text["google_sem"]["cpc"],
                                card_daily_growth=data_persentase["google_sem"]["cpc"],
                                class_name="google-sem-cpc"
                            )

                        # google sem performance chart section
                        col7, col8 = st.columns(2)
                        with col7:
                            create_chart(st, data_chart["google_sem_spend_chart"])
                        with col8:
                            create_chart(st, data_chart["google_sem_metrics_chart"])
                        
                        create_chart(st, data_chart["google_sem_details_table"])

                        # -- google GDN performance section -- 
                        st.markdown(f'''<h1 align="center">Google - GDN Performance</h1>''', unsafe_allow_html=True)
                        col9, col10, col11, col12, col13, col14 = st.columns(6)
                        with col9:
                            create_card(
                                st,
                                card_title="Cost Spend",
                                card_value=data_text["google_gdn"]["spend"],
                                card_daily_growth=data_persentase["google_gdn"]["spend"],
                                class_name="google-awareness-spend"
                            )
                        with col10:
                            create_card(
                                st,
                                card_title="Impressions",
                                card_value=data_text["google_gdn"]["impressions"],
                                card_daily_growth=data_persentase["google_gdn"]["impressions"],
                                class_name="google-awareness-impressions"
                            )
                        with col11:
                            create_card(
                                st,
                                card_title="Clicks",
                                card_value=data_text["google_gdn"]["clicks"],
                                card_daily_growth=data_persentase["google_gdn"]["clicks"],
                                class_name="google-awareness-clicks"
                            )
                        with col12:
                            create_card(
                                st,
                                card_title="Click Through Rate (CTR)",
                                card_value=data_text["google_gdn"]["ctr"],
                                card_daily_growth=data_persentase["google_gdn"]["ctr"],
                                types="persentase",
                                class_name="google-awareness-ctr"
                            )
                        with col13:
                            create_card(
                                st,
                                card_title="Cost / Impressions (CPM)",
                                card_value=data_text["google_gdn"]["cpm"],
                                card_daily_growth=data_persentase["google_gdn"]["cpm"],
                                class_name="google-awareness-cpm"
                            )
                        with col14:
                            create_card(
                                st,
                                card_title="Cost / Click (CPC)",
                                card_value=data_text["google_gdn"]["cpc"],
                                card_daily_growth=data_persentase["google_gdn"]["cpc"],
                                class_name="google-awareness-cpc"
                            )

                        # google GDN performance chart section
                        col15, col16 = st.columns(2)
                        with col15:
                            create_chart(st, data_chart["google_gdn_spend_chart"])
                        with col16:
                            create_chart(st, data_chart["google_gdn_metrics_chart"])
                        
                        create_chart(st, data_chart["google_gdn_details_table"])

                        # -- Facebook display ad performance section -- 
                        st.markdown(f'''<h1 align="center">Facebook Display Ad Performance</h1>''', unsafe_allow_html=True)
                        col17, col18, col19, col20, col21, col22 = st.columns(6)
                        with col17:
                            create_card(
                                st,
                                card_title="Cost Spend",
                                card_value=data_text["facebook_gdn"]["spend"],
                                card_daily_growth=data_persentase["facebook_gdn"]["spend"],
                                class_name="fb-awareness-spend"
                            )
                        with col18:
                            create_card(
                                st,
                                card_title="Impressions",
                                card_value=data_text["facebook_gdn"]["impressions"],
                                card_daily_growth=data_persentase["facebook_gdn"]["impressions"],
                                class_name="fb-awareness-impressions"
                            )
                        with col19:
                            create_card(
                                st,
                                card_title="Clicks",
                                card_value=data_text["facebook_gdn"]["clicks"],
                                card_daily_growth=data_persentase["facebook_gdn"]["clicks"],
                                class_name="fb-awareness-clicks"
                            )
                        with col20:
                            create_card(
                                st,
                                card_title="Click Through Rate (CTR)",
                                card_value=data_text["facebook_gdn"]["ctr"],
                                card_daily_growth=data_persentase["facebook_gdn"]["ctr"],
                                types="persentase",
                                class_name="fb-awareness-ctr"
                            )
                        with col21:
                            create_card(
                                st,
                                card_title="Cost / Impressions (CPM)",
                                card_value=data_text["facebook_gdn"]["cpm"],
                                card_daily_growth=data_persentase["facebook_gdn"]["cpm"],
                                class_name="fb-awareness-cpm"
                            )
                        with col22:
                            create_card(
                                st,
                                card_title="Cost / Click (CPC)",
                                card_value=data_text["facebook_gdn"]["cpc"],
                                card_daily_growth=data_persentase["facebook_gdn"]["cpc"],
                                class_name="fb-awareness-cpc"
                            )

                        # facebook display ad performance chart section
                        col15, col16 = st.columns(2)
                        with col15:
                            create_chart(st, data_chart["facebook_gdn_spend_chart"])
                        with col16:
                            create_chart(st, data_chart["facebook_gdn_metrics_chart"])
                        
                        create_chart(st, data_chart["facebook_gdn_details_table"])

                except KeyError as ke:
                    if data_text.get("message"):
                        st.error(f"Error while feting metrics data: {data_text.get("message", None)}, KeyError: {ke}")
                    if data_persentase.get("message"):
                        st.error(f"Error while feting daily growth data: {data_persentase.get("message", None)}, KeyError: {ke}")
                    if data_chart.get("message"):
                        st.error(f"Error while feting chart data: {data_chart.get("message", None)}, KeyError: {ke}")

                except requests.RequestException as e:
                    st.error(f"Error fetching data: {e}") 
    """
    with st.expander("View Menu Code"):
        st.code(menu_code, language="python")
