import streamlit as st


def project_2_page():
    """
    """
    st.title(
        """
        ****Fast API****

            the Python FastAPI framework, designed to deliver high-performance APIs using asynchronous operations. 
            The backend is powered by an asynchronous database engine, ensuring efficient handling of 
            data-intensive tasks and optimizing response times.

            For authentication, the project integrates a secure OAuth2PasswordBearer flow in combination with JWT tokens, 
            providing reliable token-based authentication and authorization mechanisms. This setup enhances security while 
            maintaining scalability and responsiveness, aligning with modern API standards.
        """)
    
    st.write("")
    st.write("")
    st.write("")

    st.write("- ****Fast API App creation****")
    app_code = """
        class FastAPIApp:
            def __init__(self, version: str = "1.0.0"):
                self.app_version = version
                # Configure logging
                self._configure_logging()
                
                # Initialize FastAPI app
                self.app = FastAPI(
                    title="Gooddreamer Analytics Data API",
                    description="API for handling Gooddreamer data analytics.",
                    version=self.app_version,
                    docs_url=None if not settings.DEBUG else "/docs",
                    redoc_url="/redoc",
                    lifespan=self._lifespan
                )
                
                # Add middleware
                self._add_middleware()
                
                # Include routers
                self._include_routers_v1()
                
            def _configure_logging(self):
                logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                )
            
            @asynccontextmanager
            async def _lifespan(self, app: FastAPI):
                print("Starting up...")
                async with sqlite_engine.begin() as conn:
                    await conn.run_sync(SqliteBase.metadata.create_all)
                yield
                print("Shutting down...")
                await sqlite_engine.dispose()
                
            def _add_middleware(self):
                # Add CORS Middleware
                if settings.DEBUG:
                    self.app.add_middleware(
                        CORSMiddleware,
                        allow_origins=["*"],
                        allow_credentials=True,
                        allow_methods=["*"],
                        allow_headers=["*"],
                    )
                else:
                    self.app.add_middleware(
                        CORSMiddleware,
                        allow_origins=[config("FRONTEND_URL")],
                        allow_credentials=True,
                        allow_methods=["GET", "POST"],
                        allow_headers=["Authorization", "Content-Type"],
                    )

                @self.app.middleware("http")
                async def log_requests(request: Request, call_next):
                    start_time = time.time()
                    # Process the request and get the original response
                    original_response = await call_next(request)

                    # Clone the original response content
                    content = b""
                    async for chunk in original_response.body_iterator:
                        content += chunk

                    # Create a new response with the same content
                    new_response = Response(
                        content=content,
                        status_code=original_response.status_code,
                        headers=dict(original_response.headers),
                        media_type=original_response.media_type,
                    )

                    # Attempt to parse JSON if possible
                    try:
                        response_body = json.loads(content.decode())  # Parse JSON
                    except json.JSONDecodeError:
                        response_body = content.decode()  # Fallback to plain text

                    process_time = time.time() - start_time

                    # Log details
                    async_gen = get_sqlite()
                    session = await anext(async_gen)

                    data = LogData(
                        url=str(request.url),
                        method=request.method,
                        time=process_time,
                        status=new_response.status_code,
                        response=response_body,
                        created_at=datetime.now()
                    )
                    session.add(data)
                    await session.commit()
                    await session.close()

                    return new_response
                
                # Security headers middleware
                @self.app.middleware("http")
                async def security_headers_middleware(request: Request, call_next):
                    response = await call_next(request)
                    response.headers["X-Content-Type-Options"] = "nosniff"
                    response.headers["X-Frame-Options"] = "DENY"
                    response.headers["Strict-Transport-Security"] =\
                        "max-age=31536000; includeSubDomains"
                    response.headers["Referrer-Policy"] = "same-origin"
                    response.headers["Permissions-Policy"] = (
                        "geolocation=(), microphone=(), camera=()"
                    )
                    return response
                
                # CSRF token middleware
                @self.app.middleware("http")
                async def add_csrf_token_middleware(request: Request, call_next):
                    CSRF_TOKEN_NAME = "csrf_token"
                    if CSRF_TOKEN_NAME not in request.session:
                        csrf_token = secrets.token_hex(16)
                        request.session[CSRF_TOKEN_NAME] = csrf_token
                    response = await call_next(request)
                    csrf_token = request.session[CSRF_TOKEN_NAME]
                    response.set_cookie(
                        key=CSRF_TOKEN_NAME,
                        value=csrf_token,
                        httponly=True,
                        secure=True
                    )
                    return response

                # Session Middleware
                self.app.add_middleware(
                    SessionMiddleware, 
                    secret_key=config("CSRF_SECRET"))

            def _include_routers_v1(self):
                # Include application routers
                self.app.include_router(auth_router, tags=["Authentication"])
                self.app.include_router(revenue_router, tags=["Revenue"])
                self.app.include_router(chapter_router, tags=["Chapter"])
                self.app.include_router(chapter_purchase_router, tags=["Chapter Purhcase"])
                self.app.include_router(user_activity_router, tags=["User Activity"])
                self.app.include_router(retention_router, tags=["Retention"])
                self.app.include_router(feature_data_router, tags=["Feature Data"])
                self.app.include_router(new_install_router, tags=["New Install"])
                self.app.include_router(seo_router, tags=["SEO"])
                self.app.include_router(sem_router, tags=["SEM"])
                self.app.include_router(novel_router, tags=["Novel All"])
                self.app.include_router(data_all_time_router, tags=["Data All Time"])
                self.app.include_router(aggregated_data, tags=["Aggregated Data"])
                self.app.include_router(overview_router, tags=["Overview Data"])
                self.app.include_router(chapter_read_router, tags=["Chapter Read Data"])

            def run(self):
                uvicorn_run(
                    "main:app_instance.app", 
                    host=settings.HOST,
                    port=settings.PORT,
                    workers=config("WORKERS", default=5, cast=int),
                    reload=settings.DEBUG,
                    log_level="info" if not settings.DEBUG else "debug",
                    timeout_keep_alive=30
                )
    """
    with st.expander("View code:"):
        st.code(app_code, language="python")

    st.write("- ****Fast API Config****")
    config_code = """
        class Settings(BaseSettings):
            API_V1_STR: str = "/api/v1"
            PROJECT_NAME: str = "Gooddreamer Data API V1.0"

            # Sqlite database
            SQLITE_DB_URL: str = "sqlite+aiosqlite:///./app/db/external_api.db"

            # JWT
            JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
            JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
            ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
            REFRESH_TOKEN_EXPIRE_DAYS: int = config("REFRESH_TOKEN_EXPIRE_DAYS", cast=int)
            ALGORITHM: str = "HS256"

        class ProductionSettings(Settings):
            DEBUG: bool = False

            # DATABASE
            DB_URL: str = config("DB_URL", cast=str)
            HOST: str = config("HOST", cast=str)
            PORT: int = config("PORT", cast=int)
            

        class DevelopmentSettings(Settings):
            DEBUG: bool = True

            # DATABASE
            DB_URL: str = config("DEV_DB_URL", cast=str)
            HOST: str = config("DEV_HOST", cast=str)
            PORT: int = config("DEV_PORT", cast=int)
            

        @lru_cache
        def get_settings() -> Settings:
            env = config("ENV", cast=str)

            if env == "production":
                print("Loading production settings")
                return ProductionSettings()
            else:
                print("Loading development settings")
                return DevelopmentSettings()

        settings = get_settings()r
    """
    with st.expander("View config code:"):
        st.code(config_code, language="python")

    st.write("- ****Database engine and session creation****")
    database_code = """
        # Create a sqlite engine
        sqlite_engine = create_async_engine(
            settings.SQLITE_DB_URL,
            echo=False,  # Log SQL queries in development
            poolclass=StaticPool,
            pool_pre_ping=True
        )

        # Create a sqlite async session
        sqlite_async_session = sessionmaker(
            bind=sqlite_engine,
            expire_on_commit=False,
            class_=AsyncSession  # Define the session as AsyncSession
        )

        # Create a global async engine (shared across requests)
        engine = create_async_engine(
            settings.DB_URL,
            echo=False,  # Log SQL queries in development
            pool_size=12,
            max_overflow=12,
            pool_timeout=500,
            pool_recycle=1800,
            pool_pre_ping=True,
            connect_args={"connect_timeout": 10} # Set connection timeout for robustness
        )

        # Configure a sessionmaker that creates read-only sessions
        async_session_maker = sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,       
            autocommit=False,     
        )

        async def get_db():
            async with async_session_maker() as session:
                try:
                    yield session
                finally:
                    await session.close()

        async def get_sqlite():
            async with sqlite_async_session() as session:
                try:
                    yield session
                finally:
                    await session.close()
    """
    with st.expander("View database engine and session code:"):
        st.code(database_code, language="python")

    st.write("- ****JWT Token creation and verification****")
    token_code = """
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        def verify_password(plain_password: str, hashed_password: str) -> bool:
            return pwd_context.verify(plain_password, hashed_password)


        def create_access_token(
            subject: str | Any, 
            expires_delta: timedelta = timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        ) -> str:
            expire = datetime.now() + expires_delta
            to_encode = {
                "exp": expire.timestamp(), 
                "sub": str(subject), 
                "type": "access"}
            encoded_jwt = jwt.encode(
                to_encode, 
                settings.JWT_SECRET_KEY, 
                algorithm=settings.ALGORITHM)
            return encoded_jwt


        def create_refresh_token(
            subject: str | Any, 
            expires_delta: timedelta = timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        ) -> str:
            expire = datetime.now() + expires_delta
            to_encode = {
                "exp": expire.timestamp(), 
                "sub": str(subject), 
                "type": "refresh"}
            encoded_jwt = jwt.encode(
                to_encode, 
                settings.JWT_SECRET_KEY,
                algorithm=settings.ALGORITHM)
            return encoded_jwt


        async def refresh_access_token(
                sqlite_session: AsyncSession, 
                refresh_token: str):
            # decode the refresh token, validate it, and issue a new access token.
            payload = jwt.decode(
                refresh_token, 
                settings.JWT_SECRET_KEY, 
                algorithms=[settings.ALGORITHM])
            user_id = payload.get("sub")
            query_personal_token = select(UserToken).filter_by(user_id=user_id)
            personal_token_data = await sqlite_session.execute(query_personal_token)
            personal_token = personal_token_data.scalars().first()

            if not personal_token or payload.get("type") != "refresh":
                if personal_token.is_revoked:
                    raise JWTError("Invalid refresh token")
            
            new_access_token = create_access_token(subject=user_id)
            personal_token.access_token = new_access_token
            personal_token.updated_at = datetime.now()
            await sqlite_session.commit()
            await sqlite_session.close()

            return new_access_token


        async def verify_access_token(
                sqlite_session: AsyncSession, 
                token: str):
            payload = jwt.decode(
                token, 
                settings.JWT_SECRET_KEY, 
                algorithms=[settings.ALGORITHM])
            id: str = payload.get("sub")
            query_personal_token = select(UserToken).filter_by(user_id=id)
            personal_token_data = await sqlite_session.execute(query_personal_token)
            personal_token = personal_token_data.scalars().first()
            
            if not personal_token or payload.get("type") != "access":  
                if personal_token.is_revoked:    
                    raise JWTError("Invalid access token")
            
            return TokenData(id=personal_token.user_id)


        async def verify_csrf_token(request: Request):
            csrf_token_from_request = request.cookies.get("csrf_token")
            csrf_token_from_session = request.session.get("csrf_token") 
            
            if not csrf_token_from_request or csrf_token_from_request != csrf_token_from_session:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid CSRF Token!"
                )
            return csrf_token_from_request
        
        
        async def get_current_user(
            token: str = Depends(oauth2_scheme),
            db: AsyncSession = Depends(get_db),
            sqlite_session: AsyncSession = Depends(get_sqlite)
        ):
            credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            # If the access token has expired, attempt to refresh it
            query_refresh_token = select(UserToken).filter_by(access_token=token)
            data_refresh_token = await sqlite_session.execute(query_refresh_token)
            user_token = data_refresh_token.scalars().first()
            if user_token is None:
                raise credentials_exception
            if user_token.is_revoked:
                raise credentials_exception

            try:
                # Try to verify the access token
                token_data = await verify_access_token(
                    sqlite_session, token)
            except ExpiredSignatureError:
                # Verify and refresh the access token using the refresh token
                new_access_token = await refresh_access_token(
                    sqlite_session, user_token.refresh_token)
                # Re-attempt to verify the new access token
                token_data = await verify_access_token(
                    sqlite_session, new_access_token)
            except (JWSSignatureError, JWTError):
                raise credentials_exception
            # Fetch the user from the database
            user = await get_user_by_id(id=token_data.id, session=db)
            
            if user is None:
                raise credentials_exception
            return user
    """
    with st.expander("View JWT Token creation and verification code:"):
        st.code(token_code, language="python")

    st.write("- ****Authentication Endpoint****")
    auth_code = """
        @router.post("/api/login", response_model=TokenBase)
        async def login_user(
            creds: OAuth2PasswordRequestForm = Depends(), 
            session: AsyncSession = Depends(get_db),
            sqlite_session: AsyncSession = Depends(get_sqlite),
            csrf_token : str = Depends(verify_csrf_token)):
            # Retrieve user from the database by email
            result = await session.execute(select(GooddreamerUserData).where(GooddreamerUserData.email == creds.username))
            user = result.scalar()
            user_role = roles(creds.username)
            
            if not user or not user_role or not verify_password(creds.password, user.password_hash):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid email or password!",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            # Create JWT token and store it to sqlite
            personal_token = await user_token(
                session=sqlite_session, 
                user_id=user.id, 
                role=user_role,
                access_token=create_access_token(subject=user.id), 
                refresh_token=create_refresh_token(subject=user.id))
            
            # Return access token in JSON response and refresh token in headers
            response = JSONResponse(
                content={
                    "access_token": personal_token.get("access_token"), 
                    "token_type": "Bearer", 
                    "role": user_role,
                    "success": True})
            response.headers["Authentication"] = str(user.id)

            return response
    """
    with st.expander("Authentication Code:"):
        st.code(auth_code, language="python")

    st.write("- ****Restricted Endpoint****")
    restricted_endpoint = """
        @router.get("/api/overview", response_model=OverviewData)
        async def overview(
            session: AsyncSession = Depends(get_db),
            sqlite_session: AsyncSession = Depends(get_sqlite),
            current_user: GooddreamerUserData = Depends(get_current_user),# Validating token
            from_date: date = Query(
                ..., description="The start date of data you want to fetch"),
            to_date: date = Query(
                ..., description="The end date of data you want to fetch")
        ):
            try:
                overview = await fetch_overview(
                    session=session, 
                    sqlite_session=sqlite_session, 
                    from_date=from_date, 
                    to_date=to_date)
                if not overview:
                    raise HTTPException(
                        status_code=404, detail="No data found for the specified date range."
                    )    
                return overview
            except Exception as e:
                raise HTTPException(
                    status_code=500, detail=f"An error occurred: {str(e)}"
                )
    """

    with st.expander("Restricted endpoint code:"):
        st.code(restricted_endpoint, language="python")
