import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, insert, Select

engine = create_engine("sqlite+pysqlite:///movies_db.db")
connect = engine.connect()
# connect.execute(text("create table if not exists alchemy(x int, y int)"))
# #connect.execute(text("insert into alchemy values(:x, :y)"), ({'x': 3, 'y':4}, {"x": 5, "y": 6}))
# results = connect.execute(text("select * from alchemy"))


metadata_object = MetaData()

user_table = Table("user_account",
                   metadata_object,
                   Column("id", Integer, primary_key=True),
                    Column("name", String(20)),
                    Column("fullname", String))


address_table = Table("address",
                      metadata_object,
                      Column("id", Integer, primary_key=True),
                      Column("user_id", ForeignKey("user_account.id")),
                      Column("email", String, nullable=False))

metadata_object.create_all(engine)

#statement = insert(user_table).values(id=1,name="vidya",fullname="vidya prakash peram")
#connect.execute(statement)
connect.commit()
select_statement = Select(user_table.c.id)
print(connect.execute(select_statement).fetchall())
connect.close()