from flask import Flask

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
            },
             {
            'name':'Carmen',
            'age': 30,
            'grade': 20
            },
        ]

@app.route("/students")
def students():
    return student_list

@app.route("/student/<name>")
def search_student(name):
    student =  [x for x in student_list if x['name'] == name]
    if len(student) == 0: return 'Not found'
    return student

app.run(debug=True)