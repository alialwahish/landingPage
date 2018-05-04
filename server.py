from flask import Flask,render_template,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/ninjas")
def ninja():
    return render_template("ninja.html")
@app.route("/dojo/new")
def dojos():
    return render_template("dojo.html")

app.run(debug=True)
