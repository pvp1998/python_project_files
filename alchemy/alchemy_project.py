import sqlalchemy
from sqlalchemy import *

print('Welcome to your password manager')
website = str(input("Enter your website: "))
email = str(input("Enter your email: "))
password = str(input("Enter your password: "))

if website is not None and email is not None and password is not None:
    engine = create_engine("sqlite+pysqlite:///movies_db.db")
    connection = engine.connect()
    connection.execute(text("create table if not exists creds(website string, email string, password string)"))
    info = [
        {"website": website.lower()},
        {"email": email.lower()},
        {"password": password.lower()}
    ]
    connection.execute(text("insert into creds values(:website, :email, :password)"), info)
    connection.commit()
    print(connection.execute(text("select * from creds")).fetchall())
else:
    print("Enter the details properly")

