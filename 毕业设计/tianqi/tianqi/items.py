# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TianqiItem(scrapy.Item):
    city =  scrapy.Field()#城市
    wendu = scrapy.Field()#温度
    tianqi = scrapy.Field()#天气
    wencha = scrapy.Field()#最高(低）温度
    shidu = scrapy.Field()#湿度
    fengxiang = scrapy.Field()#风向
    kqzl = scrapy.Field()#空气质量
    zwx = scrapy.Field()#紫外线
    pass
