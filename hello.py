from flask import Flask
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return '<h1>Hello World from Flask </h1>'
