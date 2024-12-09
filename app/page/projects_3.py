import streamlit as st


def project_3_page():
    """
    """
    st.title("""
        ****SQLalchemy ORM Daatabase****
    """)

    st.write("""
        - ****SQLalchemy declarative base code****
    """)
    declarative_base_code = """
        @as_declarative()
        class Base:
            id: int
            __name__: strr

            @declared_attr
            def __tablename__(cls) -> str:
                return cls.__name__.lower()
    """
    with st.expander("Declarative base code:"):
        st.code(declarative_base_code, language="python")

    st.write("""- ****SQLalchemy Database table code****""")
    table_code = """
        class GooddreamerUserData(Base):
            __tablename__ = 'gooddreamer_user_data'
            __mapper_args__ = {
                'polymorphic_identity': 'gooddreamer_user_data'
            }

            id = Column('id', Integer, primary_key=True, index=True)
            fullname = Column('fullname', String)
            email = Column('email', String)
            is_guest = Column('is_guest', Integer)
            registered_at = Column('registered_at', DateTime)
            created_at = Column('created_at', DateTime)
            password_hash = Column('password', String)

            gooddreamer_user_chapter_progression = relationship(
                'GooddreamerUserChapterProgression', 
                lazy=True, 
                back_populates='gooddreamer_user_data', 
                viewonly=True)

        class GooddreamerUserChapterProgression(Base):
            __tablename__ = 'gooddreamer_user_chapter_progression'
            __table_args__ = (
                ForeignKeyConstraint(['user_id'], ['gooddreamer_user_data.id']),
                ForeignKeyConstraint(['chapter_id'], ['gooddreamer_novel_chapter.id']),
                {'schema': None}
            )
            __mapper_args__ = {
                'polymorphic_identity': 'gooddreamer_user_chapter_progression'
            }

            id = Column("id", Integer, primary_key=True, index=True)
            user_id = Column("user_id", Integer, ForeignKey("gooddreamer_user_data.id"), index=True)
            chapter_id = Column("chapter_id", Integer, ForeignKey("gooddreamer_novel_chapter.id"), index=True)
            is_completed = Column("is_completed", Boolean)
            created_at = Column("created_at", DateTime)
            updated_at = Column("updated_at", DateTime)

            gooddreamer_user_data = relationship(
                'GooddreamerUserData', 
                lazy=True, 
                back_populates='gooddreamer_user_chapter_progression', 
                viewonly=True
            )
    """
    with st.expander("SQLalchemy database table code:"):
        st.code(table_code, language="python")

    st.write("""- ****SQLalchemy Asychronous database query****""")
    sqlalchemy_query = """
        async def query():
            query = select(
                    func.date(GooddreamerUserChapterProgression.updated_at).label('tanggal'),
                    GooddreamerUserChapterProgression.user_id.label('user_id'),
                    GooddreamerUserData.is_guest.label('is_guest'),
                    GooddreamerNovelChapter.novel_id.label('novel_id'),
                    GooddreamerNovel.novel_title.label('novel_title'),
                    DataCategory.category_name.label('category_name'),
                    Sources.name.label('source'),
                    func.date(GooddreamerUserData.created_at).label('install_date'),
                    func.count(GooddreamerUserChapterProgression.id).label('chapter_count')
                ).join(
                    GooddreamerUserChapterProgression.model_has_sources
                ).join(
                    GooddreamerUserChapterProgression.gooddreamer_novel_chapter
                ).join(
                    GooddreamerUserChapterProgression.gooddreamer_user_data
                ).join(
                    GooddreamerNovelChapter.gooddreamer_novel
                ).join(
                    ModelHasSources.sources
                ).join(
                    GooddreamerNovel.data_category
                ).filter(
                    ModelHasSources.model_type == 'App\\Models\\ChapterProgression',
                    func.date(GooddreamerUserChapterProgression.updated_at).between(from_date, to_date),
                    GooddreamerUserChapterProgression.is_completed.in_(read_is_completed)
                ).group_by(
                    func.date(GooddreamerUserChapterProgression.updated_at),
                    GooddreamerUserChapterProgression.user_id,
                    GooddreamerNovelChapter.novel_id,
                    Sources.name
                )
            # Stream the query results asynchronously
            results = await self.session.stream(query, execution_options={"yield_per": BATCH_SIZE, "stream_results": True})

            rows = []
            async for result in results:
                rows.append(result._asdict())  # Convert each row to a dictionary
            
            return rows
    """
    with st.expander("SQLalchemy database query code:"):
        st.code(sqlalchemy_query, language="python")

    
    