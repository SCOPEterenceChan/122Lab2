#!/usr/local/bin/python3.8

import pymysql
connection = pymysql.connect(user='root',
                             password='',
                             db='classicmodels', 
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    cursor.execute('SELECT customerName,phone,country from customers')
    for e in cursor.fetchall():
        print (e)
