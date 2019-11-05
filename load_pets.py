import sqlite3 as lite

conn = lite.connect('pets.db')
csr = conn.cursor()

Person=((1,'James','Smith',41),
        (2,'Diana','Greene',23),
        (3,'Sara','White',27),
        (4,'William','Gibson',23))

Pet = ((1,'Rusty','Dalmation',4,1),
      (2,'Bella','AlaskanMalamute',3,0),
      (3,'Max','CockerSpaniel',1,0),
      (4,'Rocky','Beagle',7,0),
      (5,'Rufus','CockerSpaniel',1,0),
      (6,'Spot','Bloodhound',2,1))

Person_Pet = ((1,1),(1,2),(2,3),(2,4),(3,5),(4,6))


def create_table():
    csr.execute(" CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT, age INTEGER)")
    csr.execute("CREATE TABLE IF NOT EXISTS pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT,  age INTEGER, dead INTEGER)")
    csr.execute("CREATE TABLE IF NOT EXISTS person_pet(person_id INTEGER, pet_id INTEGER)")
    conn.commit()

def load_data():
    csr.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", Person)
    csr.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", Pet)
    csr.executemany("INSERT INTO person_pet VALUES(?, ?)", Person_Pet)
    conn.commit()

create_table()
load_data()    