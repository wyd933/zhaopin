# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
import codecs
import json

class ZhaopinPipeline(object):
    def __init__(self):
#        self.file = codecs.open('mydata.json', 'w', encoding='utf-8')
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['myspider']
        self.coll = self.db['mytest']


    def process_item(self, item, spider):
#        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
#        self.file.write(lines)
        self.coll.insert_one(dict(item))
        return item

    def close_spider(self, spider):
#        self.file.close()
        pass
