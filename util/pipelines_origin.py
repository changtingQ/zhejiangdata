# -*- coding: utf-8 -*-
import psycopg2
from smcs.settings import pg_config
from util.pygresql import PgSQL


class SmcsPipeline(object):
    # 保存数据
    def __init__(self):
        self.host = pg_config['PG_HOST']
        self.user = pg_config['PG_USER']
        self.pwd = pg_config['PG_PWD']
        self.db = pg_config['PG_DB']
        self.port = int(pg_config['PG_PORT'])
        self.table = pg_config['PG_TABLE']
        self.conn = psycopg2.connect(host=self.host, user=self.user, password=self.pwd, dbname=self.db, port=self.port)

    def open_spider(self, spider):
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        
        print("sample_data------->")
        print(item)
        print(self.__class__)
        print("sample_data------->")
        keys = ', '.join(item.keys())
        values = ', '.join(item.values())
        print(values)
        sql = "insert into {0}({1}) values ({2})".format(self.table, keys, "'小红'， 3")
        print(sql)

        self.cur.execute(sql, tuple(item.values()))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
