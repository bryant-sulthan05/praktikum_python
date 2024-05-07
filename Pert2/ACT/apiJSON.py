import requests

payload = [{
    'nama': 'Bryant Sulthan Nugroho',
    'npm': 50423286,
    'kelas': '1IA03',
    'jurusan': 'Informatika',
    'alamat': 'Cileungsi',
    'userID': 1
},
{
    'nama': 'Lahdar Bellumi',
    'npm': 50123213,
    'kelas': '1KA06',
    'jurusan': 'Elektro',
    'alamat': 'Cibinong',
    'userID': 2
},
{
    'nama': 'Muhammad Yusuf Ghazali',
    'npm': 51431101,
    'kelas': '1KA02',
    'jurusan': 'ELektro',
    'alamat': 'Ciracas',
    'userID': 3
},
{
    'nama': 'Hanif Maulana',
    'npm': 50123122,
    'kelas': '1IA04',
    'jurusan': 'Informatika',
    'alamat': 'Jakarta selatan',
    'userID': 4
},
{
    'nama': 'Abdul Hakim Faiz',
    'npm': 50234724,
    'kelas': '1KA07',
    'jurusan': 'Elektro',
    'alamat': 'Jakarta Barat',
    'userID': 5
}
]

parameter = {'id': 5}

addPost = requests.post('https://httpbin.org/post', json=payload)

getPostID = requests.get('https://jsonplaceholder.typicode.com/posts', params=parameter)

if (len(getPostID.json()) > 0):
    print("Mencoba melakukan get request")
    print("Url: ", getPostID.url)
    print("Payload: ", getPostID.text)
    print()
    print("="*100)
    print()

if (addPost.status_code == 200 or addPost.status_code == 201):
    print("Mencoba melakukan post request")
    print("Status code: ", addPost.status_code)
    print("Payload: ", addPost.text)