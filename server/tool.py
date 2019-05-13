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

    uidlist = [['5b6a1ce4-18cc-4d08-bc1a-e1128c7f54f9', '30'], ['272fdb99-45ad-4840-96e6-6986f9cfdb84', '30'], ['985ba507-239a-405e-a1a2-f37427a46dae', '30'], ['efd04a61-c610-4306-bc49-0a2b743d6b23', '30'], ['bc6e4366-7087-4292-bf36-bc197c86fe4a', '30'], ['cc6df595-61f7-4021-a6a2-2a182c86a17e', '30'], ['4d2793a5-b8ab-47b8-8d8f-38e78f836d3f', '30'], ['b734cdbf-32bd-440f-bd28-070323c8f1aa', '30'], ['7629f74f-c3f0-40a4-9d0d-738e192c6611', '30'], ['0dc258e6-3f30-4148-adb9-8319aef9ed3f', '30'], ['8ac25146-f411-4de5-9ad5-5e26c4bbbd4f', '30'], ['eba7683c-b4e5-45ea-bf61-df37275ef9e2', '30'], ['7038410d-103a-4418-8a77-35b8ab022726', '30'], ['3e20cd1e-1969-465e-a83a-9eaa7c3ec3c3', '30'], ['2f138a65-dd40-4833-ab30-7e4312a5d7e2', '30'], ['11b42a4d-6e49-4c05-adf2-5a100c945d7d', '30'], ['8925422b-edc7-4088-87ce-83a20211e147', '30'], ['70bcdc17-d0cb-4eb1-bb29-c99e1859620f', '30'], ['56fdf502-6977-473f-b715-7a0f1f58681b', '30'], ['38d47141-f198-43eb-929c-ec48d754fc34', '30'], ['e4a2aaf7-8b79-4d5f-9e5b-6735c502f3ac', '30'], ['4b9bc240-5fa7-4c85-b0fc-c04fe5fde68a', '30'], ['2e730fa4-bc3d-4eef-a29d-22e7b82c83a4', '30'], ['1c00e553-26a1-4ee1-9483-64ce47916e02', '30'], ['b92dd53a-a898-4b43-b47e-d71f13cfd417', '30'], ['348b9bcb-2f14-4ed9-be66-0416f3772c86', '30'], ['889054fc-35f8-40e5-ba60-a988a9422b73', '30'], ['40b69ca0-e7a4-4147-9386-5061b882a1ab', '30'], ['66a28896-1d55-4346-bffe-8d1f13ee13f6', '30'], ['64e9587b-44a6-4328-8595-034a6a3c1fb2', '30'], ['4d97c721-4478-424d-8722-3845861d30aa', '30'], ['f8c37db1-3510-48c7-bebd-62a8f2e19737', '30'], ['e0fed291-36e8-440b-a3ac-172c09b6b0a8', '30'], ['72b79a0b-3751-4e54-8399-6ca26527c1bd', '30'], ['c2a5ec0e-a80f-48ed-82e7-3b8edafefb05', '30'], ['35d06b0e-2783-4aae-a365-d4f7a9d6d131', '30'], ['4bc12a78-986e-4a6e-9f90-62a8b757dde8', '30'], ['ebfc9784-182b-417b-8391-88b4b6a50663', '30'], ['068dab7d-8bc4-4479-8688-7c62ba9bf9ab', '30'], ['7df5528f-3e63-462a-8de5-fe33e19ac0ba', '30'], ['29e49d41-2c06-47e2-8c30-b38969749500', '30'], ['bb4a8500-a220-4708-996a-b20a02880570', '30'], ['a570af6d-efc7-45d4-bda7-70a5bda902af', '30'], ['68562e4b-6ba7-4c75-b0ef-8515c9b2de6a', '30'], ['90686e2c-b506-4a36-a500-ad3ddf8ba77d', '30'], ['e01293bd-ebe5-4861-ba49-9d39ae159caf', '30'], ['a7696e2d-69a7-449b-971f-3c635bbcea63', '30'], ['fb26eea5-62e1-4417-a9df-41e6633bc4f0', '30'], ['2d04c22d-ec2b-4ec9-9ec8-3edf8e88d461', '30'], ['c225f721-fcef-41b0-8247-37c15d6e6998', '30'], ['873e140f-d1f2-449b-a4d1-d0f2c01d5682', '30'], ['74277af1-8f6c-4bc1-8a83-1c0150ad30ce', '30'], ['32c17c2a-cecd-4d7f-b9a4-23194eb97749', '30'], ['ed518692-6060-4d8c-a0cc-c674425b5876', '30'], ['f67e36c8-f6c4-4777-a794-fcf50e7f52f8', '30'], ['d35e5a19-6e9b-430c-bd5a-0a1a81147152', '30'], ['e5bcefbc-ef0a-4cd2-be19-4077a54604c7', '30'], ['2b980e57-129e-41a5-a694-b38ecaf0e3ed', '30'], ['dfc1b878-4fb4-4637-9e7b-836071d193c2', '30'], ['281f7142-8380-4001-b7d8-f4442c8c91cd', '30']]

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

