# -*-coding:utf8-*-#
# '''
# copyright:2017
# author:
# module:数据库操作
# '''

import mysql.connector
import configparser


class Database:
    user = ''
    password = ''
    host = ''
    port = ''
    dataname = ''

    def __init__(self):
        try:
            config = configparser.ConfigParser()
            config.read('param.conf')
            self.user = config.get('database', 'user')
            self.password = config.get('database', 'password')
            self.host = config.get('database', 'host')
            self.port = config.get('database', 'port')
            self.dataname = config.get('database', 'database')
        except:
            user = ''
            password = ''
            host = ''
            port = ''
            dataname = ''

    #查询数据
    def ExecSelect(self, sql, param):
        cnx = mysql.connector.Connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.dataname)
        try:
            cur = cnx.cursor()
            cur.execute(sql, param)
            columns = [desc[0] for desc in cur.description]
            ret = []
            for row in cur.fetchall():
                row = dict(zip(columns, row))
                ret.append(row)
            cur.close()
            cnx.close()
            return ret
        except:
            cnx.close()
            return []

    #增加数据
    def ExecInsert(self, sql, param):
        cnx = mysql.connector.Connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.dataname)
        try:
            cur = cnx.cursor()
            cur.execute(sql, param)
            cnx.commit()
            cur.close()
            cnx.close()
            return 1
        except Exception as er:
            cnx.close()
            return 0

    #更新数据
    def ExecUpdate(self, sql, param):
        cnx = mysql.connector.Connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.dataname)
        try:
            cur = cnx.cursor()
            cur.execute(sql, param)
            cnx.commit()
            cur.close()
            cnx.close()
            return 1
        except Exception as er:
            print(str(er))
            cnx.close()
            return 0

    #删除数据
    def ExecDelete(self, sql, param):
        cnx = mysql.connector.Connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.dataname)
        try:
            cur = cnx.cursor()
            cur.execute(sql, param)
            cnx.commit()
            cur.close()
            cnx.close()
            return 1
        except:
            cnx.close()
