import xlrd
import xlwt
from collections import Counter
import pandas as pd


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
# 右2
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


if __name__ == '__main__':
    b();
