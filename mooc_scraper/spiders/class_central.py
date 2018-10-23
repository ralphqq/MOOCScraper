# -*- coding: utf-8 -*-
import datetime

import scrapy
from mooc_scraper.items import MoocScraperItem, MoocScraperItemLoader


class ClassCentralSpider(scrapy.Spider):
    name = 'class_central'
    allowed_domains = ['class-central.com']
    start_urls = ['https://www.class-central.com/subjects']

    def parse(self, response):
        subject_url = response.xpath(
            '//li/a[contains(@title, "List of")]/@href'
        ).extract()
        
        for url in subject_url:
            yield response.follow(url, 
                                  callback=self.parse_subject)


    def parse_subject(self, response):
        date_scraped = datetime.date.today()
        subject = response.xpath('//title/text()').extract_first()
        courses = response.xpath(
            '//tr[@itemtype="http://schema.org/Event"]'
        )
        
        for course in courses:
            name = course.xpath(
                './/span[@itemprop="name"]/text()'
            ).extract_first()
            link = course.xpath(
                './/a[@itemprop="url"]/@href'
            ).extract_first()
            university = course.xpath(
                './/a[contains(@class, "uni-name")]//text()'
            ).extract_first()
            provider = course.xpath(
                './/a[contains(@href, "/provider")]//text()'
            ).extract_first()
            duration = course.xpath(
                './/span[starts-with(@class, "hidden")]/text()'
            ).extract_first()
            start_date = course.xpath(
                './/td[contains(@class, "start-date")]/text()'
            ).extract_first()
            
            abs_link = response.urljoin(link)
            
            l = MoocScraperItemLoader(MoocScraperItem())
            l.add_value('course', name)
            l.add_value('subject', subject)
            l.add_value('university', university)
            l.add_value('provider', provider)
            l.add_value('start_date', start_date)
            l.add_value('duration', duration)
            l.add_value('link', abs_link)
            l.add_value('date_scraped', date_scraped)
            
            yield l.load_item()
        
        next_page_url = response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse_subject)
