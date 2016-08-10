from flask import Flask
from ecdsa.ecdsa import __main__
from pip.download import user_agent
from django.http import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():   
    return '<h1>hello world</h1>'
if __name__ =='__main__':
    app.run(debug=True)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
if __name__ =='__name__':
    app.run(debug=True)


@app.route('/abc/')
def abc():
    user_agent = request.HttpRequest.GET('User-Agent')
    return '<p> Your browser is %s </p>' % user_agent()


@app.route('/')
def ppp():
    respone = make_response('<h1>This document carries a cookie</h1>')
    respone.set_cookie('answer','42')
    return respone


@app.route('/')
def a():
    return redirect('http://www.taobao.cn')




