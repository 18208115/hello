import xlrd
import xlwt
import requests
from bs4 import BeautifulSoup
import time
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

    data = {'wd': '小明'}

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
    #第一行有唯一的脏数据，清洗掉
    invalidLink0='/sitemap/flight?AE71649A58c77='

    # 集合
    result = set()
    flightnumber=[]
    #查找文档中所有a标签
    #应该在class为list里找
    soup_msgs = soup.find_all('div', attrs={'class':'list'})
    #页面中只有这一个class为list的div标签，所以选择soup_msgs[0]
    for k in soup_msgs[0].find_all('a'):
        # print(k)
        #查找href标签
        link = k.get('href')
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
        #         result.add(link)
    # print("打印超链接个数:",mycount)
    # print("打印超链接列表",result)
    # f = open(r'result.txt', 'w', encoding='utf-8')  # 文件路径、操作模式、编码  # r''
    # for a in result:
    #     f.write(a + "\n")
    # f.close()
    # print("\r\n扫描结果已写入到result.txt文件中\r\n")

        #清洗
        if link ==invalidLink0:
            pass
        else:
            print(k.string)
            flightnumber.append(k.string)
            result.add(k.string)
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表
    i = 0
    for a in result:
        worksheet.write(i,0,str(a))
        i = i+1
    workbook.save('flightnumber.xls')  # 保存数据表
    print("\r\n扫描结果已写入到flightnumber.xls文件中\r\n")

main()
