# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import mooc_scraper.settings as s

Base = declarative_base()

def db_connect():
    return create_engine(URL(**s.DATABASE))

def create_opencourse_table(engine):
    Base.metadata.create_all(engine)


class OpenCourse(Base):
    __tablename__ = 'opencourse'
    __table_args__ = (UniqueConstraint('subject', 'start_date', 'link', name='uix'), )
    
    id = Column(Integer, primary_key=True)
    course = Column('course', String)
    subject = Column('subject', String)
    university = Column('university', String, nullable=True)
    provider = Column('provider', String, nullable=True)
    start_date = Column('start_date', String, nullable=True)
    duration = Column('duration', String, nullable=True)
    link = Column('link', String)
    date_scraped = Column('date_scraped', Date)
