from flask import (Flask, render_template, request, flash, redirect, url_for)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306//flaskapp'


app.config ['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
    user = {'username': "Васёк", 'age': 28}

    posts = [
        {'author': "notVanya", 'body': 'This is my first post!'},
        {'author': "Mary", 'body': 'Flask is cool!'}
    ]
    return render_template ('index.html', posts = posts, user=user, title="This is my site")

@app.route('/user/<username>')
def user_name(username):
    return (f'<h1>user\'s name: {username}</h1>')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == 'admin':
            flash ("you've successfully entered", "success")
            return redirect (url_for ('index'))
        else: 
            flash ("you've failed", "error")
            return redirect (url_for ('login'))

    return render_template ('login.html')

if __name__ == '__main__':
    app.run(debug=True)
