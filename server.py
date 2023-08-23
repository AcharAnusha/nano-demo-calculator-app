from flask import Flask
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ' '
    return 'hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    return ''
    result={'result':data['first']+data['second']}
    res=json.dump(result,indent=4)
    return res

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''
    result={'result':data['first']-data['second']}
    res=json.dump(result,indent=4)
    return res

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')