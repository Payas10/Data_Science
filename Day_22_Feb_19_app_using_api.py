from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world_1():
    return "Hello, World 1!"

@app.route("/hello2")
def hello_world_2():
    return "Hello, world 2!"

@app.route("/test_fun")
def test():
    a = 5 + 6
    return "this is my first function in flask {}".format(a)

@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
