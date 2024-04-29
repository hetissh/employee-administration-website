#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

print("""
      
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "icon" type="text/ico" href = "files/icn.png">
    <link rel="stylesheet" href="emps1.css">
    <title>Employee registration form</title>
</head>
<body>
    <form action="#" class="login-form" enctype="multipart/form-data" method = "post" autocomplete = "off">
        <h1>Employee Registeration Form</h1>

    <div class="txtb">
    <label> Employee id : </label>
    <input type="number" name="empid" placeholder="Enter your employee id" required /> <br> <br>
    </div>  

    <div class="txtb">
    <label> Name : </label>
    <input type="text" name="name" placeholder="Enter your name" required /> <br> <br>
    </div>  
    
    <div class="txtb">
    <label> Date of birth : </label>
    <input type="date" name="dob" placeholder="dd-mm-yyyy" required /> <br> <br>  
    </div>

    <div class="txtb">
    <label> Gender : </label>  
        <input type="radio" name="gender" required/> Male   
        <input type="radio" name="gender" required/> Female <br> <br>
    </div>


    <div class="txtb">
    <label> Mail id : </label>
    <input type="email" name="mailid" placeholder="Enter your mail id" required /> <br> <br>  
    </div>

    <div class="txtb">
    <label> Address : </label>
    <input type="text" name="address" placeholder="Enter your address" required /> <br> <br>
    </div>

    <div class="txtb">
    <label> Phone number : </label>
    <input type="number" name="phnno" placeholder="Enter your contact number" required /> <br> <br>
    </div>
    
    <div class="txtb">
    <label> Salary : </label>   
        <select name="salary" required>  
        <option value="salary">Select your salary</option>  
        <option value="20,000">20,000</option>  
        <option value="40,000">40,000</option>  
        <option value="60,000">60,000</option>  
        <option value="80,000">80,000</option>  
        <option value="1,00,000">1,00,000</option>  
        <option value="1,20,000">1,20,000</option>  
        </select> 
    </div>

    <div class="txtb">
        <input type="file" name = "profile" required>
    </div>
    
    <input type="submit" class="subbtn" name = "sub" value="Submit">

    </form>

</body>
</html>
      
      """)

import cgi, cgitb, pymysql as p
import os

cgitb.enable()

f = cgi.FieldStorage()
# print(f)

sub = f.getvalue("sub")
if sub!=None:
    conn = p.connect(host="localhost", user="root", password="", database="empdb")
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

        # print(name,mid,phno,pwd)

        cur = conn.cursor()
        q = """insert into tabei values('','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(empid,name.capitalize(),dob,gender,mid,adrs,phno,salary,filename)
        cur.execute(q)
        
        conn.commit()
        print("""
        <script>
        window.alert('Data inserted');
        location.href = "login.py";
        </script>
        """)
        conn.close()