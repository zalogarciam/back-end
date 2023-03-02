from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def init():
    return {'message': 'Welcome to my API!'}

@app.route('/students', methods = ['GET','POST'])
def students():
    if request.method == 'POST':
        return  {'message': 'POST'}
    elif request.method == 'GET':
        return {'message': 'GET'}

if __name__ == '__main__':
    app.run(debug=True)

