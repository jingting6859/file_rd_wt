import selenium
from selenium import webdriver
# webdriver.Chrome()
# driver = webdriver.Chrome(r'D:\ChromeCoreDownloads\chromedriver.exe')
# driver.get('https://mkt.51job.com/tg/sem/pz_2018.html?from=baidupz')

# options = webdriver.ChromeOptions()
# options.binary_location = r"D:\ChromeCoreDownloads\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
# browser.get('https://www.baidu.com')

# option = webdriver.ChromeOptions()
# option.binary_location = r'D:\ChromeCoreDownloads\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=r'D:\ChromeCoreDownloads\chromedriver_win32\chromedriver.exe',chrome_options=option)
# driver.get('https://www.baidu.com')

#excell 读写操作
import xlrd,xlwt
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    # style.borders = borders

    return style

import random
book = xlwt.Workbook()
# sheet = book.add_sheet('sheet1')
sheet1 = book.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
status = [u'预订',u'出票',u'退票',u'业务小计']

#写标题行
for i in range(len(row0)):
    sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))

# 1 到 n 行
# 生成第一列和最后一列(合并4行)
i, j = 1, 0
while i < 4 * len(column0) and j < len(column0):
    sheet1.write_merge(i, i + 3, 0, 0, column0[j], set_style('Arial', 220, True))  # 第一列
    sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
    i += 4
    j += 1

sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))

# 生成第二列
i = 0
while i < 4 * len(column0):
    for j in range(0, len(status)):
        sheet1.write(j + i + 1, 1, status[j])
    i += 4

book.save('demo1.xlsx')  # 保存文件


book = xlrd.open_workbook('demo1.xlsx')
sheet = book.sheet_by_name('sheet1')
row= sheet.nrows
col = sheet.ncols
sheet.
# for i in range(1,row):
#     for j in range(1,col):
#         print(sheet.cell_value(i,j))

# 获取行值
print(sheet.row_values(0))
print(sheet.col_values(0,1))
# 获取单元格值
print(sheet.cell(0,0).)


