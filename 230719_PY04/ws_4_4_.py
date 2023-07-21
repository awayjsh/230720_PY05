black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

import requests
from pprint import pprint as print

def create_user(user_info):

    censored_user_list = []

    for j in range(len(user_info)) :

        part_dict = {}
        name_list = []
        name_list.append(user_info[j]['name'])

        if censorship(user_info[j]['company'],user_info[j]['name']) == True :

            part_dict[user_info[j]['company']] = name_list
            censored_user_list.append(part_dict)

    return censored_user_list
 
def censorship(company,name):

    if company in black_list :

        print(f"{company} 소속의 {name} 은/는 등록할 수 없습니다.")
        return False
    else :

        print("이상 없습니다.")
        return True
    

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