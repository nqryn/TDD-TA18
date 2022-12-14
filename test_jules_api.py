import requests


def test_wrong_login():
    api_login_url = "https://api.jules.app/login"
    payload = {
        "email": "fake.email@ceva.com",
        "password": "ParolaGresita"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
    }
    response = requests.post(api_login_url, json=payload, headers=headers)
    # 401 BAD REQUEST
    assert response.status_code == 401
    response_json = response.json()
    assert response_json.get('message') == 'Invalid email/password combination'


def test_contacts_postman_api():
    contacts_url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MzZhOWIxZTZlOTNmMTAwMTUyNjA1MmIiLCJpYXQiOjE2Njc5MzA5MTB9.jcl-7KJRPRqtM6xwRN1ppd3fSg-P65z_JiVIaDQi-80"
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.get(contacts_url, headers=headers)

    # 200 OK
    assert response.status_code == 200
    assert len(response.json()) == 1
    my_contact = response.json()[0]
    assert my_contact['firstName'] == 'Cineva'
    assert my_contact['lastName'] == 'Lallalaal'

