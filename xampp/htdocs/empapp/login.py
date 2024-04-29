#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")


import cgi, cgitb, pymysql as p

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

print("""

<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
    <link rel = "icon" type="text/ico" href = "files/icn.png">
    <link rel="stylesheet" type="text/css" href="emps2.css">
</head>
<body>
    <div><h1>Login Page</h1></div><br>
    <div class="login">
    <form action="#" class="login-form" method = "post">
        <label><b>User Name</b>
        </label>
        <input type="text" name="uname" id="Uname" placeholder="username" required>
        <br><br>
        <label><b>Password</b></label>
        <input type="password" name="pass" id="Pass" placeholder="password" required>
        <br><br>
        <input type="submit" name="sub" id="log" value="Login">
        <input type="button"  id="log" value="Cancel" onclick="location.href='index.py';">
        <br><br>
    </form>
</div>
</body>
</html>
""")

f = cgi.FieldStorage()
sub=f.getvalue("sub")
if sub!=None:
    uname=f.getvalue("uname")
    pwd=f.getvalue("pass")
    q="""select * from tabei where name='%s' and empid='%s'"""%(uname,pwd)
    cur.execute(q)
    r=cur.fetchone()
    if r!=None:
        print("""
        <script>
        window.alert('Login successful');
        location.href="admindashboard.py?u=%s";
        </script>
        """%(r[0]))
    else:
        print("""
        <script>
        window.alert('Invalid username or password');
        location.href = "login.py";
        </script>
        """)