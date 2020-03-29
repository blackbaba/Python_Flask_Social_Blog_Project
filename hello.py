from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Root route
@app.route('/')
def index():
    return render_template('index.html')

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


# app.add_url_route('/', 'index', index)
# SET FLASK_APP=hello.py
# SET FLASK_DEBUG=1

# if __name__ == '__main__':
    # app.run(debug=True)
