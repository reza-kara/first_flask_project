from flask import Flask
app1 = Flask(__name__)

@app1.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app1.route('/user/<name>')
def SayHello2User(name):
    return '<h1>Hi %s!</h1>' % name.capitalize()

if __name__ == '__main__':
    app.run(debug=True)
