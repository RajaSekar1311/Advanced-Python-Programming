#login.py
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return 'Welcome : %s'%name
@app.route('/loginpage', methods = ['post', 'get'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))
if __name__ == '__main__':
    app.run(host = '10.14.51.65', port = 5050, debug=True)