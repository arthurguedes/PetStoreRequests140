import pytest
import requests   #framework de teste de API 
import json
from utils.utils import ler_csv

user_id = 50
user_username = "jose_moreira"
user_firstname = "jose"
user_lastname = "moreira"
user_email = "josemoreira@hotmail.com"
user_password = "jose1234"
user_phone = "11952013248"
user_status = 1

url= 'https://petstore.swagger.io/v2/user'                 
headers= {'Content-type':'application/json'}  

def test_post_user():
    user = open('./fixtures/json/user1.json')         # abertura de arquivo json 
    data = json.loads(user.read())                   # leitura do conteudo e carrega como json em uma variavel data 

    # execucao 
    response = requests.post(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout = 5
    ) 

    # validacao 
    response_body = response.json()                 # cria variavel e carrega a resposta em formato json
    

    assert response.status_code == 200 
    assert response_body['code'] == 200
    assert response_body['type'] == "unknown"
    assert response_body['message'] == str(user_id)

def test_get_user():

    response = requests.get(
        url=f'{url}/{user_username}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['username'] == user_username
    assert response_body['firstName'] == user_firstname
    assert response_body['lastName'] == user_lastname


def test_put_user():

    user = open('./fixtures/json/user2.json')
    data = json.loads(user.read())

    response = requests.put(
        url=f'{url}/{user_username}',
        headers=headers,
        data=json.dumps(data),
        timeout= 5 
    )

    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200
    assert response_body['type'] == "unknown"
    assert response_body['message'] == str(user_id)

def test_delete_user():

    response = requests.delete(
        url=f'{url}/{user_username}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == user_username



@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/user.csv')
                         )



def test_post_user_dinamico(user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status):
    user = {}     # lista vazia pet 
    user['id'] = user_id
    user['username'] = user_username
    user['firstName'] = user_firstname
    user['lastName'] = user_lastname
    user['email'] = user_email
    user['password'] = user_password
    user['phone'] = user_phone
    user['user_Status'] = user_status



    user = json.dumps(obj=user, indent=4)
    print('\n' + user)                     # visualiza o json criado dinamicamente 

    #executa 

    response = requests.post(
        url=url,
        headers=headers,
        data=user,
        timeout=5
    )
    #compara
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == "unknown"
    assert response_body['message'] == str(user_id)

    @pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/user.csv')
    )
    def test_get_user_dinamico(user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status):
        
        response = requests.get(
            url=f'{url}/{user_username}',
            headers=headers
        )

        response_body = response.json()

        assert response.status_code == 200
        assert response_body['id'] == int(user_id)
        assert response_body['username'] == user_username
        assert response_body['firstName'] == user_firstname


@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/user.csv')
    )
def test_put_user_dinamico(user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status):
        
        user = {}     # lista vazia pet 
        user['id'] = user_id
        user['username'] = user_username
        user['firstName'] = user_firstname
        user['lastName'] = user_lastname
        user['email'] = user_email
        user['password'] = user_password
        user['phone'] = user_phone
        user['user_Status'] = '0'

        user = json.dumps(obj=user, indent=4)
        print('\n' + user)

        response = requests.put(
            url=f'{url}/{user_username}',
            headers=headers,
            data=user,
            timeout=5
        )

        response_body = response.json()

        assert response.status_code == 200
        assert response_body['code'] == 200
        assert response_body['type'] == "unknown"
        assert response_body['message'] == str(user_id)
        







@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/user.csv')
                         )



def test_delete_user_dinamico(user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status):
    '''
    user = {}     # lista vazia pet 
    user['id'] = user_id
    user['username'] = user_username
    user['firstName'] = user_firstname
    user['lastName'] = user_lastname
    user['email'] = user_email
    user['password'] = user_password
    user['phone'] = user_phone
    user['user_Status'] = user_status
    '''

    '''
    user = json.dumps(obj=user, indent=4)
    print('\n' + user)                     # visualiza o json criado dinamicamente 
    '''
    #executa 

    response = requests.delete(
        url=f'{url}/{user_username}',
        headers=headers
    )
    #compara
    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == user_username
