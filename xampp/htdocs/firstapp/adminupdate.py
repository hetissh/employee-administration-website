#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi,os
import pymysql as p, cgitb

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="dbfirst")
cur = conn.cursor()

f = cgi.FieldStorage()
uid = f.getvalue("u")
q = """select * from tabsi where RegNo=%s"""%(uid)
cur.execute(q)
r = cur.fetchone()


print("""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Edit</title>
    <link rel = "icon" type="text/ico" href = "files/download.jpg">
    <link rel="stylesheet" href="style1.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" charset="utf-8"></script>
  </head>
  <body>

      <form action="#" class="login-form" enctype="multipart/form-data" method = "post" autocomplete = "off">
        <h1>Edit</h1>
        
        <center>
        
        <img src="%s" height ="50" width="50">
        
        </center>

        <div class="txtb">
          <input type="text" name = "name" value="%s" placeholder="Name" required> 
        </div>

        <div class="txtb">
          <input type="date" name = "dob" value="%s" placeholder="Date of birth" required> 
        </div>

        <div class="txtb">
            <input type="email" name = "mailid" value="%s" placeholder="Mailid"  required>
        </div>

        <div class="txtb">
            <input type="number" name = "phone_number" value="%s" placeholder="ContactNo" required>
        </div>

        <div class="txtb">
            <input type="text" name = "password" value="%s" placeholder="password" readonly>
        </div>

        <div class="txtb">
            <input type="file" name = "profile" >
        </div>

        <input type="submit" class="subbtn" name = "subbtn" value="Save">
      </form>

  </body>
</html>
"""%("files/"+r[6],r[1],r[2],r[4],r[3],r[5]))

sub = f.getvalue("subbtn")
if sub!=None:
    name = f.getvalue("name")
    mid = f.getvalue("mailid")
    phno = f.getvalue("phone_number")
    pwd = f.getvalue("password")
    dob = f.getvalue("dob")
    profile = f['profile']

    if profile.filename:
        filename=os.path.basename(profile.filename)
        open("files/"+filename,"wb").write(profile.file.read())
        q = """update tabsi set name='%s', dob='%s', ContactNo='%s',Mailid='%s', password='%s', profile='%s' where RegNo=%s"""%(name.capitalize(),dob,phno,mid,pwd,filename,uid)
    else:
        q = """update tabsi set name='%s', dob='%s', ContactNo='%s',Mailid='%s', password='%s' where RegNo=%s""" % (name.capitalize(), dob, phno, mid, pwd, uid)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
    window.alert('Data changed');
    location.href = "adminview.py";
    </script>
    """)
    conn.close()
