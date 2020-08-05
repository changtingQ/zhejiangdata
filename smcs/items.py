# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmcsItem(scrapy.Item):
    site_name = scrapy.Field()
    license_key = scrapy.Field()
    top_domain = scrapy.Field()
    belonging_city = scrapy.Field()
    wzfzr = scrapy.Field()
    wzfzrdh = scrapy.Field()
    wzfzr_sjhm = scrapy.Field()
    ztfzr = scrapy.Field()
    ztfzrdh = scrapy.Field()
    ztfzr_sjhm = scrapy.Field()