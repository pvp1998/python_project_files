import sqlalchemy
from sqlalchemy import *

engine = create_engine("sqlite+pysqlite:///:memory:")
connect = engine.connect()
results = connect.execute(text("SELECT 'Hello World"))


