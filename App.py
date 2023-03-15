from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/projetcitoyen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    zone = db.Column(db.String(100))
    work = db.Column(db.String(100))
    date = db.Column(db.String(100))
    organization = db.Column(db.String(100))

    def __init__(self, name, email, phone, zone, work, date, organization):
        self.name = name
        self.email = email
        self.phone = phone
        self.zone = zone
        self.work = work
        self.date = date
        self.organization = organization

    def __repr__(self) -> str:
            return f"Data{self.id}"


@app.route('/')
def index():
    all_works = Data.query.all()
    return render_template('index.html', title='home', works = all_works)

@app.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        zone = request.form['zone']
        work = request.form['work']
        date = request.form['date']
        organization = request.form['organization']

        my_data = Data(name, email, phone, zone, work, date, organization)
        db.session.add(my_data)
        db.session.commit()

        flash("Work Inserted Successfully")
        
        return redirect(url_for('index'))

@app.route('/update', methods = ['POST'])
def update():

    if request.method == 'POST':

        my_data = Data.query.get(request.form.get('id'))

        my_data.name= request.form['name']
        my_data.email= request.form['email']
        my_data.phone= request.form['phone']
        my_data.zone= request.form['zone']
        my_data.work= request.form['work']
        my_data.date= request.form['date']
        my_data.organization= request.form['organization']

        db.session.commit()

        flash("Work Updated Successfully")
            
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
        my_data = Data.query.get(id)
        db.session.delete(my_data)
        db.session.commit()

        flash("Work delete Successfully")
            
        return redirect(url_for('index'))

if __name__ == "__name__":
    app.run(debug=True)