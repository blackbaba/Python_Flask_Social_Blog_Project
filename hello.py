from flask import Flask, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

# index route
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
				flash('Looks like you have changed your name !!')
		session['name']=form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))

# user route
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')
