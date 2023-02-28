from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def wel():
  return 'welcome'

@app.route('/welcome/home')
def write():
  return f"welcome home"

@app.route('/welcome/back')
def back():
  return 'welcome back'