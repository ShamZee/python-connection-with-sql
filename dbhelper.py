import mysql.connector
import sys


class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="python_sql")
            self.mycursor = self.conn.cursor()
        except:
            print("some error occured could not connect to DB")
            sys.exit(0)
        else:
            print('Connected to DB')

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `user`(`id`,`name`,`email`,`password`) VALUES(NULL,'{}','{}','{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM user WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))

        data = self.mycursor.fetchall()
        return data