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


# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = Key_data(keyname = "qaz",keytime = "30")
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
