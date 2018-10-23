# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

def fix_duration_string(self, text):
    """Clean up raw string for duration info"""
    for t in text:
        dur = [d.strip() for d in t.split(',')]
        yield ','.join(dur)


class MoocScraperItem(scrapy.Item):
    course = scrapy.Field()
    subject = scrapy.Field()
    university = scrapy.Field()
    provider = scrapy.Field()
    start_date = scrapy.Field()
    duration = scrapy.Field()
    link = scrapy.Field()
    date_scraped = scrapy.Field()

class MoocScraperItemLoader(ItemLoader):
    default_input_processor = MapCompose(lambda x: x.strip())
    default_output_processor = TakeFirst()
    
    subject_in = MapCompose(lambda x: x.split('|')[0].strip())
    
    duration_in = fix_duration_string
    
    date_scraped_in = MapCompose(lambda x: x)
