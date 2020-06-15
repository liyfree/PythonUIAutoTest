#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time:2020/6/13 20:55
# @Author:李阳
import os

import pymysql

from common.utils.config import Config, BASE_PATH

conf_file = os.path.join(BASE_PATH, 'data', 'database.yaml')


class DataBase():
    ''' 定义一个 MySQL 操作类'''

    def __init__(self):
        '''初始化数据库信息并创建数据库连接'''
        self.conf = Config(conf_file)
        self.connect = pymysql.connect(
            host=self.conf.get('database').get('host'),
            user=self.conf.get('database').get('user'),
            passwd=str(self.conf.get('database').get('password')),
            db=self.conf.get('database').get('db_name'),
            port=self.conf.get('database').get('port')
        )

    def insertDB(self, sql):
        ''' 插入数据库操作 '''

        self.cursor = self.connect.cursor()

        try:
            # 执行sql
            count = self.cursor.execute(sql)
            self.connect.commit()
        except:
            # 发生错误时回滚
            self.connect.rollback()
        finally:
            self.cursor.close()
        return count

    def deleteDB(self, sql):
        ''' 操作数据库数据删除 '''
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            count = self.cursor.execute(sql)
            self.connect.commit()
        except:
            self.connect.rollback()
        finally:
            self.cursor.close()
        return count

    def updateDb(self, sql):
        ''' 更新数据库操作 '''

        self.cursor = self.connect.cursor()

        try:
            # 执行sql
            count = self.cursor.execute(sql)
            self.connect.commit()
        except:
            # 发生错误时回滚
            self.connect.rollback()
        finally:
            self.cursor.close()
        return count

    def selectDb(self, sql):
        ''' 数据库查询 '''
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall()  # 返回所有记录列表

            # 结果遍历
            # for row in data:
            #     sid = row[0]
            #     name = row[1]
            #     # 遍历打印结果
            #     print('sid = %s,  name = %s' % (sid, name))
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()
        return data

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.connect.close()


if __name__ == '__main__':
    db = DataBase()
    c = db.selectDb('select * from user')
    print(c)
    db.closeDb()
