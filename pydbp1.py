#!/usr/local/bin/python3.8

import pymysql
db = pymysql.connect('localhost','root','','classicmodels')
cursor = db.cursor()

cursor.execute('SELECT customerName FROM customers')
data = cursor.fetchone()
print ('customer is : %s ' % data)

cursor.execute('SELECT customerName FROM customers')
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.execute('SELECT * FROM customers')
for row in cursor:
    print(row)

db.close()