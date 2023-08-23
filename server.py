from flask import Flask
from flask import Flask,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ''

@app.route("/calculator/add", methods=['POST'])
def add():
    return ''
    data = request.get_json()


    return { "result" : data["first"] + data["second"] }

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''
    data = request.get_json()


    return { "result": data["first"] - data["second"] }


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')