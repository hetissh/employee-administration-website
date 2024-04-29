#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")


print("""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>New user</title>
    <link rel = "icon" type="text/ico" href = "files/download.jpg">
    <link rel="stylesheet" href="style1.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" charset="utf-8"></script>
  </head>
  <body>

      <form action="#" class="login-form" enctype="multipart/form-data" method = "post" autocomplete = "off">
        <h1>Registeration Form</h1>

        <div class="txtb">
          <input type="text" name = "name" placeholder="Name" required> 
        </div>
        
        <div class="txtb">
          <input type="date" name = "dob" placeholder="Date of birth" required> 
        </div>

        <div class="txtb">
            <input type="email" name = "mailid" placeholder="Mailid"  required>
        </div>

        <div class="txtb">
            <input type="number" name = "phone_number" placeholder="ContactNo" required>
        </div>

        <div class="txtb">
            <input type="password" name = "password" placeholder="password"  required>
        </div>
        
        <div class="txtb">
            <input type="file" name = "profile" required>
        </div>
        
        <input type="submit" class="subbtn" name = "subbtn" value="Submit">
      </form>

  </body>
</html>
""")

import cgi, cgitb, pymysql as p
import os

cgitb.enable()

f = cgi.FieldStorage()
# print(f)

sub = f.getvalue("subbtn")
if sub!=None:
    conn = p.connect(host="localhost", user="root", password="", database="dbfirst")
    cur = conn.cursor()
    name = f.getvalue("name")
    mid = f.getvalue("mailid")
    phno = f.getvalue("phone_number")
    pwd = f.getvalue("password")
    dob = f.getvalue("dob")
    profile = f['profile']

    if profile.filename:
        filename=os.path.basename(profile.filename)
        open("files/"+filename,"wb").write(profile.file.read())

        # print(name,mid,phno,pwd)

        q = """insert into tabsi values('','%s','%s','%s','%s','%s','%s')"""%(name.capitalize(),dob,phno,mid,pwd,filename)
        cur.execute(q)

        conn.commit()
        print("""
        <script>
        window.alert('Data inserted');
        location.href = "login.py";
        </script>
        """)
        conn.close()