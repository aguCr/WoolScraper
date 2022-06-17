
import scrapy


class WoolsScraperItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    delivery_time = scrapy.Field()
    needle_size = scrapy.Field()
    composition = scrapy.Field()
