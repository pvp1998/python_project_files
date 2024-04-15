# 1. Create department table
# 2. Add department_id column to the employees
# 3. Set employees department_id as foreign key to the department table
# 4. Insert department_id values to the department table
# 4. Update department_id columns of the employees table based on the department table

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
    room_id = Column(Integer, ForeignKey("hr.rooms.id"))
    rel = relationship('Rooms')

class Courses(Base):
    __tablename__ = 'courses'
    __table_args__ = {"schema":"hr"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey('hr.employees.id'))
    course = Column(String(50))
    emp = relationship('Employees')

class Rooms(Base):
    __tablename__ = 'rooms'
    __table_args__ = {"schema":"hr"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    room = Column(Integer)

Base.metadata.create_all(engine)
# rooms = [704, 507]
# for r in rooms:
#     details = Rooms(room=r)
#     session.add(details)

first_query = select(Rooms.id).where(Rooms.room == 704)
first_room = session.scalar(first_query)
second_query = select(Rooms.id).where(Rooms.room == 507)
second_room = session.scalar(second_query)
print(f'{first_room}, {second_room}')
#
first_room_mates = ['vidya', 'mahesh', 'rajeeva']
second_room_mates = ['bharath', 'nomesh', 'sameer']
#
# for mates in first_room_mates:
#     update_query = update(Employees).where(Employees.name == mates).values(Employees.room_id = first_room)
#     session.execute(update_query)
#
# for mates in second_room_mates:
#     update_query = update(Employees).where(Employees.name == mates).values(Employees.room_id = second_room)
#     session.execute(update_query)

res = session.query(Employees).all()
for i in res:
    if i.name in first_room_mates:
        i.room_id = first_room
    elif i.name in second_room_mates:
        i.room_id = second_room

session.commit()
session.close()

