from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


# app.add_url_rule('/', 'index', index)
# SET FLASK_APP=hello.py
# SET FLASK_DEBUG=1

# if __name__ == '__main__':
#     app.run()
