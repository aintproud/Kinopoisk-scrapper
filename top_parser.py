import requests
from requests.auth import HTTPProxyAuth
import random
from fake_useragent import UserAgent

useragent = UserAgent()

url = 'https://www.kinopoisk.ru/lists/top250/?tab=all'
proxies = {'http': '193.187.147.112:8000'}
auth = HTTPProxyAuth('RZvvQA', 'agBAoH')
headers = {
    "Accept": "*/*",
    "User-Agent": f"{useragent.random}"}


r = requests.get(url, headers=headers, proxies=proxies, auth=auth)
src = r.text

with open('top250.html', 'w', encoding='utf-8') as file:
    file.write(src)




