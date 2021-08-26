import xlrd
import xlwt
from collections import Counter
import pandas as pd
from datetime import datetime
from xlrd import xldate_as_tuple

def a():
    workBook = xlrd.open_workbook('../templates/xls/团队结算明细.xls')
    mouduleName = []
    totalPay = []
    sheet = workBook.sheets()[0]
    mouduleName1 = sheet.col_values(3) # 业务模块
    # print(mouduleName1)
    totalPay1 = sheet.col_values(6) # 结算金额
    # print(totalPay1)
    modulePay = dict(zip(mouduleName1,totalPay1))
    print(modulePay)

# 次数+金额 模板
def ww():
   wb = xlrd.open_workbook("../templates/xls/团队预定订单数据.xls")
   ws = wb.sheet_by_index(0)
   print(ws.row_values(0))  # 每一行作为一个列表
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
            namedict[items[5]]["出现次数"] += 1
            namedict[items[5]]["累计认购金额"] += items[8]
         else:
            namedict.setdefault(items[5], {})
            namedict[items[5]].setdefault("出现次数", 1)
            namedict[items[5]].setdefault("累计认购金额", items[8])
   print(namedict)

   print("-----------------前30个-------------------")
   # 前20个
   lastNamedict = []
   for i in range(30):
       lastNamedict.append(sortNamedict[i])
   print(lastNamedict)

# 地图展示 省份-人流量 [[[
def map():
    province=[]
    nums=[]
    work = xlrd.open_workbook('../templates/xls/地图.xls')
    sheet = work.sheets()[0]
    data = sheet.col_values(0)
    tem = Counter(data)
    fidata = sorted(tem.items(), key=lambda tem: tem[1], reverse=True)
    print(fidata)
    for i in fidata:
        province.append(i[0])
        nums.append(i[1])
    lastNamedict = []
    for i in range(17):
        lastNamedict.append(fidata[i])
    print(lastNamedict)

# 旅行社区排行榜 [[[[
def lxingshe():
   lastNamedict=[]
   wb = xlrd.open_workbook("../templates/xls/aaa.xls")
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
   print(lastNamedict)


# 消费模块占比 [[[[
def b():
    wb = xlrd.open_workbook("../templates/xls/团队结算明细.xls")
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)

    namedict = {}
    for items in total_list:
        if items[3] == None or items[3] == "MODULE_NAME":
            continue
        else:
            if items[3] in namedict.keys():
                namedict[items[3]] += items[6]
            else:
                namedict.setdefault(items[3], items[6])
    # print(namedict)

    # print("-----------------sort-------------------")
    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    print(sortNamedict)

    # print("-----------------前30个-------------------")
    # 前20个

# 不同支付方式使用频率情况 【【【【
def payNum1():
    wb = xlrd.open_workbook('../templates/xls/团队结算支付明细.xls')
    sheet = wb.sheets()[0]
    pay = sheet.col_values(4)  # 支付方式

    payNum = Counter(pay)
    paySort = sorted(payNum.items(),key=lambda payNum:payNum[1])
    print(paySort)

def payNum2():
   wb = xlrd.open_workbook("../templates/xls/团队结算支付明细.xls")
   ws = wb.sheet_by_index(0)
   print(ws.row_values(0))  # 每一行作为一个列表
   total_list = []
   for row in range(ws.nrows):
      row_list = ws.row_values(row)
      total_list.append(row_list)

   namedict = {}
   for items in total_list:
      if items[4] == None or items[4] == "PAY_TYPE_NAME":
         continue
      else:
         if items[4] in namedict.keys():
            namedict[items[4]] += 1

         else:
            namedict.setdefault(items[4], 1)

   payType=[]
   num=[]
   for i in namedict:
        payType.append(i[0])
        num.append(i[1])

   print(namedict)
   print(payType)
   print(num)


