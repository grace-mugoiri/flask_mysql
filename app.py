"""import necessary modules"""
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# configure the db
db = yaml.load(open("db.yaml"))
app.config["MySQL_HOST"] = db["mysql_host"]
app.config["MySQL_USER"] = db["mysql_user"]
app.config["MySQL_PASSWORD"] = db["mysql_password"]
app.config["MySQL_DB"] = db["mysql_db"]

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def index():
    """define tthe index function"""
    if request.method == "POST":
        # fetch the data forms
        userDetails = request.form
        firstname = userDetails["firstname"]
        secondname = userDetails["secondname"]
        foodtoeat = userDetails["foodtoeat"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(firstname, secondname, foodtoeat) VALUES(%s, %s, %s)",(firstname, secondname, foodtoeat))
        mysql.connection.commit()
        cur.close()
        return redirect("/users")
    return render_template("index.html")

@app.route("/users")
def users():
    """define the users function endpoint"""
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("users.html", userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)
