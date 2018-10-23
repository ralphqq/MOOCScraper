# -*- coding: utf-8 -*-
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker

from class_central.models import db_connect, create_opencourse_table, OpenCourse

class MoocScraperPipeline(object):
    def process_item(self, item, spider):
        item.setdefault('course', None)
        item.setdefault('subject', None)
        item.setdefault('university', None)
        item.setdefault('provider', None)
        item.setdefault('start_date', None)
        item.setdefault('duration', None)
        item.setdefault('link', None)
        item.setdefault('date_scraped', None)
        return item


class DBPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_opencourse_table(engine)
        self.session = sessionmaker(bind=engine)
    
    def process_item(self, item, spider):
        session = self.session()
        
        try:
            insert_stmt = insert(OpenCourse  .__table__).values(**item)
            do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
                constraint='uix'
            )
            session.execute(do_nothing_stmt)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
        
        return item
