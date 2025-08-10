from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def home():
    return '<h1>Hello world</h1>'

@app.route('/oi')
def oi():
    return '<h4>oi</h4>'

if __name__ == '__main__':
    app.run(debug=True)