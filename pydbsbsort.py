#!/usr/local/bin/python3.8

import time
import pymysql
import cgi

html5top='''
<!-- {fname} -->
<!DOCTYPE html>
<html>
 <head>
  <title>{title}</title>
 </head>
 <body>
  <h1>{header}</h1>
'''
html5bottom='''
 </body>
</html>
'''
tableHeader='''
<table border=1>
<tr><th>Name</th><th>Address</th><th>Balance</th></tr>
'''

form = cgi.FieldStorage()
if 'sortBy' in form:
    sortBy = form[ 'sortBy' ].value
else:
    sortBy = 'name'
   
if 'sortOrder' in form:
    sortOrder = form[ 'sortOrder' ].value
else:
    sortOrder = 'ASC'   
   
print (html5top.format(fname='pydbsb.py',title='pymysql',header='Customer Table'))

connection = pymysql.connect(user='root',
                             password='',
                             db='simplebilling', 
                             cursorclass=pymysql.cursors.DictCursor)

print(tableHeader)
with connection.cursor() as cursor:
    cursor.execute('SELECT * from customers ORDER BY %s %s' %
                   ( sortBy, sortOrder ))
    allFields = cursor.description
    for e in cursor.fetchall():
        print ('<tr><td>'+e['name']+'</td>'+
               '<td>'+e['address']+'</td>'+
               '<td>'+str(e['balance'])+'</td></tr>')

print('</table>')
print('<hr>')

print ('''
      \n<form method = 'post' action = '/cgi-bin/pydbsbsort.py'>
      Sort By:<br />''')

for field in allFields:
    print ('''<input type = 'radio' name = 'sortBy'
      value = '%s' />''' % field[ 0 ])
    print (field[ 0 ])
    print ("<br />")

print ('''<br />\nSort Order:<br />
      <input type = 'radio' name = 'sortOrder'
      value = 'ASC' checked = 'checked' />
      Ascending
      <input type = 'radio' name = 'sortOrder'
      value = 'DESC' />
      Descending
      <br /><br />\n<input type = 'submit' value = 'SORT' />
      </form>\n\n</body>\n</html>''')
 

connection.close()
print (time.ctime( time.time() ))
print (html5bottom)


