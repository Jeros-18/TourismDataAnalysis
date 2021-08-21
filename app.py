from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()

@app.route('/aaa')
def aaa():
    return render_template("index2.html")

@app.route('/bbb')
def bbb():
    return render_template("index3.html")

@app.route('/ccc')
def ccc():
    return render_template("bigdata.html")

@app.route('/ddd')
def ddd():
    return render_template("survey.html")


if __name__ == '__main__':
    app.run()
