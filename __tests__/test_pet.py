import pytest
import requests   #framework de teste de API 
import json
from utils.utils import ler_csv 




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


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags,status',
                         ler_csv('./fixtures/csv/pets.csv')
                         )

def test_post_pet_dinamico(pet_id,category_id,category_name,pet_name,tags,status):
    pet = {}     # lista vazia pet 
    pet['id'] = int(pet_id)
    pet['category'] = {}
    pet['category']['id'] = int(category_id)
    pet['category']['name'] = category_name
    pet['name'] = pet_name
    pet['photoUrls'] = []
    pet['photoUrls'].append('')
    pet['tags'] = []

    tags = tags.split(';')
    for tag in tags:
        tag = tag.split('-')
        tag_formatada = {} 
        tag_formatada['id'] = int(tag[0])
        tag_formatada['name'] = tag[1]
        pet['tags'].append(tag_formatada)
    
    pet['status'] = status 

    pet = json.dumps(obj=pet, indent=4)
    print('\n' + pet)                     # visualiza o json criado dinamicamente 

    #executa 

    response = requests.post(
        url=url,
        headers=headers,
        data=pet,
        timeout=5
    )
    #compara
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == int(pet_id)
    assert response_body['name'] == pet_name
    assert response_body['status'] == status 
    

    


















    







































