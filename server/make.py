from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

# 创建对象的基类:
Base = declarative_base()


# 定义Key对象:
class Key_data(Base):
    # 表的名字:
    __tablename__ = 'keys'

    # 表的结构:
    keyname = Column(String(50),unique=True,primary_key=True)
    keytime = Column(String(10))

    def __repr__(self):

        return "{name}!{time}".format(name=self.keyname\
            ,time=self.keytime)


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


# 初始化数据库连接:
engine = create_engine('sqlite:///test.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

#创建表
Base.metadata.create_all(engine)

uidlist = ['1297580e-8613-42c1-8432-cf1da93cc575', '162afa3b-1f6e-411f-b701-3235d54aa600', '693051a3-de09-430a-8614-eaeacedb7dc6', 'aef59362-c548-49f9-9539-4de2e1e8fcbb', '5b47c08d-c143-43de-b5e2-ab93e2a95acc', 'ec1ea4c2-2dfd-44ff-a551-9cb2d4993b3b', '1e866b34-0969-4ce8-97fd-89e08895e610', '93179148-0cb0-456e-a797-19756aa0756e', '957ebe06-a05b-4c86-bb39-1e8b2b2ff016', '9c494e9b-8ad3-486a-b94e-31af0123d15d', '3bf83e35-9d36-4979-84de-1b54485236bc', 'b7c29e9c-ecb3-4487-9a6f-5321724edcc4', '7e67b79b-f69d-4ac9-86fe-ff6899f40afd', '30fe30c7-b62b-4d80-8df5-18f718dbfe22', '04705128-556c-49a2-8e76-73a81c13b46f', '687fbf03-9949-4eb3-a68c-8c7b4eeb8fe9', 'b85eae75-5326-4f1a-8224-a36f49e4f1b4', '2812bc45-98b9-4a51-a18a-6d60efc3e0e2', '8171869f-84b3-4176-9aa4-0e9bfe496ff5', '302a4810-c4e3-4967-8edf-cc89ce42f7a0', 'e62db391-9475-4fba-b843-13c5cdfd064e', '6cb7bbf9-9703-4ace-a093-75ebe74f9b2a', '814580bc-852a-47a6-94a1-891bdb85748a', 'c2b5adc0-b52f-403b-b854-1ae9d368bb87', '5d858126-fc82-4016-beee-995f7a011f74', 'a838e75c-5edc-4e16-a66a-ad31c091a09c', '5c974c9f-8e2a-40ed-8a83-8fdd10a3d7d1', 'a359da75-25ae-4fd5-9c30-726ec544341a', '1b47ca88-9e2a-4c9c-b0e4-d9804b4eec49', '3fb18f26-44e9-47e0-920d-995752d483ee']

for x in uidlist:

    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = Key_data(keyname = x,keytime = "30")
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
# 关闭session:
session.close()


