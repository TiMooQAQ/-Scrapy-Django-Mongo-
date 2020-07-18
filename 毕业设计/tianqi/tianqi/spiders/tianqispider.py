# -*- coding: utf-8 -*-

import scrapy
from ..items import TianqiItem
import re

class TianqispiderSpider(scrapy.Spider):
    name = 'tianqispider'
    allowed_domains = ['tianqi.com']
    start_urls = ['https://www.tianqi.com/chinacity.html']
    def parse(self, response):
        city_list = response.xpath('/html/body/div[5]/div[3]/div[1]/span/a/@href').extract()
        for i in city_list:
            url = 'https://www.tianqi.com'+ i
            yield scrapy.Request(url,self.new_parse)
    def new_parse(self, response):
        item = TianqiItem()
        item['city'] = response.xpath('/html/body/div[5]/div/div[1]/dl/dd[1]/h2/text()').extract()[0]  # 城市
        item['wendu'] = response.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/p/b/text()').extract()[0]  # 温度
        item['tianqi'] = response.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/span/b/text()').extract()[0]  # 天气
        item['wencha'] = response.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/span/text()').extract()[0]  # 最高(低）温度
        item['shidu'] = re.findall(r'\d+', response.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[1]/text()').extract()[0])[0]  # 湿度
        item['fengxiang'] = re.findall(r'([^风向：].*)',response.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[2]/text()').extract()[0])[0]  # 风向
        item['zwx'] = re.findall(r'([^紫外线：].*)',response.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[3]/text()').extract()[0])[0]  # 紫外线
        item['kqzl'] = re.findall(r'\d+', response.xpath('/html/body/div[5]/div/div[1]/dl/dd[5]/h6/text()').extract()[0])[0]  # 空气质量
        yield item