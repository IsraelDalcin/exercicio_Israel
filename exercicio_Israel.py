import requests
import json

api = 'https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=600&camera=pancam&api_key=18dJe0tVOWFdqcNMPoW2q65psHKGnVds6st8sAMd'
request = requests.get(api)
url_img = list()
counter = 0

if request.status_code == 200:
    json_string = request.text
    api_dict = json.loads(json_string)
    dct_lst = api_dict['photos']
    for dicts in dct_lst:
        if 'img_src' in dicts:
            if counter < 10:
                url_img.append(dicts['img_src'])
                print(f'A URL da imagem {counter+1} é: {url_img[counter]}')
                counter += 1
else:
    print('Erro na requisição!')