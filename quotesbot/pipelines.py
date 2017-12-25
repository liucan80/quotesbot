# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class QuotesbotPipeline(object):
    #爬虫启动时执行此函数
    def open_spider(self,spider):
        #创建数据库和数据表
        self.db=sqlite3.connect("test.db")
        self.c=self.db.cursor()
        
        self.c.execute('drop table if exists down')
        self.c.execute('create table if not exists down (text text,author text,authorlink text,tags text )')
    #爬虫结束时执行此函数
    def close_spider(self,spider):
        #关闭数据库连接
        self.db.close()
        
    def process_item(self, item, spider):
        #将引擎传来的item数据导出到数据库 
        self.c.execute('insert into down values(?,?,?,?)',(item['text'],item['author'],item['authorlink'],item['tags']))
        self.db.commit()
        #print(item)
        return item
