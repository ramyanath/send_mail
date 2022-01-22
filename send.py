#!C:\Users\Public\python\python.exe

import cgi
# import mysql.connector
import smtplib
import pandas as pd
# data=cgi.FieldStorage()
# db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="test")
# cursor=db.cursor()

# sql="select email from table1"
# cursor.execute(sql)

# result=cursor.fetchall()
# db.commit()

e = pd.read_excel("Email.xlsx")
result = e['Emails'].values
SenderAddress = "ramyanathsgs@gmail.com"
password = "password"


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this mail is just for test purpose"
subject = "test mail"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in result:
    server.sendmail(SenderAddress, email, body)
server.quit()
