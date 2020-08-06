# -*- coding: utf-8 -*-
import psycopg2
from smcs.settings import pg_config
from util.pygresql import PgSQL


class SmcsPipeline(PgSQL):
    # 保存数据
    def __init__(self):
        super().__init__()

    def open_spider(self, spider):
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        self.insert(self.table, item)
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
