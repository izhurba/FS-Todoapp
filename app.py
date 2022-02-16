from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  completed = db.Column(db.Boolean, nullable=False, default=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html', data=[{
    'description': 'Todo 1'
  }, {
    'description': 'Todo 2'
  }, {
    'description': 'Todo 3'
  }])


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=4455)


