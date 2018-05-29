# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["미세먼지 알아보기", "도움말"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"미세먼지 알아보기":
        dataSend = {
            "message": {
                "text": "1. 경기도 \n 2. 경상북도 \n 3. 경상남도"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "이제 곧 정식 버전이 출시될거야. 조금만 기다려~~~"
            }
        }
    elif u"1" in content:
        dataSend = {
            "message": {
                "text": "경기도 미세먼지는 00이야"
            }
        }
    elif u"2" in content:
        dataSend = {
            "message": {
                "text": "경상북도 미세먼지는 00이야"
            }
        }
    elif u"3" in content:
        dataSend = {
            "message": {
                "text": "경상남도 미세먼지는 00이야"
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "숫자만 입력하세요"
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
