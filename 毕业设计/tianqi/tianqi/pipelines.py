# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
class TianqiPipeline(object):
    def __init__(self):
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient('127.0.0.1', 27017)
        # 连接所需数据库,ScrapyChina为数据库名
        db = client['ScrapyChina']
        # 连接所用集合，也就是我们通常所说的表，mingyan为表名
        self.post = db['tianqi']
    def process_item(self, item, spider):
        dic = dict(item)# 把item转化成字典形式
        city = dic['city']
        self.post.update({'city':f'{city}'},{'$set':dic},upsert=True)#匹配主键city如果存在则更新数据、否者向数据库插入一条记录
        return item#会在控制台输出原item数据，可以选择不写
