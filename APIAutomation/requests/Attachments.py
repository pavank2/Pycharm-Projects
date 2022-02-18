import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"

files = {'file': open('C:\\Users\\PK\\Downloads\\car.jpg', 'rb')}
request_attach = requests.post(url,files = files)

print(request_attach.status_code)