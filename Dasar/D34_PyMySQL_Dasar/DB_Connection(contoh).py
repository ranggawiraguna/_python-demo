import pymysql

db = object()
cursor = object()

def createConnection(server="localhost", user="root", password="") :
    global db

    db = pymysql.connect(server, user, password)

def createCursor() :
    global db
    global cursor

    cursor = db.cursor()

def executeQuery(sql) :

    try:
        cursor.execute(sql)
        db.commit()

        data = cursor.fetchall()
        if type(data) is type(tuple()) :
            for row in range(len(data)) :
                for column in data[row] :
                    print("\t\t", str(row+1)+".", column)

        print("\n\t\t [>]Query OK ")

    except Exception as e:
        db.rollback()
        print("\t\t {}".format(e))

    finally:
        db.close()


if __name__ == '__main__':
    while True :
        createConnection()
        createCursor()
        executeQuery(input("[query]> "))
        db.commit()
        print()