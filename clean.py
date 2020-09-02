import pandas as pd
#去除相同航班号的数据
data = pd.DataFrame(pd.read_excel('国内航班数据new.xls', 'hangban'))

# 查看去除重复行的数据
data.drop_duplicates(subset="flight_schedules", keep='first', inplace=True)
print(data)
# 将去除重复行的数据输出到csv表中，存到桌面
data.to_csv("C:/Users/CH/Desktop/hangban.csv",index=False,encoding="utf_8_sig")
