# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockdataItem(scrapy.Item):
    #STT = scrapy.Field()
    Ngay = scrapy.Field()
    Giathamchieu = scrapy.Field()
    Thaydoi = scrapy.Field()
    Thaydoiphantram = scrapy.Field()
    Dongcua = scrapy.Field()
    Khoiluong = scrapy.Field()
    Mocua = scrapy.Field()
    Caonhat= scrapy.Field()
    Thapnhat= scrapy.Field()
    GDthoathuan= scrapy.Field()
    Nuocngoaimua = scrapy.Field()
    Nuocngoaiban = scrapy.Field()
    Giatri = scrapy.Field()

