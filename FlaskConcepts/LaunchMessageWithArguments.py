from flask import Flask

app = Flask(__name__)

@app.route('/integer/<int:integerNumber>')
def show_integer(integerNumber):
	return 'The interger number is %d'%integerNumber
	
@app.route('/float/<float:floatingNumber>')
def show_float(floatingNumber):
	return 'The float number is %f'%floatingNumber
	
@app.route('/string/<string:stringInput>')
def show_string(stringInput):
	return 'The string is %s'%stringInput

if __name__ == '__main__':
	app.run(host='10.14.51.65',port=2020)

