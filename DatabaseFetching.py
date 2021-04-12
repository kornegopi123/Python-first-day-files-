import mysql.connector

def verifyUser(uid,passw):
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="python")
    cursor=mydb.cursor()
    cursor.execute("SELECT passw FROM users WHERE userid = '"+uid+"'")
    infor=cursor.fetchone()
    #print("database data",infor)
    if(infor!=None):
        if(passw==infor[0]):
            return True
        else:
            return False
    else:
        return False
        
    
print(verifyUser("gopi","9908"))
print(verifyUser("gopi","9907"))

