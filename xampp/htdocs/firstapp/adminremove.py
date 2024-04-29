#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")


import cgi
import pymysql as p,cgitb
cgitb.enable()

conn=p.connect(host="localhost",user="root",password="",database="dbfirst")
cur=conn.cursor()

f=cgi.FieldStorage()
uid=f.getvalue("u")
q="""delete from tabsi where RegNo=%s"""%(uid)
cur.execute(q)
conn.commit()
conn.close()
print("""
<script>
window.alert('Record removed');
location.href = "adminview.py";
</script>
""")