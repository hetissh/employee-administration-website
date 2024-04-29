#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import pymysql as p,cgitb
cgitb.enable()

conn=p.connect(host="localhost",user="root",password="",database="dbfirst")
cur=conn.cursor()

q="""create database dbfirst"""
# cur.execute(q)

q=""" create table tabsi(RegNo int AUTO_INCREMENT PRIMARY KEY,name varchar(50),
ContactNo bigint(12),Mailid varchar(100),password varchar(50),profile varchar(250)"""
cur.execute(q)


print("""
<script>
window.alert('database created');
</script>
""")
conn.close()