from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Привет, мир! </h1>'

@app.route('/test')
def test():
    return '<h1>Привет, мир! Test1 </h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
