import xlrd
import xlwt
from collections import Counter
import pandas as pd
import csv

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
k=0
k=0

def read_excel():
    workBook1 = xlrd.open_workbook('templates/xls/团队结算明细.xls')
    sheet1 = workBook1.sheets()[0]

    aa = Counter(sheet1.col_values(4))
    moduleName = []
    # Counter({'other': 7862, 'catering': 2605, 'ticket': 2486, 'hotel': 1343, 'meeting': 979, 'training': 617, 'guid': 407, 'party': 84})
    moduleName = sorted(set(aa))

    otherTotal = 0
    cateringTotal = 0
    ticketTotal = 0
    hotelTotal = 0
    meetingTotal = 0
    trainingTotal = 0
    guidTotal = 0
    partyTotal = 0


    list = []
    sheet1_nrows = sheet1.nrows  # 获得行数
    for i in range(sheet1_nrows):  # 逐行打印sheet1数据
        if sheet1.row_values(i)[4] == 'catering':
            # print(sheet1.row_values(i)[6])
            cateringTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'guid':
            # print(sheet1.row_values(i)[6])
            guidTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'ticket':
            # print(sheet1.row_values(i)[6])
            ticketTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'hotel':
            # print(sheet1.row_values(i)[6])
            hotelTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'meeting':
            # print(sheet1.row_values(i)[6])
            meetingTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'other':
            # print(sheet1.row_values(i)[6])
            otherTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'party':
            # print(sheet1.row_values(i)[6])
            partyTotal += sheet1.row_values(i)[6]
        if sheet1.row_values(i)[4] == 'training':
            # print(sheet1.row_values(i)[6])
            trainingTotal += sheet1.row_values(i)[6]

    print(otherTotal)

def aa():
    workBook2 = xlrd.open_workbook('templates/xls/团队预定订单数据.xls')
    sheet2 = workBook2.sheets()[0]

    aa = Counter(sheet2.col_values(5))
    print(aa)  # Counter({'other': 7862, 'catering': 2605, 'ticket': 2486, 'hotel': 1343, 'meeting': 979, 'training': 617, 'guid': 407, 'party': 84})
    bb=sorted(set(aa))
    print(aa)

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    k = 0
    k = 0

    sheet1_nrows = sheet2.nrows  # 获得行数
    for i in range(sheet1_nrows):  # 逐行打印sheet1数据
        if sheet2.row_values(i)[5] == '湖南嗨周末国际旅行社有限公司':
            # print(sheet1.row_values(i)[6])
            a += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '长沙幸福时光国际旅行社有限公司':
            b += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湖南新麦乐国际旅行社有限公司':
            # print(sheet1.row_values(i)[6])
            c += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湖南益阳平安国际旅行社有限公司':
            d += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '岳阳宝中旅游国际旅行社有限公司':
            # print(sheet1.row_values(i)[6])
            e += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '株洲市火车头旅行社有限责任公司':
            f += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '岳阳康辉国际旅行社有限公司':
            # print(sheet1.row_values(i)[6])
            g += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湘潭潇湘风情旅业发展有限公司':
            h += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湖南湘聚天下国际旅行社有限公司':
            # print(sheet1.row_values(i)[6])
            i += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湖南湘聚天下国际旅行社有限公司益阳分公司':
            j += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '岳阳海航乐游国际旅行社有限公司':
            # print(sheet1.row_values(i)[6])
            k += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湖南研学旅文化传媒有限公司':
            l += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '衡阳市飞扬国际旅行社有限公司':
            m += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '湖南海外旅游常德有限公司':
            n += sheet2.row_values(i)[8]
        if sheet2.row_values(i)[5] == '黄山中国国际旅行社有限公司太平分公司':
           o += sheet2.row_values(i)[8]


def bb():
    with open('/templates/xls/团队预定订单数据.xls') as csvfile:
        sp

if __name__ == '__main__':
   aa();