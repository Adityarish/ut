# pyrefly: ignore [missing-import]
from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}

# GET
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET single elememt
@app.route('/student/<roll>', methods=['GET'])
def get_student(roll):
    if roll in students:
        return jsonify(students), 200
    return jsonify({"error":"Student not found"}) ,404

# POST
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or "roll" not in data or "name" not in data or "course" not in data:
        return jsonify({"error":"Invalid input"}), 400

    roll = str(data["roll"])
    if roll in students:
        return jsonify({'error':'Student already exist'}), 400
    
    students[roll] = {
        "name" : data['name'],
        "course" : data['course']
    }
    return jsonify({'message':'Student added successfully'}), 201
    
@app.route('/student/<roll>', methods=['DELETE'])
def delete_student(roll):
    if roll not in students:
        return jsonify({'error':'Student not found'}), 404

    del students[roll]
    return jsonify({'message':'Student deleted successfully'}), 200

@app.route('/student/<roll>', methods=['PUT'])
def update_student(roll):
    if roll not in students:
        return jsonify({'error':'Student not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error':'Invalid input'}), 400

    students[roll]['name'] = data.get('name', students[roll]['name'])
    students[roll]['course'] = data.get('course', students[roll]['course'])
    return jsonify({'message':'Student updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)