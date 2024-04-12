import sqlite3

def password_pusher():
    print("Welcome to your password manager!")
    website = str(input("Enter the website: "))
    email = str(input("Enter your email address: "))
    password = str(input("Enter your password: "))


    def insert_details(website, email, password):
        details = ({
            "website": website.lower(),
            "email": email.lower(),
            "password": password.lower()
        })
        connect = sqlite3.connect("movies_db.db")
        curr = connect.cursor()
        curr.execute("create table if not exists creds(website, email, password)")
        curr.execute("insert into creds values (:website, :email, :password)", details)
        connect.commit()
        connect.close()


    if website is not None and email is not None and password is not None:
        print(insert_details(website, email, password))
    else:
        print("Please enter the details correctly")

def password_verifier():
    print("Welcome to your password manager!")
    website = input("Enter the website: ")
    email = input("Enter your email address: ")

    def fetch_details(website, email):
        details = ({
            "website": website,
            "email": email
        })
        connect = sqlite3.connect("movies_db.db")
        curr = connect.cursor()
        curr.execute("create table if not exists creds(website, email, password)")
        print(curr.execute("select * from creds where website = :website and email = :email,)", details).fetchone())
        connect.commit()
        connect.close()


password_verifier()
