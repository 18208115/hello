from random import random
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 得到所有地方航班及链接

flights = {}  # {'安庆航班': 'https://flights.ctrip.com/schedule/aqg..html', ...}
url = 'https://flights.ctrip.com/schedule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'upgrade-insecure-requests': '1'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
letter_list = soup.find(attrs={'class': 'letter_list'}).find_all('li')
for li in letter_list:
    for a in li.find_all('a'):
        flights[a.get_text()] = url + a['href'][9:]
        print(flights[a.get_text()])


