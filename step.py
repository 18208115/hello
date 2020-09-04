from random import random
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# 得到一个地方航班的所有线路

url = "https://flights.ctrip.com/schedule/yie..html"
flightlines = {}   # {'安庆-北京': 'http://flights.ctrip.com/schedule/aqg.bjs.html', ...｝
headers = {
    'Referer': 'https://flights.ctrip.com/schedule/',
    'User-Agent': '{}'.format(UserAgent().random)
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
letter_list = soup.find(attrs={'id': 'ulD_Domestic'}).find_all('li')
for li in letter_list:
    for a in li.find_all('a'):
        flightlines[a.get_text()] = a['href']
        print(flightlines[a.get_text()])

