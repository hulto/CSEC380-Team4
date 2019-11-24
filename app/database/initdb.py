from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, BLOB, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('sqlite://')

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    fname = Column(String, nullable=False)
    uname = Column(String, nullable=False, unique=True)
    passwd = Column(String(128), nullable=False)
    role = Column(Integer, nullable=False)

class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(BLOB, nullable=False)
    description = Column(String, nullable=False)
    timestamp = Column(Date, nullable=False)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)
    views = Column(Integer,nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    timestamp = Column(Date, nullable=False)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)
    video = Column(Integer, ForeignKey('video.id'), nullable=False)

Base.metadata.create_all(engine)

password123_hash = "793e284dda1f551ebe0cb9f1dab48effa2a0ad8660cb489b445936b9ffd812a0b8f46bca66dd549fea530ce0114badc30a132fe819ad486f3952233427db488c"
user_hulto = User(fname='Jack McKenna', \
    uname='hulto', \
    passwd=password123_hash, \
    role=0)
user_oneeyed = User(fname='Jacob Ruud', \
    uname='oneeyedgrape', \
    passwd=password123_hash, \
    role=0)

session.add(user_hulto)
session.add(user_oneeyed)

session.commit()



# Query
query = session.query(User)

instance = query.all()

for i in instance:
    print(i.uname)

# message = Message(message="Hello World!")
# session.add(message)
# session.commit()

# query = session.query(Message)
# instance = query.first()
# print (instance.message) # Hello World!



