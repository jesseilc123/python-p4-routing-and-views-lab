#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_route(parameter):
    print(f"{parameter}")
    return f'{parameter}'

@app.route("/count/<int:parameter>")
def count_route(parameter):
    new_str = ""
    for i in range(parameter):
        new_str += f"{str(i)}\n"
    return new_str

@app.route("/math/<param1>/<param2>/<param3>")
def math_route(param1, param2, param3):
    if param2 == "+":
        return str(int(param1) + int(param3))
    if param2 == "-":
        return str(int(param1) - int(param3))
    if param2 == "*":
        return str(int(param1) * int(param3))
    if param2 == "div":
        return str(int(param1) / int(param3))
    if param2 == "%":
        return str(int(param1) % int(param3))
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
