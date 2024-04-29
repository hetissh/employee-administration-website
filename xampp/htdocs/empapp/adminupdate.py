#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi,os
import pymysql as p, cgitb

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

f = cgi.FieldStorage()
uid = f.getvalue("u")
q = """select * from tabei where id=%s"""%(uid)
cur.execute(q)
r = cur.fetchone()

print("""
      
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "icon" type="text/ico" href = "files/icn.png">
    <link rel="stylesheet" href="emps1.css">
    <title>Edit</title>
</head>
<body>
    <form action="#" class="login-form" enctype="multipart/form-data" method = "post" autocomplete = "off">
        <h1>Edit</h1>
        
    <center>
        
        <img src="%s" height ="50" width="50">
        
    </center>

    <div class="txtb">
    <label> Employee id : </label>
    <input type="number" name="empid" value ="%s" placeholder="Enter your employee id" read only /> <br> <br>
    </div>  

    <div class="txtb">
    <label> Name : </label>
    <input type="text" name="name" value ="%s" placeholder="Enter your name" required /> <br> <br>
    </div>  
    
    <div class="txtb">
    <label> Date of birth : </label>
    <input type="date" name="dob" value ="%s" placeholder="dd-mm-yyyy" required /> <br> <br>  
    </div>

    <div class="txtb">
    <label> Gender : </label>
    <input type="text" name="gender" value ="%s" placeholder="Enter your gender" required /> <br> <br>
    </div> 


    <div class="txtb">
    <label> Mail id : </label>
    <input type="email" name="mailid" value ="%s" placeholder="Enter your mail id" required /> <br> <br>  
    </div>

    <div class="txtb">
    <label> Address : </label>
    <input type="text" name="address" value ="%s" placeholder="Enter your address" required /> <br> <br>
    </div>

    <div class="txtb">
    <label> Phone number : </label>
    <input type="number" name="phnno" value ="%s" placeholder="Enter your contact number" required /> <br> <br>
    </div>
    
    <div class="txtb">
    <label> Salary : </label>
    <input type="number" name="salary" value ="%s" placeholder="Enter your name" required /> <br> <br>
    </div> 

    <div class="txtb">
        <input type="file" name = "profile" >
    </div>
    
    <input type="submit" class="subbtn" name = "sub" value="save">

    </form>

</body>
</html>
      
  """%("files/"+r[9], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))

sub = f.getvalue("sub")
if sub!=None:
    empid = f.getvalue("empid")
    name = f.getvalue("name")
    dob = f.getvalue("dob")
    gender = f.getvalue("gender")
    mid = f.getvalue("mailid")
    adrs = f.getvalue("address")
    phno = f.getvalue("phnno")
    salary = f.getvalue("salary")
    profile = f['profile']

    if profile.filename:
        filename=os.path.basename(profile.filename)
        open("files/"+filename,"wb").write(profile.file.read())
        q = """update tabei set name='%s',dob='%s', gender='%s', mailid='%s', address='%s', phnno='%s', salary='%s', profile='%s' where id=%s"""%(name.capitalize(),dob,gender,mid,adrs,phno,salary,filename,uid)
    else:
        q = """update tabei set name='%s',dob='%s', gender='%s', mailid='%s', address='%s', phnno='%s', salary='%s' where id=%s"""%(name.capitalize(),dob,gender,mid,adrs,phno,salary,uid)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
    window.alert('Data changed');
    location.href = "adminview.py";
    </script>
    """)
    conn.close()