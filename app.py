from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/user/<username>')
def user_nane(username):
    return f'<h1>user\'s name: {username}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
