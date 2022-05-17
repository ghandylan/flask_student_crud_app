from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import *

app = Flask(__name__)
app.secret_key = "hotdogs"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ghandylan:hotdog123@localhost/FlaskApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.INT, primary_key = True)
    name = db.Column(db.VARCHAR(255))
    email = db.Column(db.VARCHAR(255))
    phone = db.Column(db.VARCHAR(255))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template('index.html', students = all_data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Student Inserted Successfully")

        return redirect(url_for('index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Student Updated Successfully")

        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Student Deleted Successfully")

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=False)
    app.run()
    db.create_all()