# 不同支付方式消费金额情况  【【【
def payMoney():
    wb = xlrd.open_workbook('../templates/xls/团队结算支付明细.xls')
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)

    namedict = {}
    for items in total_list:
        if items[4] == None or items[4] == "PAY_TYPE_NAME":
            continue
        else:
            if items[4] in namedict.keys():
                namedict[items[4]] += items[5]
            else:
                namedict.setdefault(items[4], items[5])
    # print(namedict)

    # print("-----------------sort-------------------")
    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    print(sortNamedict)

# 餐厅人流量【【【
def hangPerson():
    wb = xlrd.open_workbook('../templates/xls/团队预定订单餐饮板块明细数据.xls')
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)

    namedict = {}
    for items in total_list:
        if items[4] == None or items[4] == "FRESTAURANT_NAME":
            continue
        else:
            if items[4] in namedict.keys():
                namedict[items[4]] += items[7]
            else:
                namedict.setdefault(items[4], items[7])

    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    print(sortNamedict)

    lastNamedict = []
    for i in range(6):
        lastNamedict.append(sortNamedict[i])
    print(lastNamedict) #[('融景餐厅', 116211.0), ('金茂酒店', 33679.0), ('古堡餐厅', 15499.0), ('土菜馆', 13487.0), ('活鱼村', 9639.0), ('陶令餐厅', 6304.0)]

# 会议室受欢迎程度---每个会议被预约了多少次
def roomNum():
    wb = xlrd.open_workbook("../templates/xls/团队预定订单会议板块明细数据.xls")
    ws = wb.sheet_by_index(0)
    print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)

    namedict = {}
    for items in total_list:
        if items[3] == None or items[3] == "PAY_TYPE_NAME":
            continue
        else:
            if items[3] in namedict.keys():
                namedict[items[3]] += 1
            else:
                namedict.setdefault(items[3], 1)

    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)

    print(sortNamedict) # [('多功能厅', 721), ('金茂厅', 683), ('山庄会议室', 611), ('香樟厅', 493), ('石燕厅', 371), ('1号会议室', 311), ('六号会议室', 296), ('一号会议室', 249), ('阳光厅', 227), ('五号会议室', 116), ('贵宾厅', 69), ('千人大会场', 48), ('四号会议室', 9), ('金茂5号会议室', 7), ('ROOMNAME', 1)]
    lastNamedict=[]
    for i in range(12):
      lastNamedict.append(sortNamedict[i])
    print(lastNamedict)

# 每个会议室的总营业额 有bug
def roomMoney():
    wb = xlrd.open_workbook('../templates/xls/团队预定订单会议板块明细数据.xls')
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)
    # print(total_list)

    namedict = {}
    for items in total_list:
        if items[3] == None or items[3] == "ROOMNAME":
            continue
        else:
            if items[3] in namedict.keys():
                namedict[items[3]] += items[4]
            else:
                namedict.setdefault(items[3], items[4])

    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    print(sortNamedict)

# 团队类型 占比 扇形图  [[[[
def teamType():
    wb = xlrd.open_workbook("../templates/xls/团队类型.xls")
    sheet = wb.sheets()[0]
    pay = sheet.col_values(0)  # 支付方式

    payNum = Counter(pay)
    paySort = sorted(payNum.items(), key=lambda payNum: payNum[1])
    print(paySort) # [('招待', 83), ('同行', 1447), ('散客班', 2062), ('总代', 23114), ('直客', 38830)]

# 各个景区的人流量 [[[[[
def naturePerson():
    wb = xlrd.open_workbook("../templates/xls/团队预定订单旅游板块明细数据.xls")
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
    for i in range(32):
        lastNamedict.append(sortNamedict[i])
    print(lastNamedict)


