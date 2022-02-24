from flask import Flask, render_template, url_for
import time
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#https://www.youtube.com/watch?v=Z1RJmh_OqeA
#15:43
#https://towardsdatascience.com/using-python-flask-and-ajax-to-pass-information-between-the-client-and-server-90670c64d688
#get-processes
#taskkill /F /PID 13952

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/index.html')
def hello_world():
    return render_template('index.html')

@app.route('/time')
def current_time():
    current_time= time.time()
    localTime = time.localtime(current_time)
    return ("<p>  Time : %dh:%dm:%ds</p>" %(localTime.tm_hour,localTime.tm_min,localTime.tm_sec))

def time_rn():
    current_time= time.time()
    localTime = time.localtime(current_time)
    return ("<p>  Time : %dh:%dm:%ds</p>" %(localTime.tm_hour,localTime.tm_min,localTime.tm_sec))


if __name__ == '__main__':
    app.run(debug=True)
