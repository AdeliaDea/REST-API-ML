from flask import Flask, request, jsonify

app = Flask(__name__)

# Data sementara untuk menyimpan tracking perjalanan
tracking_data = {}


@app.route('/tracking', methods=['POST'])
def add_tracking():
    # Mendapatkan data JSON dari permintaan
    data = request.get_json()

    # Memeriksa apakah data yang diperlukan ada dalam permintaan
    if 'id' not in data or 'location' not in data:
        return jsonify({'error': 'ID dan lokasi harus disertakan'}), 400

    # Menambahkan data tracking ke dalam dictionary
    tracking_data[data['id']] = data['location']

    return jsonify({'message': 'Data tracking berhasil ditambahkan'}), 201


@app.route('/tracking/<string:id>', methods=['GET'])
def get_tracking(id):
    # Memeriksa apakah ID ada dalam data tracking
    if id not in tracking_data:
        return jsonify({'error': 'ID tidak ditemukan'}), 404

    # Mengembalikan data tracking untuk ID yang diberikan
    return jsonify({'id': id, 'location': tracking_data[id]}), 200


if __name__ == '__main__':
    # Menjalankan aplikasi Flask pada port 5000
    app.run(debug=True)
