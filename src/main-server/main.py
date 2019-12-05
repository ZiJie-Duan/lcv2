# -- coding:utf-8--
#this file set place in main server
import socket
import time
import datetime
import json
import os
import core
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random


# 创建对象的基类:
Base = declarative_base()


# 定义Key对象:
class Server_data(Base):
    # 表的名字:
    __tablename__ = 'servers'

    # 表的结构:
    name = Column(String(200),unique=True,primary_key=True)
    level = Column(String(10))

    def __repr__(self):

        return "{name}!{time}".format(name=self.name\
            ,time=self.level)


# 定义User对象:
class User_data(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    userid = Column(String(50),unique=True,primary_key=True)
    due = Column(String(20))
    otime = Column(String(20))

    def __repr__(self):

        return "{userid}!{due}!{otime}".format(userid=self.userid\
            ,due=self.due,otime=self.otime)


# 定义User对象:
class Config_data(Base):
    # 表的名字:
    __tablename__ = 'config'

    # 表的结构:
    ip = Column(String(50),unique=True,primary_key=True)
    uuid = Column(String(20))
    port = Column(String(20))

    def __repr__(self):

        return "{ip}!{uuid}!{port}".format(ip=self.ip\
            ,uuid=self.uuid,port=self.port)



# 初始化数据库连接:
engine = create_engine('sqlite:///test.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()


