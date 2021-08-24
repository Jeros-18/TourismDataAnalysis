import xlrd
import xlwt
from collections import Counter
import pandas as pd

work = xlrd.open_workbook('../templates/xls/地图.xls')
sheet = work.sheets()[0]
data = sheet.col_values(0)
tem = Counter(data)
print(tem)
fidata = sorted(tem.items(),key=lambda tem:tem[1],reverse=True)
print(fidata)
province=[]
nums=[]
for i in fidata:
    province.append(i[0])
    nums.append(i[1])
print(province,nums)

def map():
    work = xlrd.open_workbook('../templates/xls/地图.xls')
    sheet = work.sheets()[0]
    data = sheet.col_values(0)
    tem = Counter(data)
    fidata = sorted(tem.items(), key=lambda tem: tem[1], reverse=True)
    province = []
    nums = []
    for i in fidata:
        province.append(i[0])
        nums.append(i[1])