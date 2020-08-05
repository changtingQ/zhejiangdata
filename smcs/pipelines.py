# -*- coding: utf-8 -*-
import psycopg2
from smcs import settings


class SmcsPipeline(object):
    def __init__(self):
        self.host = settings['PG_HOST']
        self.user = settings['PG_USER']
        self.pwd = settings['PG_PWD']
        self.db = settings['PG_DB']
        self.port = int(settings['PG_PORT'])
        self.table = settings['PG_TABLE']
        self.conn = psycopg2.connect(host=self.host, user=self.user,password=self.pwd, dbname=self.db, port=self.port)

    def open_spider(self, spider):
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into {0}({1}) values ({2})".format(self.table, ','.join(item.keys()), ','.join(['%s'] * len(item.fields.keys())))
        # print(tuple(item.values()))
        self.cur.execute(sql, tuple(item.values()))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
