#爬取单个航班实时经纬度数据
from fake_useragent import UserAgent
import requests
import json


url = "https://adsbapi.variflight.com/adsb/index/track/MF8356?lang=zh_CN"
      #https://adsbapi.variflight.com/adsb/index/track/HU7389?lang=zh_CN
#对比中只有航班号不同
headers = {
    'User-Agent': '{}'.format(UserAgent().random),
    'Referer': 'https://flightadsb.variflight.com/tracker/MF8356'
}
response = requests.get(url, headers=headers, timeout=30).text
#  json.dumps 将 Python 对象编码成 JSON 字符串
routeList = json.loads(response)# 字典 get('key') 返回 value
# json.loads 将已编码的 JSON 字符串解码为 Python 对象
print(routeList)#字典类型    有用参数，msg或code判断爬取结果   data中anum用于爬取具体信息   其他为航班基本信息
print(type(routeList))




