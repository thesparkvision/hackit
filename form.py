from flask import Flask,render_template
app =Flask(__name__)
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import flash, redirect

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    state=SelectField('State', [DataRequired()],
                        choices=[('Madhya Pradesh', 'Madhya Pradesh'),
                                 ('Arunachal Pradesh', 'Arunachal Pradesh'),
                                 ('Uttar Pradesh', 'Uttar Pradesh'),
                                 ('Bihar', 'Bihar'),
                                 ('Kerala', 'Kerala'),
                                 ('Punjab', 'Punjab'),
                                 ('Others','Others')])
    sector = StringField('Sector', validators=[DataRequired()])
    subcategory =StringField('Subcategory', validators=[DataRequired()])
    resumelink = StringField('Resumelink(Uploaded on Google drive)', validators=[DataRequired()])
    submit = SubmitField('Submit')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    state=db.Column(db.String(120),index=True)
    sector=db.Column(db.String(64), index=True)
    subcategory=db.Column(db.String(64), index=True)
    resumelink=db.Column(db.String(400),index=True)

    def __str__(self):
        return '<User {}>'.format(self.username)

@app.route('/')
@app.route('/home')
def login():
    return render_template('home.html')

@app.route('/success')
def submit_success():
    return render_template('submission.html',title='Submission Success')

@app.route('/submit/', methods=['GET', 'POST'])
def submitform():
    form = LoginForm()
    if form.validate_on_submit():
        applicant = User(firstname=form.firstname.data, lastname=form.lastname.data,email= form.email.data,state=form.state.data, sector=form.sector.data,
                             subcategory= form.subcategory.data,resumelink= form.resumelink.data)
        db.session.add(applicant)
        db.session.commit()
        return redirect('/success')
    return render_template('submit.html', title='Submit Application', form=form)

@app.route('/dashboard')
def dashboard_generator():
    return "Dashboard"

if __name__=="__main__":
    app.run(debug=True)
