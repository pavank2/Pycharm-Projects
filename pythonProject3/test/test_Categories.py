import pytest
import requests
import json
def test_getCategories():

    url = 'http://localhost:3030/products'
    header = {'Content-Type':'Application/json'}
    products = requests.get(url, headers=header)

    #assert categories.status_code == 200
    products_json = products.json()
    products_list = products_json['data']
    num_products = len(products_list)


    for i in range(num_products):
        categories_list = products_list[i]['categories']
        num_categories = len(categories_list)
        for j in range(num_categories):
            #print(categories_list[j]['name'])
            if categories_list[j]['name'] == 'Car Audio':
                id = categories_list[j]['id']
                #print (id)
                #print("http://localhost:3030/categories/{}".format(id))

                del_req = requests.delete('http://localhost:3030/categories/{}'.format(id),\
                                          headers={'Content-Type':'application/json'})

                assert del_req.status_code == 200,\
                f"Expected status code is 200 whereas actual status code is {del_req.status_code}"

@pytest.mark.smoke
def test_getCategorieswithCoffeePods():

    get_resp = requests.get('http://localhost:3030/products',params= {'category.name':'Coffee Pods'},\
                            headers={'Content-Type':'Application/json'})

    print(type(get_resp))
    json_resp = get_resp.json()

    print(type(json_resp))
   # dict_resp = json.loads(json_resp)

    #print(type(dict_resp))
    #products_list = json_resp['data']

    for item in json_resp['data']: # Iterating through a list
        if item['shipping'] == 0:
            print(item['name'])

   # length = len(products_list)

    #print(length)

    #for i in range(length):
     #   type(products_list[i]['shipping'])
      #  if products_list[i]['shipping'] == 0:
       #     print(products_list[i]['name'])