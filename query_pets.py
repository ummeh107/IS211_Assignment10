import sqlite3 as lite

conn = lite.connect('pets.db')
csr = conn.cursor()

while True:
    person_id = (input("Enter person id or -1 for exit :"))
    if int(person_id) > 0:
        csr.execute("SELECT * from person inner join person_pet inner join pet on person.id=person_pet.person_id AND pet.id=person_pet.person_id where person.id=?", person_id)
        details = csr.fetchall()
        if len(details) > 0:
            print("{} {}, {} years old.".format(details[0][1],details[0][2],details[0][3]))
            for person in details:
                print("{} {} owned {}, a {}, that was {} years old"
                        .format(person[1], person[2], person[7], person[8].lower(), person[9]))                                    
                
        else:
            print("Cannot find that id!, Please enter valid id")
    elif person_id == '-1' :
        break
