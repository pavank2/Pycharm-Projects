import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('../config/properties.ini')
response = requests.get(config['API']['endpoint']+"/Library/GetBook.php", params={'AuthorName':'John Doe'},)

response_json = response.json()

for obj in response_json:
    if obj['book_name'] == "Learn API":
        print(obj['isbn'])
