#爬取航班基本数据，，航空公司，起落时间等，，单个
from fake_useragent import UserAgent
import requests
import json
from bs4 import BeautifulSoup


url = "https://adsbapi.variflight.com/adsb/index/track/CZ6368?lang=zh_CN"
      #https://adsbapi.variflight.com/adsb/index/track/HU7389?lang=zh_CN
#对比中只有航班号不同
headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
                'Referer': 'https://flightadsb.variflight.com/tracker/CZ6368',
                "Content-Type": "application/json"
            }
response = requests.get(url, headers=headers, timeout=30).text
            #  json.dumps 将 Python 对象编码成 JSON 字符串
routeList = json.loads(response)# 字典 get('key') 返回 value
            # json.loads 将已编码的 JSON 字符串解码为 Python 对象
print(routeList)

