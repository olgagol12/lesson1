import requests
base_url = "https://x-clients-be.onrender.com"

def test_get_emplo():
    r = requests.get(base_url + "/employee?company=506")
    body = r.json()
    assert r.status_code == 200

def test_aut():

    creds = {
        "username": "michaelangelo",
        "password": "party-dude"
    }
    new_emplo = {
        "id": 0,
        "firstName": "kkdjk",
        "lastName": "sng",
        "middleName": "sdddgdsdng",
        "companyId": 506,
        "email": "sddhtsddng@mail.ru",
        "url": "kmkfvdfsdk",
        "phone": "fhtrokvo",
        "birthdate": "2024-09-12T17:50:13.575Z",
        "isActive": True
    }


    r = requests.post(base_url + "/auth/login", json=creds)
    token = r.json()["userToken"]
    new = {}
    new ["x-client-token"] = token
    re = requests.post(base_url + '/employee' , json=new_emplo, headers=new)
    assert re.status_code == 201




   



def test_emplo():
    creds = {
        "username": "michaelangelo",
        "password": "party-dude"
    }
    new_emplo = {
        "id": 0,
        "firstName": "kkdjk",
        "lastName": "sng",
        "middleName": "sdddgdsdng",
        "companyId": 506,
        "email": "sddhtsddng@mail.ru",
        "url": "kmkfvdfsdk",
        "phone": "fhtrokvo",
        "birthdate": "2024-09-12T17:50:13.575Z",
        "isActive": True
    }
    body = {
        "lastName": "sngfff",
        "email": "sddhtsddng@mail.ru",
        "url": "kmkfvdfsdk",
        "phone": "fhtrokvo",
        "isActive": True
    }
    r = requests.post(base_url + "/auth/login", json=creds)
    token = r.json()["userToken"]
    new = {}
    new["x-client-token"] = token
    re = requests.post(base_url + '/employee', json=new_emplo, headers=new)
    i = {}
    i ["id"] = new_emplo.get(id)
    rej = requests.patch(base_url + '/employee', json=body, headers= i)
    assert rej.status_code == 201