# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ActiveItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    operation = scrapy.Field()
    price = scrapy.Field()
    type = scrapy.Field()