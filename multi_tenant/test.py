import datetime
import mysql.connector



cnx = mysql.connector.connect(user='admin', password="cmpe281#2017", host="cmpe281.cotowvf3a27g.us-west-2.rds.amazonaws.com", database='cmpe281')
cursor = cnx.cursor()

query = ("select * from TENANT_DATA where TENANT_ID = 'Tenant4' order by RECORD_ID desc LIMIT 1")

cursor.execute(query)

c = next(cursor)
print (c)

cursor.close()
cnx.close()
