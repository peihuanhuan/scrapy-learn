# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from HelloScrapy.items import HelloscrapyItem
from HelloScrapy.mysqlpiplines.sql import Sql


class HelloscrapyPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,HelloscrapyItem):
            title=item['title']
            ret=Sql.select_book_title(title)
            if ret[0]==1:
                print("已经存在")
            else:
                author=item['author']
                link=item['link']
                collect=item['collect']
                Sql.insert_book(title,author,link,collect)
        return item

