from bs4 import BeautifulSoup
import lxml
import json
import requests
import random
from fake_useragent import UserAgent
import time
import os
from requests.auth import HTTPProxyAuth

# proxies

proxies = {'http': 'ur proxy'}
auth = HTTPProxyAuth('login', 'password')

# links

with open('data\\links.json', encoding='utf-8') as file:
    dictionary = json.load(file)

#  request

for name, link in dictionary.items():
    os.mkdir(f'data/{name}')
    useragent = UserAgent()
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"}
    r = requests.get(url=link, proxies=proxies, headers=headers, auth=auth)
    src = r.text
    with open(f'data/{name}/{name}.html','w', encoding='utf-8') as file:
        file.write(src)
    
    with open(f'data/{name}/{name}.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    actors = soup.find(class_="styles_wideContentContainer__3AhDG")
    print(len(actors))

    mas = []
    for actor in actors:
       mas.append(f'{actor.text}')
       
    with open(f'data/{name}/actors.json', 'w', encoding='utf-8') as file:
         json.dump(mas, file, ensure_ascii=False, indent=4)

    
    time.sleep(random.randint(7, 30))
      
