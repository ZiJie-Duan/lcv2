from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
    nameid = Column(String(50),unique=True,primary_key=True)
    due = Column(String(20))
    otime = Column(String(20))
    x = Column(String(20))


    def __repr__(self):

        return "{nameid}!{due}!{otime}!{x}".format(nameid=self.nameid\
            ,due=self.due,otime=self.otime,x=self.x)



# 初始化数据库连接:
engine = create_engine('sqlite:///test.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

#创建表
#Base.metadata.create_all(engine)

# 创建session对象:
session = DBSession()

'''


#删除数据库项
a = session.query(Key_data)\
    .filter_by(keyname="114dfa91-a8b7-4512-b7a3-3f9db7f33c8f").first()

session.delete(a)



a = session.query(Key_data)\
    .filter_by(keyname="114dfa91-a8b7-4512-b7a3-3f9db7f33c8f").first()

if a == [] :
    print("yes")


#查询语句
a = session.query(User_data)\
    .filter_by(nameid="815a580e-d00c-4923-81ca-64618ef35b4e").first()



# 创建新User对象:
new_user = Key_data(keyname="114dfa91-a8b7-4512-b7a3-3f9db7f33c8f",keytime=60)
new_user2 = User_data(nameid="815a580e-d00c-4923-81ca-64618ef35b4e"\
    ,due="20002",otime="2001",x="0")


# 添加到session:
session.add(new_user)
session.add(new_user2)
'''

# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()