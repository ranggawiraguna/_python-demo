import pymysql

db = pymysql.connect("localhost","root","")
cursor = db.cursor()

while True :
    try :
        cursor.execute(input("[mysql]> "))
        desc = cursor.fetchall()
        for row in desc :
            for column in row :
                print(column,end='')
            print()
        db.commit()

    except :
        db.rollback()

    print()