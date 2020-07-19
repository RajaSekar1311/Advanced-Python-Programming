from flask import Flask
app = Flask(__name__)

#By default
#a decorator function
@app.route('/')
def display():
	return 'Welcome to SCET-Autonomous Python Workshop'
	
@app.route('/message')
def displayMessage():
	return 'I am updating a new message here while my Web App is already running'

@app.route('/message/<name>')
def displayName(name):
	return 'Hello %s'%name
	
if (__name__ == '__main__'):
	#app.run()
	app.run(host='10.14.51.65',port=9090,debug = True)
	
	


