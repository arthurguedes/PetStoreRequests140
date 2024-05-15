import pytest
import requests   #framework de teste de API 
import json



store_id = 5
store_petId = 1
store_quantity = 5
store_shipDate = "2024-05-15T17:55:21.564Z"
store_status = "placed"
store_complete = True

url= 'https://petstore.swagger.io/v2/store/order'                 
headers= {'Content-type':"application/json"}  

def test_post_order():
    user = open('./fixtures/json/order.json')         # abertura de arquivo json 
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
    assert response_body['quantity'] == 5
    assert response_body['status'] == "placed"
    assert response_body['complete'] == True



def test_get_order():

    response = requests.get(
        url=f'{url}/{store_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['quantity'] == 5
    assert response_body['status'] == "placed"
    assert response_body['complete'] == True


def test_delete_order():

    response = requests.delete(
        url=f'{url}/{store_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(store_id)




