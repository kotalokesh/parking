# neccesary mysql database code to store the data in database
import mysql.connector
mydb = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = '1111',
    database = 'parking'
)
print(mydb)
mycursor = mydb.cursor()


def enter(slotid):
    b = slotid
    try:
        sql = "update Slot set status = %s where slotid = %s "
        val = ("no", b)
        mycursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.errors.ProgrammingError or mysql.connector.IntegrityError as e:
        print(e)
        print("fail to access the database")


def vechileenter(Vechile, slotid):
    try:
        sql1 = "insert into Vechile (type,number,name,slotno) values (%s,%s,%s,%s)"
        val1 = (Vechile.type, Vechile.number, Vechile.name, slotid)
        mycursor.execute(sql1, val1)
        sql2 = "update Slot set status = %s where slotid = %s "
        val2 = ("no", slotid)
        mycursor.execute(sql2, val2)
        mydb.commit()
    except mysql.connector.errors.ProgrammingError or mysql.connector.IntegrityError as e:
        print(e)
        print("fail to access the database")


def exit(slotid):
    b = slotid
    try:
        sql = "update Slot set status = %s where slotid = %s "
        val = ("yes", b)
        mycursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.errors.ProgrammingError or mysql.connector.IntegrityError as e:
        print(e)
        print("fail to access the database")

def vechileexit(number):
    try:
        sql = "update Vechile set status = %s where number = %s"
        val = ("deactive",number)
        mycursor.execute(sql,val)
        mydb.commit()
    except mysql.connector.errors.ProgrammingError or mysql.connector.IntegrityError as e:
        print(e)
        print("fail to access the database")