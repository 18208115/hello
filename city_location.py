import requests
import csv
import pandas as pd
import codecs
import json
from urllib.request import urlopen, quote

#修改路径即可匹配寻找城市经纬度
def get_city():
    data = pd.read_csv("D:\代码\py\课设\city_location.csv",header=None)
    list = data[0].values
    print("读取文件成功，处理结束")
    return list


def geocodeB(address):
    parameters = {'address': address, 'key': '49286e03f8cb5ffafd93d71c2eabea4f'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    print(address + "：", answer['geocodes'][0]['location'])


if __name__ == '__main__':
    # data_write_csv('city_location.csv', citys)
    citylist = get_city()
    print(citylist)
    #f = open(r'location.csv', 'w', encoding='utf-8')
    for i in range(len(citylist)):
        geocodeB(citylist[i])
    #f.close()
    #print("\r\n经纬度分析结果已写入到location.csv文件.中\r\n")