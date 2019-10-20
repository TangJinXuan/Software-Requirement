import requests
from bs4 import BeautifulSoup
import re

f = open('title.json', 'w')

for i in range(1,9):
    url = 'https://github.com/microsoft/vscode/pulls?page=' + i.__str__() + '&q=is%3Apr+is%3Aopen'
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    div = soup.find_all('div', class_ = 'float-left col-8 lh-condensed p-2')
    a_div = BeautifulSoup(str(div))
    a = a_div.find_all('a', class_ = 'link-gray-dark v-align-middle no-underline h4 js-navigation-open')
    for item in a:
        print(item.string)
        jst = item.string + '\n'
        f.write(jst)