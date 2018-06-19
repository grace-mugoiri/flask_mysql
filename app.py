"""import necessary modules"""
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# configure the db
db = yaml.load(open("db.yaml"))
app.config["MySQL_HOST"] = db["mysql_host"]
app.config["MySQL_USER"] = db["mysql_user"]
app.config["MySQL_PASSWORD"] = db["mysql_password"]
app.config["MySQL_DB"] = db["mydql_db"]


@app.route("/", methods=["GET", "POST"])
def index():
    """define tthe index function"""
    if request.method == "POST":
        # fetch the data
       userDetails = request.form
       firstName = userDetails["firstName"]
       secondName = userDetails["secondName"]
       foodToEat = userDetails["foodToEat"]

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)