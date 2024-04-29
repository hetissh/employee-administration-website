#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")


import cgi, cgitb, pymysql as p

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="dbfirst")
cur = conn.cursor()

f=cgi.FieldStorage()
uid=f.getvalue("u")
q="""select * from tabsi where RegNo=%s"""%(uid)
cur.execute(q)
r=cur.fetchone()
print("""
<h2>Welcome %s</h2>
"""%(r[1],))