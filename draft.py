import requests


def send_get_request():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
    except Exception as e:
        raise Exception(e)
    assert response.status_code == 200
    return response.json()

data = send_get_request()

def get_info(data):
    list = []
    for i in data:
        dict = {}
        for j, value in i.items():
            if j == "title" and "vol" in value:
                dict['id'] = i['id']
                dict[j] = value
        if len(dict) > 0:
            list.append(dict)
    print(list)
    return list

get_info(data)
