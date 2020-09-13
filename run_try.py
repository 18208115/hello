from fake_useragent import UserAgent
import requests
import json
import xlrd
import xlwt
import time
#不在循环体里读写文件，程序的效率会高出很多
#78为测试运行所需，正式运行删掉即可


def get_position(numberlist):
    #json数据举例
    # {'msg': 'success', 'code': 200, 'data': {'alert': '0', 'angle': '178', 'anum': 'B5282',
    # 'atype': 'B737', 'atypename': 'Boeing737-700 Winglets', 'device': '8728b827ebc839a4', 'deviceTime': 1599718404,
    # 'emergency': '0', 'fnum': 'CES5938', 'height': 6012.18, 'id': '7807D7', 'onground': '0',
    # 'position': {'lat': 25.78096, 'long': 102.25302}, 'speed': 638.94, 'spi': '0', 'squawk': '2120',
    # 'time': 1599718404, 'updateflag': 1, 'updatetime': 1599718406, 'vspeed': -1152.0}}
    datalist = []
    for flightnumber in numberlist:
        url = "https://adsbapi.variflight.com/adsb/index/track/"+flightnumber+"?lang=zh_CN"
        # https://adsbapi.variflight.com/adsb/index/track/HU7389?lang=zh_CN
        # 对比中只有航班号不同
        headers = {
            'User-Agent': '{}'.format(UserAgent().random),
            'Connection': 'keep - alive',
            'Host': 'adsbapi.variflight.com',
            'Origin': 'https: // flightadsb.variflight.com',
            'Sec - Fetch - Mode': 'cors',
            'Sec - Fetch - Site': 'same - site',
            'Referer': 'https://flightadsb.variflight.com/tracker/'+flightnumber
        }
        response = requests.get(url, headers=headers)  # !!!若用json的函数转换   需先转换为str
        try:
            # routelist = json.loads(response.text)
            # json.loads将已编码的JSON字符串解码为Python 对象   objet对象转换为字典dict
            result = response.json()
        except json.decoder.JSONDecodeError:
            time.sleep(3)#停滞程序三秒
            print("异常！")
            continue#网站反扒机制会给假数据，为了不让程序异常停止，处理异常并停滞程序三秒
        else:
            if result.get('code') == 200:
                rowlist = []
                print(flightnumber+"爬取成功")
                #print(result)  # 字典类型    有用参数，msg或code判断爬取结果   data中anum用于爬取具体信息   其他为航班基本信息
                detaildict = get_flightdetail(result.get('data').get('anum'))  # 用于爬取航班信息
                #调用另一个爬取基本信息的函数
                #航班号
                airCName = detaildict.get('data').get('airCName')#航空公司
                forgAptCcity = detaildict.get('data').get('forgAptCcity')#起飞城市
                forgAptCname = detaildict.get('data').get('forgAptCname')#起飞机场
                forgAptLat = detaildict.get('data').get('forgAptLat')#起始纬度
                forgAptLon = detaildict.get('data').get('forgAptLon')  # 起始经度
                scheduledDeptime = detaildict.get('data').get('scheduledDeptime')  # 预计起飞时间
                fdstAptCcity = detaildict.get('data').get('fdstAptCcity')  #降落城市
                fdstAptCname = detaildict.get('data').get('fdstAptCname')  # 降落机场
                fdstAptLat = detaildict.get('data').get('fdstAptLat')  # 终止纬度
                fdstAptLon = detaildict.get('data').get('fdstAptLon')  # 终止经度
                scheduledArrtime = detaildict.get('data').get('scheduledArrtime')  # 预计降落时间
                actualDeptime = detaildict.get('data').get('actualDeptime')  # 实际起飞时间
                estimatedArrtime = detaildict.get('data').get('estimatedArrtime')  # 预计实际降落时间
                airAge = detaildict.get('data').get('airAge')  # 机龄
                atypename = detaildict.get('data').get('atypename')  # 机型
                try:
                    position_lat = result.get('data').get('position').get('lat')
                    position_long = result.get('data').get('position').get('long')
                except AttributeError:
                    continue
                else:
                    speed = result.get('data').get('speed')#水平速度
                    vspeed = result.get('data').get('vspeed')#垂直速度
                    height = result.get('data').get('height')#飞行高度
                    updatetime = result.get('data').get('updatetime')#读取时间
                    rowlist = [flightnumber,airCName,forgAptCcity,forgAptCname,forgAptLat,forgAptLon,scheduledDeptime,fdstAptCcity,fdstAptCname,fdstAptLat
                               ,fdstAptLon,scheduledArrtime,actualDeptime,estimatedArrtime,airAge,atypename,position_lat,
                               position_long,speed,vspeed,height,updatetime]
                    datalist.append(rowlist)
                    break
            else:
                print(flightnumber+"暂无数据")
    return datalist


