import requests

URL = "http://127.0.0.1:8000/auth/register/"

"""
{
    "username": "",
    "email": "",
    "password": "",
    "first_name": "",
    "last_name": ""
}
"""

for i in range(10):
    data = {
        "username": f"usuario{i}",
        "email": f"usuario{i}@gmail.com",
        "password": "asdf*963,",
        "first_name": f"usuario{i}",
        "last_name": f"usuario{i}"
    }

    response = requests.post(URL, json=data)

    if response.status_code == 201:
        print(f"Usuário {i} criado com sucesso!")
    else:
        print(f"Erro ao criar usuário {i}")
