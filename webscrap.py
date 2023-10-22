import requests
import pyautogui as pg
from bs4 import BeautifulSoup

headers = {"Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"
           }
url = pg.prompt("enter url from which you want to get data: ", 'URL')

try:
    response = requests.get(url, headers=headers)

except requests.exceptions.MissingSchema:
    pg.alert(f"Couldn't get data from: {url}!")
    raise Exception("Error in website's domain")

parser_html = BeautifulSoup(response.text, 'html.parser')
type_to_parse = pg.prompt("enter html tag to be parser(name, id, class): ", 'DATA')
data_to_parse = pg.prompt("enter html to be parser: ", 'DATA')

if type_to_parse == 'name':
    data = parser_html.find_all(data_to_parse)
elif type_to_parse == 'id':
    data = parser_html.find_all(id=data_to_parse)
elif type_to_parse == 'class':
    data = parser_html.find_all(class_=data_to_parse)
else:
    pg.alert('error')
    raise Exception('error')

if data:
    [print(pg.alert(article.text)) for article in data]
    with open("data.txt", 'w') as file:
        [file.write(f'{article}\n') for article in data]

else:
    pg.alert("None was found!")