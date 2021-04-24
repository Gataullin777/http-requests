import requests



intelligence_statistics = {}

def intelligence_Hulk():

    url = 'https://superheroapi.com/api/2619421814940190/search/hulk'
    response = requests.get(url)
    r = response.json()
    for hero in r['results']:
        if hero['name'] == 'Hulk':
            intelligence_statistics[hero['powerstats']['intelligence']] = hero['name']

def intelligence_Captain_America():

    url = 'https://superheroapi.com/api/2619421814940190/search/captain america'
    response = requests.get(url)
    r = response.json()

    for hero in r['results']:
        if hero['name'] == 'Captain America':
            intelligence_statistics[hero['powerstats']['intelligence']] = hero['name']

def intelligence_Thanos():

    url = 'https://superheroapi.com/api/2619421814940190/search/thanos'
    response = requests.get(url)
    r = response.json()

    for hero in r['results']:
        if hero['name'] == 'Thanos':
            intelligence_statistics[hero['powerstats']['intelligence']] = hero['name']

def intelligence_comparison():
    value = 0
    for intelligence in intelligence_statistics:
        if int(intelligence) > value:
            value = int(intelligence)

    print(f'Из всех героев по интелекту побеждает: {intelligence_statistics[str(value)]}')


if __name__ == '__main__':
    intelligence_Hulk()
    intelligence_Captain_America()
    intelligence_Thanos()
    intelligence_comparison()

