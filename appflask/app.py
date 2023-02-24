from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Bievenidos a mi primera API con flask"

@app.route("/student")
def student():
    return {
        'name':'Gonzalo',
        'age': 27,
        'grade': 20
    }


student_list = [
            {
            'name':'Gonzalo',
            'age': 27,
            'grade': 20
            },
             {
            'name':'Guillermo',
            'age': 30,
            'grade': 20
            },
             {
            'name':'Gustavo',
            'age': 35,
            'grade': 20
            }
            ]

@app.route("/students", methods=['GET','POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'])
def students():
    print(request.method)
    if request.method == 'GET':
        return student_list
    elif request.method == 'POST':
        print(request.json)
        student_list.append(request.json)
        return student_list

@app.route("/student/<name>")
def search_student(name):
    student =  [x for x in student_list if x['name'] == name]
    if len(student) == 0: return 'Not found'
    return student

@app.route("/html")
def html():
    # return "<button> Click me </button>"
    return render_template("index.html")

@app.route("/form-data", methods=['POST'])
def form_data():
    print(request.form)
    return 'Form data received'

@app.route("/files", methods=['POST'])
def files():
    f = request.files['txt'].read().decode('utf-8')
    print(f)
    return "File received successfully"

app.run(debug=True)