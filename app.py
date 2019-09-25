
# source code
# https://github.com/jakerieger/FlaskIntroduction

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s = db.Column(db.Integer, nullable=False)
    s2 = db.Column(db.Integer, nullable=False)
    s3 = db.Column(db.Integer, nullable=False)
    s4 = db.Column(db.Integer, nullable=False)
    s5 = db.Column(db.Integer, nullable=False)
    s6 = db.Column(db.Integer, nullable=False)
    s7 = db.Column(db.Integer, nullable=False)
    s8 = db.Column(db.Integer, nullable=False)
    s9 = db.Column(db.Integer, nullable=False)
    s10 = db.Column(db.Integer, nullable=False)
    score_sum = db.Column(db.Integer, nullable=False)


    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_s = request.form['s']
        task_s2 = request.form['s2']
        task_s3 = request.form['s3']
        task_s4 = request.form['s4']
        task_s5 = request.form['s5']
        task_s6 = request.form['s6']
        task_s7 = request.form['s7']
        task_s8 = request.form['s8']
        task_s9 = request.form['s9']
        task_s10 = request.form['s10']
        score_sum = int(task_s) + int(task_s2) + int(task_s3) + int(task_s4) + int(task_s5) + int(task_s6) + int(task_s7) + int(task_s8) + int(task_s9) + int(task_s10)
        new_task = Todo(s=task_s, s2=task_s2, s3=task_s3, s4=task_s4, s5=task_s5, s6=task_s6, s7=task_s7, s8=task_s8, s9=task_s9, s10=task_s10, score_sum=score_sum)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    target = Todo.query.get_or_404(id)

    try:
        db.session.delete(target)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task.'

if __name__ == "__main__":
    app.run(debug=True)
