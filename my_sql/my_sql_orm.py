from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.orm import declarative_base

password = "vidya"

engine = create_engine(f'mysql+mysqlconnector://vidya:{password}@localhost:3306/hr', echo=True)
session = Session(engine)
results = session.execute(text("select * from employees"))
print(results.fetchall())
Base = declarative_base()


class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = {"schema": "hr"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    position = Column(String(50))

class Courses(Base):
    __tablename__ = 'courses'
    __table_args__ = {"schema":"hr"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey('hr.employees.id'))
    course = Column(String(50))
    emp = relationship('Employees')


def add_details(name, position, course, session):
    new_user = Employees(name=name, position=position)
    session.add(new_user)
    query = select(Employees.id).where(Employees.name == name)
    user_id = session.scalar(query)
    new_course = Courses(emp_id=user_id, course=course)
    session.add(new_course)




Base.metadata.create_all(engine)
add_details("rajeeva","junior data engineer", "apache spark", session)
session.commit()
session.close()
