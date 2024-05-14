import pytest
import requests   #framework de teste de API 
import json




pet_id = 173218101   #código do animal 
pet_name = "Snoopy"  # nome do animal
pet_category_id = 1  #codigo da categoria do animal
pet_category_name = "dog"   #titulo da categoria 
pet_tag_id = 1       # codigo da tag - rotulo 
pet_tag_name = "vacinado"     # titulo do rotulo 
      #status do animal 


url= 'https://petstore.swagger.io/v2/pet'                 #endereço
headers= {'Content-type':"application/json"}              # formato dos dados trafegados


def test_post_pet():
    #configuração - dados de entrada / arquivo json 
    pet = open('./fixtures/json/pet1.json')         # abertura de arquivo json 
    data = json.loads(pet.read())                   # leitura do conteudo e carrega como json em uma variavel data 


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
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name 
    assert response_body['tags'][0]['name'] == pet_tag_name


def test_get_pet():




    response = requests.get(
        url=f'{url}/{pet_id}',
        headers=headers,

    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'



def test_put_pet():

    pet = open('./fixtures/json/pet2.json')
    data = json.loads(pet.read())

    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout= 5 
    )

    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name 
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'sold'


def test_delete_pet():



    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)

    







































