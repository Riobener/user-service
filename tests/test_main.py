import requests

api = 'http://localhost:8081/users'

def test_user_empty_get():
    s = requests.Session()
    id = '7bd047cb-a57e-412c-9d83-81c50e3e3902'
    response = s.get(f'{api}/{id}')
    assert response.status_code == 200


def test_user_save_and_get():
    s = requests.Session()
    parameters = "?name=Benjamin&departmentId=7bd047cb-a57e-412c-9d83-81c50e3e3902"
    response = s.post(f'{api}/{parameters}')
    assert response.status_code == 200
    assert response.json().get('name') == 'Benjamin'
    createdUserId = response.json().get('id')
    responseUser = s.get(f'{api}/{createdUserId}')
    assert responseUser.status_code == 200
    assert responseUser.json().get('name') == 'Benjamin'


