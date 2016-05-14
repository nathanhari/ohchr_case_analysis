# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadcasesItem(scrapy.Item):
    Committee = scrapy.Field()
    Communication_numbers = scrapy.Field()
    Author = scrapy.Field()
    Display_name = scrapy.Field()
    Victim = scrapy.Field()
    Countries = scrapy.Field()
    Admission_date = scrapy.Field()
    Submission_date = scrapy.Field()
    Date_of_adoption_of_the_Views = scrapy.Field()
    Session_No = scrapy.Field()
    Type_of_decision = scrapy.Field()
    Comment = scrapy.Field()
    Issues = scrapy.Field()
    Articles = scrapy.Field()
    Id_string = scrapy.Field()
    file_urls = scrapy.Field()    
    files = scrapy.Field()