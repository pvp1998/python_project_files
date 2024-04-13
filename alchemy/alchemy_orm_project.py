from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select


print("Welcome to your password manager")
task = int(input("Please press 1 for storing the passwords and 2 for retriving the password: "))

if task == 1:
    website = str(input("Enter the website: "))
    email = str(input("Enter the email: "))
    password = str(input("Enter the password: "))

    engine = create_engine("sqlite+pysqlite:///movies_db.db")
    session = Session(engine)
    Base = declarative_base()

    class Details(Base):
        __tablename__ = "passwords"

        id = Column(Integer, primary_key=True, autoincrement=True)
        website = Column(String)
        email = Column(String)
        password = Column(String)

    Base.metadata.create_all(engine)
    session.commit()

    details = Details(website=website, email=email, password=password)
    session.add(details)
    print("Details stored successfully")
    session.commit()
    session.close()
else:
    website = str(input("Enter the website: "))
    email = str(input("Enter the email: "))

    engine = create_engine("sqlite+pysqlite:///movies_db.db")
    session = Session(engine)
    Base = declarative_base()

    class Details(Base):
        __tablename__ = "passwords"

        id = Column(Integer, primary_key=True, autoincrement=True)
        website = Column(String)
        email = Column(String)
        password = Column(String)


    Base.metadata.create_all(engine)
    session.commit()

    state = select(Details.password).where(Details.email == email)

    result = session.execute(statement=state).scalar_one()
    print(result)
    session.commit()
    session.close()






