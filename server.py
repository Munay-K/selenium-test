from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://munay:No7854@localhost/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80),  nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color


@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


"""
@app.route('/index', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.session.query(People).filter_by(pname=username).first()
        print(user)
        print(user.pname)
        print(user.color)
        if (user.color != password):
            message = 'Error: Invalid Credentials. Please try again.'
        else:
            message = 'Success: Login Sucessful.'
    return render_template('login.html', message=message)
"""

@app.route('/index', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = []

        for result in db.engine.execute("SELECT * FROM people WHERE pname="+"'"+username+"'"):
            print(result)
            print(result[0])
            print(result[1])
            if (result[2] != password):
                message = 'Error: Invalid password. Please try again.'
            else:
                message = 'Success: Login Sucessful.'
        if(len(result) == 0):
            message = 'Invalid user'
    return render_template('login.html', message=message)


@app.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


@app.route("/delete", methods=['GET'])
def deleteTable():
    print('ga')
    return 'SE BORRO LA WEA'


if __name__ == '__main__':
    db.create_all()
    app.run()
