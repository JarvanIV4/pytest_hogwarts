# -*- coding: utf-8 -*-
# @Time : 2020/04/11
# @Author : Wind
import base64
import random
import time
from flask import Flask, request

app = Flask(__name__)

users = {
    "magigo": ["123456"]
}

def gen_token(uid):
    print('')
    token = base64.b64encode(bytes(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]), encoding='utf-8'))
    users[uid].append(token)
    return token

def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request.headers)
    return "hello"

@app.route('/login', methods=['POST', 'GET'])
def login():
    print(type(base64.b64decode(request.headers['Authorization'].split(' ')[-1])))
    uid, pw = str(base64.b64decode(request.headers['Authorization'].split(' ')[-1]), encoding='utf-8').split(':', 1)
    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'error'

@app.route('/test', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'

@app.route('/', methods=['POST', 'GET'])
def t():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)