from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {'username': "Elena", 'age': 28}

    posts = [
        {'author': "Vanya", 'body': 'This is my first post!'},
        {'author': "Mary", 'body': 'Flask is cool!'}
    ]
    return render_template ('index.html', posts = posts, user=user, title="Main")

@app.route('/user/<username>')
def user_name(username):
    return f'<h1>user\'s name: {username}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
