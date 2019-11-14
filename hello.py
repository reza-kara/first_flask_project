from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app1 = Flask(__name__)

bootstrap = Bootstrap(app1)

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

@app1.route('/')
def index():
    return render_template('index.html',mydict=mydict)

@app1.route('/user/<name>')
def SayHello2User(name):
    return render_template('user.html', name=name, me='*ROCK STAR*')

if __name__ == '__main__':
    app1.run(debug=True)
