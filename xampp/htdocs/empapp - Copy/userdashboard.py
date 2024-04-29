#!C:/Users/HETISSH/AppData/Local/Programs/Python/Python310/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi, cgitb, pymysql as p

cgitb.enable()

conn = p.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

f=cgi.FieldStorage()
uid=f.getvalue("u")
q="""select * from tabei where id=%s"""%(uid)
cur.execute(q)
r=cur.fetchone()

print("""
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: monospace;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        }
        h1 {
            font-size: 40px;
            text-align: center;
            margin-top: 50px;
            color: #333;
        }
        h2 {
            font-size: 24px;
            margin-top: 30px;
            margin-bottom: 10px;
            color: #333;
        }
        p {
            font-size: 18px;
            color: #444;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome %s</h1>
    </div>
</body>
</html>
"""%(r[1],))
