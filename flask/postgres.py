from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)
con = connect(host='localhost', database='alumnos', user='postgres', password='scrappy')

@app.route('/', methods = ['GET'])
def init():
    return {'message': 'Welcome to my API!'}

@app.route('/students', methods = ['GET','POST'])
def students():
    if request.method == 'POST':
        data = request.json
        cursor = con.cursor()
        print(data)
        cursor.execute("INSERT INTO alumnos(nombre, apellido, matriculado) VALUES(%s, %s, %s)", (data.get('name'), data.get('last_name'), data.get('enrolled')))
        con.commit()
        return  {'message': 'POST'}
    elif request.method == 'GET':
        cursor = con.cursor()
        cursor.execute('SELECT * FROM alumnos;')
        res = cursor.fetchall()
        # print(res)
        list = []
        for alumno in res:
            item = {
                'id': alumno[0],
                'name': alumno[1],
                'last_name': alumno[2],
                'sex': alumno[3],
                'date': alumno[4],
                'enrolled': alumno[5],
            }
            list.append(item)
            print(list)

        return {'message': list}

@app.route('/student/<id>', methods = ['GET','PUT','DELETE'])
def student(id):
    if request.method == 'GET':
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM alumnos where id = {id}")
        student = cursor.fetchone()
        if student is None:
            return {
            'message': 'Student not found',
        }
        return {'message': {
            'id': student[0],
                'name': student[1],
                'last_name': student[2],
                'sex': student[3],
                'date': student[4],
                'enrolled': student[5],
        }}
    
    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

if __name__ == '__main__':
    app.run(debug=True)

