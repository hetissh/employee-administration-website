#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi
import pymysql as p, cgitb

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="dbfirst")
cur = conn.cursor()

f = cgi.FieldStorage()
uid = f.getvalue("u")
q = """select * from tabsi"""
cur.execute(q)
r = cur.fetchall()
# print(r)
print("""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Student details</title>
    <link rel="icon" type="text/ico" href="file/download.jpg">
  <style>
  img{border-radius:50%;}
  table,th,td{border:1px solid blue; padding:20px;}
  th{background-color:#96d4d4;}
  td{background-color:#b2beb5;color:blue;font-weight:bold;}
  </style>  
  <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>

</head>

<body>
 <center> <h2>Student details</h2>
      <table>
      <tr><th> S.No.</th><th>Profile</th><th>Name</th><th>DOB</th><th>Contact no</th><th>Mail id</th><th>password</th><th>Change</th><th>Delete</th></tr>""")
cnt = 0
for i in r:
    cnt = cnt + 1
    f = "files/" + i[6]
    print("""
    <tr><td>%s</td><td><img src="%s" height="50" width="50"></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
    <td><a href="adminupdate.py?u=%s"><i class='fas fa-edit' style='font-size:24px'></i></a></td>
    <td><a href="adminremove.py?u=%s"><i class='fas fa-trash' style='font-size:24px;color:red'></i></a></td></tr>
    """ % (cnt, f, i[1], i[2], i[3], i[4], i[5], i[0], i[0]))

print("""

      </table>
      <a href="admindashboard.py">Home </a>
    </center>
    </body>
    </html>


""")