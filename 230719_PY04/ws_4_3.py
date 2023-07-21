import requests
from pprint import pprint as print

dummy_data = []

API_URL = 'https://jsonplaceholder.typicode.com/users/1'

for i in range(10) :

    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i+1)
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80 :

        dict_keys = ['company','lat','lng','name']
        dict_values = [parsed_data['company']['name'],parsed_data['address']['geo']['lat'],parsed_data['address']['geo']['lng'],parsed_data['name']]
        dummy_data.append(dict(zip(dict_keys,dict_values)))

print(dummy_data)

    
