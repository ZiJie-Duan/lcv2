

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



ml = input("创建服务器数据库（make）添加卡密（add）:")

if ml == "make":

    # 初始化数据库连接:
    engine = create_engine('sqlite:///test.db')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    #创建表
    Base.metadata.create_all(engine)

elif ml == "add":
    # 初始化数据库连接:
    engine = create_engine('sqlite:///test.db')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    keyname = input("卡密名称：")
    keytime = input("激活时间：")

    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = Key_data(keyname = keyname,keytime = keytime)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

elif ml == "x":

    # 初始化数据库连接:
    engine = create_engine('sqlite:///test.db')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    uidlist = [['d35e5a19-6e9b-430c-bd5a-0a1a81147152', '30'], ['e5bcefbc-ef0a-4cd2-be19-4077a54604c7', '30']]

    for x,y in uidlist:

        # 创建session对象:
        session = DBSession()
        # 创建新User对象:
        new_user = Key_data(keyname = x,keytime = y)
        # 添加到session:
        session.add(new_user)
        # 提交即保存到数据库:
        session.commit()
    # 关闭session:
    session.close()

