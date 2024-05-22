from flask import Flask, request, jsonify

app = Flask(__name__)

datas = [
    {
        "id": 1,
        "nama": "Toko Laptop",
        "items": [
            {
                "item_name": "Laptop Asus TUF Gaming F15",
                "price": 12000000
            }
        ]
    },
    {
        "id": 2,
        "nama": "Toko Robotik",
        "items": [
            {
                "item_name": "Arduino UNO",
                "price": 56000
            }
        ]
    }
]

@app.route('/store')
def getAll():
    return jsonify(datas)

@app.route('/store/<int:id>')
def getItemid(id):
    for data in datas:
        if (data)['id'] == id:
            return jsonify(data)
    return jsonify({'message': "Data not found"})

@app.route('/store', methods=['POST'])
def addStore():
    req_data = request.get_json()
    new_data = {
        'id': req_data['id'],
        'nama': req_data['nama'],
        'items': req_data['items'],
    }
    datas.append(new_data)
    return jsonify(new_data)

@app.route('/store/<int:id>', methods=['DELETE'])
def delete(id):
    for i, data in enumerate(datas):
        if data['id'] == id:
            deleted = datas.pop(i)
            return jsonify({'message': 'Data deleted', 'deleted': deleted})
    return jsonify({'message': 'data not found'})

@app.route('/store/<int:id>', methods=['PATCH'])
def update(id):
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 415
    req_data = request.get_json()

    for i, data in enumerate(datas):
        if data['id'] == id:
            if 'nama' in req_data:
                datas[i]['nama'] = req_data['nama']
            if 'items' in req_data:
                datas[i]['items'] = req_data['items']
            return jsonify({'message': 'Data updated', 'data': datas[i]})

    return jsonify({'message': 'Data not found'}), 404

@app.route('/')
def home():
    return "Selamat datang di Compushop!"

if __name__ == '__main__':
    app.run(debug=True)