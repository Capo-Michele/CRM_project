from flask import Flask, render_template

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)
