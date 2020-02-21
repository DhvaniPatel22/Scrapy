# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# class QuotetutorialPipeline(object):

#     def process_item(self, item, spider):
#         return item

# import scrapy
# import pymysql

# class QuotetutorialPipeline(object):

#     def __init__(self):
#         self.conn = pymysql.connect(host='localhost', user='my', password='', database='myquo', charset='utf8')
#         self.cursor = self.conn.cursor()
#         self.conn.autocommit(True)

#     def process_item(self, item, spider):
#         for i in range(3):
#             try:
#                 self.cursor.execute("""INSERT INTO `tablename` ( `title`, `author` , `tag` )
#                                 VALUES ( %s , %s , %s )  ON DUPLICATE KEY UPDATE title = title, author = author, tag = tag""",(item['title'].encode('utf8'), item["author"].encode('utf8'), item["tag"].encode('utf8'))
#                 )

#             except:
#                 continue
           
import pymysql

class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'my',
            #user = 'mn',
            #passwd = 'uebycLbapWAoPefu',
            passwd = '',
            database = 'myquo',
            #database = 'myv',
            charset='utf8'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                title text,
                author text,
                tag text
               
                
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
           

        ))

        self.conn.commit()



# import sqlite3

# class QuotetutorialPipeline(object):

#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#         # self.create_connection1()
#         # self.create_table1()
    
#     def create_connection(self):
#         self.conn = sqlite3.connect("myquotes.db")
#         self.curr = self.conn.cursor()

#     # def create_connection1(self):
#     #     self.conn = sqlite3.connect("author.db")
#     #     self.curr = self.conn.cursor()

#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
#         self.curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
                
#                 )""")

#     # def create_table1(self):
#     #     self.curr.execute("""DROP TABLE IF EXISTS author_tb""")
#     #     self.curr.execute("""create table author_tb(
#     #             name text,
#     #             birthdate text,
#     #             bio text
        
#     #             )""")

#     def process_item(self, item, spider):
#         self.store_db(item)
#         # self.store_db1(item)
#         return item

#     def store_db(self,item):
#         self.curr.execute("""insert into quotes_tb values (?,?,?)""", (
#             item['title'][0],
#             item['author'][0],
#             item['tag'][0]
            
#         ))
#         # self.curr.execute("""insert into author.db values (?,?,?)""", (
#         #     item['name'][0],
#         #     item['birthdate'][0],
#         #     item['bio'][0]
#         # ))
        
#         self.conn.commit()