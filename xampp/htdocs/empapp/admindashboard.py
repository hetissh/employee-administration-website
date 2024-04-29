#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi, cgitb, pymysql as p

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

f=cgi.FieldStorage()
uid=f.getvalue("u")
q="""select * from tabei where id=%s"""%(uid)
cur.execute(q)
r=cur.fetchone()

print("""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Admin</title>
    <link rel="icon" type="text/ico" href="file/flower.jpg">

</head>
<body>
 <h2>WELCOME ADMIN</h2>
       <h2> <a href="adminview.py" <h2>View Employees<h2></a>
    <a href="index.py" <h2>Logout<h2></a></h2>

    </body>
    </html>

""")