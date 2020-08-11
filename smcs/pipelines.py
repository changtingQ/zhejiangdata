# -*- coding: utf-8 -*-
import psycopg2
from smcs.settings import pg_config, redis_config
from util.pygresql import PgSQL
import redis
from scrapy.exceptions import DropItem

Redis = redis.StrictRedis(host=redis_config["r_host"],
                          port=redis_config["r_port"],
                          db=redis_config["r_db"],
                          password=redis_config["r_pd"])


class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if Redis.exists('license_key: %s' % item["license_key"]):
            print(item["license_key"])
            raise DropItem
        else:
            Redis.set('license_key: %s' % item["license_key"], 1)
            return item


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
