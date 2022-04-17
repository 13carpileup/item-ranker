import mysql.connector
#sample, obviously doesnt actually connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="x",
    database="x",

)
#database is formatted as follows:
#filename (varchar(255)) prim key, elo (int)


mycursor = mydb.cursor()
def updateElo(photo1,elo1,photo2,elo2):
    sql = "UPDATE elo SET elo = '%s' WHERE filename = '%s'"%(elo1,photo1)
    mycursor.execute(sql)
    sql = "UPDATE elo SET elo = '%s' WHERE filename = '%s'"%(elo2,photo2)
    mycursor.execute(sql)
    mydb.commit()

def fetchElo():
    mycursor.execute("SELECT * FROM elo")
    x=mycursor.fetchall()
    out={}
    for item in x:
        out[item[0]]=item[1]
    return(out)

