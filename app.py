#!/usr/bin/env python
# coding: utf-8
import json
import flask
from flask import request, render_template
import iris

PORT_NO = 8085
app = flask.Flask(__name__)
print('http://localhost:' + str(PORT_NO))


@app.route('/')
def index():
    data = iris.getIris()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=PORT_NO)
