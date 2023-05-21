from flask import Flask,redirect
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello my World'

@app.route("/<some>")
def szndj(some):
	return some

@app.route("/gokul/ <b>")
def func(b):
	return f"gokul {b} is a good boy"
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)
