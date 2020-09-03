import requests
from bs4 import BeautifulSoup
import time
# 使用网络请求类库
import urllib.request

def main():
    url = 'http://www.variflight.com/sitemap.html?AE71649A58c77='
    # 请求头
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.variflight.com',
        'Cookie': '_ga=GA1.2.128747732.1598840911; _gid=GA1.2.208035445.1598840911; PHPSESSID=tl9fqahnt06omeq1jqcub6lvv2; Hm_lvt_d1f759cd744b691c20c25f874cadc061=1598840903,1598840916,1598841037,1599113344; midsalt=5f508dad05af5; fnumHistory=%5B%7B%22fnum%22%3A%223U5021%22%7D%2C%7B%22fnum%22%3A%22AC8%22%7D%2C%7B%22fnum%22%3A%22CZ5045%22%7D%2C%7B%22fnum%22%3A%223U5012%22%7D%2C%7B%22fnum%22%3A%223U5027%22%7D%2C%7B%22fnum%22%3A%22CA8905%22%7D%2C%7B%22fnum%22%3A%22CA1957%22%7D%2C%7B%22fnum%22%3A%22CA1961%22%7D%5D; salt=5f509017e3414; Hm_lpvt_d1f759cd744b691c20c25f874cadc061=1599115289',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    data = {'wd': '邓超'}

    try:
        # 写入User Agent信息
        response = requests.get(url, params=data, headers=header)
        # 读取响应信息并解码
        if response.status_code == 200:
            html = response.text
            print(response.status_code)
    except Exception:
        print('error')
        time.sleep(5)
        return

    # 获取请求
    req = urllib.request.Request(url)
    # 打开页面
    webpage = urllib.request.urlopen(req)
    # 读取页面内容
    html = webpage.read()
    # 解析成文档对象
    soup = BeautifulSoup(html, 'html.parser')  # 文档对象
    # 非法URL 1
    #invalidLink1 = '#'
    # 非法URL 2
    #invalidLink2 = 'javascript:void(0)'
    # 集合
    result = set()
    flightnumber=[]
    # 查找文档中所有a标签
    for k in soup.find_all('a'):
        # print(k)
        # 查找href标签
        #link = k.get('href')
        # 过滤没找到的
        # if (link is not None):
        #     # 过滤非法链接
        #     if link == invalidLink1:
        #         pass
        #     elif link == invalidLink2:
        #         pass
        #     elif link.find("javascript:") != -1:
        #         pass
        #     else:
        print(k.string)
        flightnumber.append(k.string)
        result.add(k.string)
    f = open(r'flightnumber.txt', 'w', encoding='utf-8')  # 文件路径、操作模式、编码  # r''

    #数据清洗


    for a in result:
        f.write(str(a) + "\n")
    f.close()
    print("\r\n扫描结果已写入到flightnumber.txt文件中\r\n")
main()