#Q7NUEhTyYFOyDrtfmHDSnNRB7phGBEU8
import requests

def geocodeB(address):
    """
    @ address: 名称字符串
    @ 返回值：经度，纬度
    """
    base_url = "http://api.map.baidu.com/geocoder?address={address}&output=json&key=Q7NUEhTyYFOyDrtfmHDSnNRB7phGBEU8".format(address=address)

    response = requests.get(base_url)
    answer = response.json()
    latitude = answer['result']['location']['lng']
    longitude = answer['result']['location']['lat']

    return latitude, longitude
#南昌115.892151 28.676493
print(geocodeB('南昌市'))
#成都104.065735，30.659462
print(geocodeB('成都市'))

