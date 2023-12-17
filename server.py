import requests

# Menambahkan data tracking
add_data = {'id': '123', 'location': 'Jakarta'}
response = requests.post('http://127.0.0.1:5000/tracking', json=add_data)
print(response.json())

# Mendapatkan data tracking berdasarkan ID
id_to_get = '123'
response = requests.get(f'http://127.0.0.1:5000/tracking/{id_to_get}')
print(response.json())
