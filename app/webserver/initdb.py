from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, BLOB, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#  sqlite:///:memory: (or, sqlite://)
#  sqlite:///relative/path/to/file.db
#  sqlite:////absolute/path/to/file.db
# sqlite for testing... [TODO]
engine = create_engine('sqlite:////tmp/tmpdb.sql')

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

password123_hash = "bed4efa1d4fdbd954bd3705d6a2a78270ec9a52ecfbfb010c61862af5c76af1761ffeb1aef6aca1bf5d02b3781aa854fabd2b69c790de74e17ecfec3cb6ac4bf"
user_hulto = User(fname='Jack McKenna', \
    uname='hulto', \
    passwd=password123_hash, \
    role=0)
user_oneeyed = User(fname='Jacob Ruud', \
    uname='oneeyedgrape', \
    passwd=password123_hash, \
    role=0)


if __name__ == "__main__":
    session.add(user_hulto)
    session.add(user_oneeyed)

    session.commit()



# Query
# query = session.query(User)

# instance = query.all()

# for i in instance:
#     print(i.uname)

# message = Message(message="Hello World!")
# session.add(message)
# session.commit()

# query = session.query(Message)
# instance = query.first()
# print (instance.message) # Hello World!



