import requests
from pprint import pprint



token = ''
file_path = r'C:\Users\rudol\Desktop\home work netology\test_file_for_home_work.txt'
disk_file_path = '/test_file_for_home_work.txt'
file_name = r'C:\Users\rudol\Desktop\home work netology\test_file_for_home_work.txt'

def get_headers():
    return {'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'}

def get_file_list():
    url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = get_headers()
    response = requests.get(url, headers=headers)
    r = response.json()
    return r

def get_upload_link():
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers = get_headers()
    params = {'path': disk_file_path,'overwrite': 'true' , 'fields':'href'}
    response = requests.get(upload_url, headers=headers, params=params)
    return response.json()

def upload_to_disk(filename):
    href = get_upload_link().get('href')
    response = requests.put(href, data=open(filename, 'rb'))
    response.raise_for_status()

    if response.status_code == 201 :
        print('Success')

if __name__ == "__main__":
    get_file_list()
    upload_to_disk(file_name)
