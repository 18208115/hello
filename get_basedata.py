#爬取航班基本数据，，航空公司，起落时间等，，单个
from fake_useragent import UserAgent
import requests
import json


url = "https://adsbapi.variflight.com/adsb/index/flightdetail?lang=zh_CN&anum=B5318&onground=0"
      #https://adsbapi.variflight.com/adsb/index/flightdetail?lang=zh_CN&anum=B5318&onground=0
#对比中只有航班号不同
headers = {
    'User-Agent': '{}'.format(UserAgent().random),
    'Referer': 'https://flightadsb.variflight.com/tracker/MF8356'
}
response = requests.get(url, headers=headers, timeout=30).text
#  json.dumps 将 Python 对象编码成 JSON 字符串
routeList = json.loads(response)# 字典 get('key') 返回 value
# json.loads 将已编码的 JSON 字符串解码为 Python 对象
print(routeList)
print(type(routeList))
#print(routeList.get('data').get('airCName'))#尝试取出数据

