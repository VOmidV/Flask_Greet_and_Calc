# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def adds():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return f"""{add(a, b)}"""


@app.route('/sub')
def subs():
  a = request.args['a']
  b = request.args['b']
  return f"""{sub(a, b)}"""


@app.route('/mult')
def mults():
  a = request.args['a']
  b = request.args['b']
  return f"""{mult(a, b)}"""
  

@app.route('/div')
def divs():
  a = int(request.args['a'])
  b = int(request.args['b'])
  return f"""{div(a, b)}"""
