#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import pymysql as p,cgitb
cgitb.enable()

conn=p.connect(host="localhost",user="root",password="",database="empdb")
cur=conn.cursor()

q="""create database empdb"""
# cur.execute(q)


q=""" create table tabei(id int AUTO_INCREMENT PRIMARY KEY,
empid bigint(6),name varchar(50),dob int(50),gender varchar(50),mailid varchar(100),address varchar(100),phnno bigint(12)salary varchar(250),profile varchar(250)"""
cur.execute(q)

print("""
<script>
window.alert('database created');
</script>
""")
conn.close()