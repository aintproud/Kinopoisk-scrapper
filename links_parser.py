from bs4 import BeautifulSoup
import lxml
import json

with open('top250.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

div = soup.find_all(class_="selection-film-item-meta__link")

tags = {}

for tag in div:
    href = 'https://www.kinopoisk.ru/' + tag.get('href')
    name = tag.find(class_="selection-film-item-meta__name").text 
    if ':' in name:
        name = name.replace(':', '_')
    tags[name] = href

with open('data/links.json', 'w', encoding='utf-8') as file:
    json.dump(tags, file, ensure_ascii=False, indent=4)






    
