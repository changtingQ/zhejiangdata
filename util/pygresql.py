# -*- coding: utf-8 -*-
import psycopg2

from smcs.settings import pg_config


class PgSQL(object):
    """docstring for mysql"""

    def __init__(self):
        self.host = pg_config['PG_HOST']
        self.user = pg_config['PG_USER']
        self.passwd = pg_config['PG_PWD']
        self.dbname = pg_config['PG_DB']
        self.port = int(pg_config['PG_PORT'])
        self.table = pg_config['PG_TABLE']
        self._connect()
        self.conn = psycopg2.connect(host=self.host, user=self.user, password=self.passwd, dbname=self.dbname,
                                     port=self.port)
        self._cursor = self.conn.cursor()

    def _connect(self):
        try:
            self._conn = psycopg2.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.passwd,
                                          dbname=self.dbname)
        except Exception as e:
            raise e

    def query(self, sql):
        try:
            # self._conn.ping(reconnect=True)
            result = self._cursor.execute(sql)
        except Exception as e:
            raise e
            result = False
        return result

    def select(self, table, column='*', condition='', offset=0, length=0):
        condition = ' where ' + condition if condition else None
        if condition:
            sql = "select %s from %s  %s" % (column, table, condition)
        else:
            sql = "select %s from %s" % (column, table)
        if offset >= 0 and length > 0:
            sql += " limit %s,%s " % (offset, length)
        self.query(sql)
        return self._cursor.fetchall()

    def findOne(self, table, column='*', condition='', p=None):
        condition = ' where ' + condition if condition else None
        if condition:
            sql = "select %s from %s  %s" % (column, table, condition)
        else:
            sql = "select %s from %s" % (column, table)
        if p is not None:
            print(sql)
            exit()
        self.query(sql)
        return self._cursor.fetchone()

    def fetchall(self, sql=''):
        self.query(sql)
        return self._cursor.fetchall()

    def fetchone(self, sql=''):
        self.query(sql)
        return self._cursor.fetchone()

    def insert(self, table, tdict):
        column = ''
        value = ''
        for key in tdict:
            column += ',' + key
            value += "','" + (tdict[key])
        column = column[1:]
        value = value[2:] + "'"
        sql = "insert into %s(%s) values(%s)" % (table, column, value)
        print(sql)
        self.query(sql)
        self.conn.commit()
        return self._cursor.lastrowid  # 返回最后的id

    def get_find_where(self, where, p=None):
        where_str = ''
        for where_vod_key, where_vod_val in where.items():
            if p is not None:
                where_str += 'and ' + " " + where_vod_key + " " + "=" + " '" + str(where_vod_val) + "' "
            else:
                where_str += 'and ' + " `" + where_vod_key + "` " + "=" + " '" + str(where_vod_val) + "' "
        where_str = where_str[3:]
        return where_str

    def update(self, table, tdict, condition='', p=None):
        if not condition:
            print("must have id")
            exit()
        else:
            condition = 'where ' + condition
        value = ''
        for key in tdict:
            new_key_str = str(tdict[key])
            new_key_str = new_key_str.replace('"', '')
            value += ",`%s`=\"%s\"" % (key, new_key_str)
        value = value[1:]
        sql = "update %s set %s %s" % (table, value, condition)
        if p is not None:
            print(sql)
            exit()
        self.query(sql)
        self._conn.commit()
        return self.affected_num()  # 返回受影响行数

    def delete(self, table, condition=''):
        condition = 'where ' + condition if condition else None
        sql = "delete from %s %s" % (table, condition)
        # print(sql)
        self.query(sql)
        self._conn.commit()
        return self.affected_num()  # 返回受影响行数

    def rollback(self):
        self._conn.rollback()

    def affected_num(self):
        return self._cursor.rowcount

    def __del__(self):
        try:
            self._cursor.close()
            self._conn.close()
        except:
            pass

    def close(self):
        self.__del__()