# 月消费额
def monthPay():
    wb = xlrd.open_workbook('../templates/xls/团队结算支付明细.xls')
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    cols3 = ws.col_values(3)  # 获得第3列数据
    print(cols3)
    cols32 = xldate_as_tuple(cols3,1)
    cols33 = datetime(*cols32).strftime('%y/%m')

    c1=ws.cell(1,3).value #获取第2行第4列的内容
    c2=xldate_as_tuple(c1,0)
    c3=datetime(*c2).strftime('%y/%m')
    # print(c3)

    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)
    # print(total_list)

    namedict = {}
    for items in total_list:
        if items[3] == None or items[3] == "PAY_DATE":
            continue
        else:
            if items[3] in namedict.keys():
                namedict[items[3]] += items[5]
            else:
                namedict.setdefault(items[3], items[5])
    # print(namedict)

    # print("-----------------sort-------------------")
    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    # print(sortNamedict)

def monbb():
    wb = xlrd.open_workbook('../templates/xls/团队结算支付明细.xls')
    ws = wb.sheet_by_index(0)
    c1 = ws.cell(1, 2).value
    print(c1)

# 拓展项目预约次数
def tuoZhan():
    wb = xlrd.open_workbook("../templates/xls/团队预定订单拓展培训板块明细数据.xls")
    ws = wb.sheet_by_index(0)
    print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)

    namedict = {}
    for items in total_list:
        if items[3] == None or items[3] == "PAY_TYPE_NAME":
            continue
        else:
            if items[3] in namedict.keys():
                namedict[items[3]] += 1
            else:
                namedict.setdefault(items[3], 1)

    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)

    print(
        sortNamedict)  # [('多功能厅', 721), ('金茂厅', 683), ('山庄会议室', 611), ('香樟厅', 493), ('石燕厅', 371), ('1号会议室', 311), ('六号会议室', 296), ('一号会议室', 249), ('阳光厅', 227), ('五号会议室', 116), ('贵宾厅', 69), ('千人大会场', 48), ('四号会议室', 9), ('金茂5号会议室', 7), ('ROOMNAME', 1)]
    lastNamedict = []
    for i in range(12):
        lastNamedict.append(sortNamedict[i])
    print(lastNamedict)

# 融景餐厅 中午晚餐预定次数
def rongjinNum():
   wb = xlrd.open_workbook("../templates/xls/融景餐厅.xls")
   ws = wb.sheet_by_index(0)
   print(ws.row_values(0))  # 每一行作为一个列表
   total_list = []
   for row in range(ws.nrows):
      row_list = ws.row_values(row)
      total_list.append(row_list)

   namedict = {}
   for items in total_list:
      if items[5] == None or items[5] == "FCATEGORY_NAME":
         continue
      else:
         if items[5] in namedict.keys():
            namedict[items[5]] += 1

         else:
            namedict.setdefault(items[5], 1)

   print("融景餐厅",namedict)

# 金茂酒店 中午晚餐预定次数
def jinMao():
   wb = xlrd.open_workbook("../templates/xls/金茂酒店.xls")
   ws = wb.sheet_by_index(0)
   print(ws.row_values(0))  # 每一行作为一个列表
   total_list = []
   for row in range(ws.nrows):
      row_list = ws.row_values(row)
      total_list.append(row_list)

   namedict = {}
   for items in total_list:
      if items[5] == None or items[5] == "FCATEGORY_NAME":
         continue
      else:
         if items[5] in namedict.keys():
            namedict[items[5]] += 1

         else:
            namedict.setdefault(items[5], 1)

   print("金茂酒店",namedict)

# 古堡餐厅 中午晚餐预定次数
def guBao():
   wb = xlrd.open_workbook("../templates/xls/古堡餐厅.xls")
   ws = wb.sheet_by_index(0)
   print(ws.row_values(0))  # 每一行作为一个列表
   total_list = []
   for row in range(ws.nrows):
      row_list = ws.row_values(row)
      total_list.append(row_list)

   namedict = {}
   for items in total_list:
      if items[5] == None or items[5] == "FCATEGORY_NAME":
         continue
      else:
         if items[5] in namedict.keys():
            namedict[items[5]] += 1

         else:
            namedict.setdefault(items[5], 1)

   print("古堡餐厅",namedict)


if __name__ == '__main__':
    hangPerson();
    rongjinNum();
    guBao();