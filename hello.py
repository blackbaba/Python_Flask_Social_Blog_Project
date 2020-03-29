from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string aha..'
bootstrap = Bootstrap(app)
moment = Moment(app)

# Root route
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


# User route
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Error routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# app.add_url_route('/', 'index', index)
# SET FLASK_APP=hello.py
# SET FLASK_DEBUG=1

# if __name__ == '__main__':
    # app.run(debug=True)
