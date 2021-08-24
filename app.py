from flask import Flask, render_template
import xlrd
import xlwt
from collections import Counter
import pandas as pd

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()

@app.route('/aaa')
def aaa():
    return render_template("index2.html")

@app.route('/bbb')
def bbb():
    return render_template("index3.html")

@app.route('/ccc')
def ccc():
    return render_template("bigdata.html")

@app.route('/ddd')
def ddd():
    return render_template("survey.html")

@app.route('/test')
def test():
    # workBook1 = xlrd.open_workbook('D:\\ProgramFiles\\docTest\excel\\TeamSettlementDetails.xls')
    workBook1 = xlrd.open_workbook('templates\\xls\\团队结算明细.xls')
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

    lastNamedict=[]
    bb(lastNamedict)

    # 地图展示
    province=[]
    nums=[]
    map(province,nums)

    return render_template("test.html", moduleName=moduleName, cateringTotal=cateringTotal,
                           guidTotal=guidTotal,
                           ticketTotal=ticketTotal, hotelTotal=hotelTotal, meetingTotal=meetingTotal,
                           otherTotal=otherTotal, partyTotal=partyTotal, trainingTotal=trainingTotal,
                           lastNamedict=lastNamedict,
                           province=province,nums=nums)


@app.route('/a')
def a():
    province = []
    nums = []
    map(province, nums)
    return render_template("a.html",province=province,nums=nums)

@app.route('/b')
def b():
    natu=[]
    num=[]
    naturePerson(natu,num)
    return render_template("b.html",natu=natu,num=num)

# 各个景区的人流量
def naturePerson(natu,num):
    wb = xlrd.open_workbook("templates/xls/团队预定订单旅游板块明细数据.xls")
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)
    # print(total_list)

    namedict = {}
    for items in total_list:
        if items[1] == None or items[1] == "TICKETGROUP_NAME":
            continue
        else:
            if items[1] in namedict.keys():
                namedict[items[1]] += items[3]
            else:
                namedict.setdefault(items[1], items[3])

    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    # print(sortNamedict)

    lastNamedict = []
    for i in range(30):
        lastNamedict.append(sortNamedict[i])
    # print(lastNamedict)

    for i in lastNamedict:
        natu.append(i[0])
        num.append(i[1])

# 旅行社区排行榜
def bb(lastNamedict):
   wb = xlrd.open_workbook("templates/xls/aaa.xls")
   ws = wb.sheet_by_index(0)
   # print(ws.row_values(0))  # 每一行作为一个列表
   total_list = []
   for row in range(ws.nrows):
      row_list = ws.row_values(row)
      total_list.append(row_list)

   namedict = {}
   for items in total_list:
      if items[5] == None or items[5] == "AGENT_ACCOUNTNAME":
         continue
      else:
         if items[5] in namedict.keys():
            namedict[items[5]] += items[8]
         else:
            namedict.setdefault(items[5], items[8])

   sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)

   for i in range(30):
      lastNamedict.append(sortNamedict[i])


# 地图展示  中国各省份人流量
def map(province,nums):
    work = xlrd.open_workbook('templates/xls/地图.xls')
    sheet = work.sheets()[0]
    data = sheet.col_values(0)
    tem = Counter(data)
    fidata = sorted(tem.items(), key=lambda tem: tem[1], reverse=True)

    for i in fidata:
        province.append(i[0])
        nums.append(i[1])



if __name__ == '__main__':
    app.run()
