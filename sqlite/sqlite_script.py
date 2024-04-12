import csv
import sqlite3

connect = sqlite3.connect("movies_db.db")
cur = connect.cursor()
# cur.execute("DROP TABLE if exists population")
cur.execute("CREATE TABLE if not exists population(city, state, population)")
# #
csvfile = open('/Users/vidyaprakashperam/Downloads/CSVtoSQLite/population_data.csv')
results = csv.reader(csvfile)
results.__next__()
#
for row in results:
    if row[1] not in list(cur.execute("SELECT city from population").fetchall()):
        cur.execute("INSERT INTO population values (?,?,?)", row)
#
#
# #
# # # cur.executemany("INSERT INTO population values (?,?,?)", results)
# # #
connect.commit()
# # #
print(cur.execute("SELECT city from population").fetchall())
# # #
connect.close()
