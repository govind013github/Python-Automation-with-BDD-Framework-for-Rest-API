import mysql.connector
from utilities.configurations import *

# host, database,user, password
#conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                              user='root', password='Govind@013')

conn = getConnection()
print(conn.is_connected())
cursors = conn.cursor()
cursors.execute('SELECT * FROM apidevelop.customerinfo')
# row = cursors.fetchone()
# print(row)
# print(row[3])    # prints 3rd index here from tuple as, Note - mysql output is in form of tuple.
# rowAll = cursors.fetchall()
# print(rowAll)    # return list of tuples here.

# Q. Print sum of Amount column
rows = cursors.fetchall()
print(type(rows))
print(rows)
sums = 0
for row in rows:  # ('selenium', datetime.date(2024, 3, 31), 120, 'Africa')
    sums = sums + row[2]

print(sums)


query = "update apidevelop.customerinfo set Location = %s WHERE CourseName = %s"
data = ("IN", "Appium")
cursors.execute(query, data)
conn.commit()



conn.close()
