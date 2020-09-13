from pyecharts import options as opts
from pyecharts.charts import Geo
import xlrd


workbook = xlrd.open_workbook('data.xls')#存储数据的文件  由run_try.py生成
sheet = workbook.sheets()[0]#获得工作表  索引
flightnumber_list = sheet.col_values(0)#获取第一列的值，即航班号
aircname = sheet.col_values(1)#航空公司
lat_list = sheet.col_values(20)#纬度数据
long_list = sheet.col_values(21)#经度数据
city1 = sheet.col_values(2)#起飞城市
city2 = sheet.col_values(8)#降落城市
speed = sheet.col_values(22)#飞机速度
vspeed = sheet.col_values(23)#垂直速度
height = sheet.col_values(24)#飞行高度
uptime = sheet.col_values(26)#时间


c = Geo()
# 加载图表模型中的中国地图
c.add_schema(maptype="china")

i = 1
for i in range(1,10):
    c.add_coordinate("航班号" + flightnumber_list[i], long_list[i], lat_list[i])
    # 为自定义的点添加属性
    c.add("geo", [("航班号" + flightnumber_list[i], "航空公司："+aircname[i]+"  "+city1[i]+"飞往"+city2[i]+"  飞行速度："+str(speed[i])+"  垂直速度："+str(vspeed[i])+"  高度："+str(height[i])+"  时间"+uptime[i])])
    # 设置坐标属性

c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 设置全局属性
c.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="航班信息可视化"),
)


# 在 html(浏览器) 中渲染图表
c.render()
# 在 Jupyter Notebook 中渲染图表
c.render_notebook()