def get_flightdetail(anum):
    #json数据举例{'msg': 'success', 'code': 200, 'data': {'actualDeptime': 1599714120, 'airAge': '13.3',
    # 'airCName': '厦门航空有限公司', 'airCtry': 'CN', 'airIATA': 'MF', 'aircraftNumber': 'B5318',
    # 'airline': 'MF', 'airname': 'Xiamen Airlines', 'atype': 'B738', 'atypename': 'Boeing737-800 Winglets',
    # 'dstTinezone': 28800, 'estimatedArrtime': 1599718625, 'estimatedDeptime': 1599708600,
    # 'fdst': 'CSX', 'fdstAptCcity': '长沙', 'fdstAptCity': 'Changsha', 'fdstAptCname': '长沙黄花',
    # 'fdstAptICAO': 'ZGHA', 'fdstAptLat': 28.193336, 'fdstAptLon': 113.21459, 'fdstAptName': 'Changsha Huanghua',
    # 'flightStatusCode': 1, 'fnum': 'MF8194', 'fnum3': 'CXA8194', 'forg': 'WUH',
    # 'forgAptCcity': '武汉', 'forgAptCity': 'Wuhan', 'forgAptCname': '武汉天河', 'forgAptICAO': 'ZHHH',
    # 'forgAptLat': 30.776598, 'forgAptLon': 114.209625, 'forgAptName': 'Wuhan Tianhe', 'ftype': 'B738',
    # 'icaoId': '780313', 'id': '5eed4fd1a9128ebd3dced4de202e2952', 'imageId': '9C146811-76DA-49E7-A1B2-10050281F155',
    # 'imageUrl': 'https://file.veryzhun.com/buckets/wxapp/keys/20181030-160815-x1maklpe19ienbav.jpg!400!300',
    # 'orgTinezone': 28800, 'scheduledArrtime': 1599710400, 'scheduledDeptime': 1599708600}}

    url = "https://adsbapi.variflight.com/adsb/index/flightdetail?lang=zh_CN&anum=" + anum + "&onground=0"
    # https://adsbapi.variflight.com/adsb/index/flightdetail?lang=zh_CN&anum=B5318&onground=0
    # 对比中只有anum不同，拼接url
    headers = {
        'Connection': 'keep - alive',
        'Host': 'adsbapi.variflight.com',
        'User-Agent': '{}'.format(UserAgent().random)
    }
    response = requests.get(url, headers=headers)  # response对象中含json数据
    # routelist = json.loads(response.text)
    # json.loads 将已编码的 JSON 字符串解码为 Python 对象
    result = response.json()  # 字典 get('key') 返回 value
    return result


if __name__ == "__main__":          #当程序执行时
    workbook = xlrd.open_workbook('flightnumber1.xls')#存储航班号的文件  航班号由get_flightnymber.py获取
    sheet = workbook.sheets()[0]#获得工作表  索引
    # print(sheet.nrows)
    # print(sheet.ncols)#查看大小
    first_col = sheet.col_values(1)#获取第一列的值，即航班号
    datalist = get_position(first_col)#将航班号作为列表传入函数
    titlelist = ["flightnumber","airCName","forgAptCcity","forgAptCname","forgAptLat","forgAptLon","scheduledDeptime","fdstAptCcity","fdstAptCname","fdstAptLat","fdstAptLon","scheduledArrtime","actualDeptime","estimatedArrtime","airAge","atypename","position-lat","position-long","speed","vspeed","height","updatetime"]
                # 航班号           航空公司     起飞城市         起飞机场        起飞 经纬度                  计划起飞时间            降落城市      降落机场        降落经纬度                   计划降落时间          实际起飞时间       预计降落时间       机龄      机型          实时纬度        实时经度         速度     垂直速度   高度      上传时间
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表
    i = 0
    for title in titlelist:
        worksheet.write(0,i,title)
        i = i+1
    k = 1
    for row in datalist:
        j = 0
        for data in row:
            worksheet.write(k, j, data)
            j = j + 1
        k = k + 1
    workbook.save('datatext.xls')  # 保存数据表


