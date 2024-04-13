from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

engine = create_engine("sqlite+pysqlite:///movies_db.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    email_address = Column(String)

Base.metadata.create_all(engine)
session.commit()

# new_user = User(id=1, name='vidya', fullname="vidyaprakashperam")
#
# session.add(new_user)
state = select(User)
result = session.execute(state).scalar_one()
print(result.id)

