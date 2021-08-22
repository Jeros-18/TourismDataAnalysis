import xlrd, xlwt

def aa():
   # By WDL 2020-3-31

   wb = xlrd.open_workbook("templates/xls/公司推荐.xls")
   ws = wb.sheet_by_index(0)
   print(ws.row_values(2))  # 每一行作为一个列表
   total_list = []
   for row in range(ws.nrows):
      row_list = ws.row_values(row)
      total_list.append(row_list)
   print(total_list) # [['XXX公司推荐成交明细', '', '', '', ''], ['员工所在项目', '员工姓名', '推荐项目', '认购客户姓名', '累计认购金额'], ['xxxx公司', '张毅', 'xxx车', 'xxx', 444.0], ['xxxx公司', '赫尔', 'xxx车', 'xxx', 4422.0], ['xxxx公司', '将三', 'xxx车', 'xxx', 333.0], ['xxxx公司', '张三', 'xxx车', 'xxx', 222.0], ['xxxx公司', '李四', 'xxx车', 'xxx', 11.0], ['xxxx公司', '王五', 'xxx车', 'xxx', 33.0], ['xxxx公司', '张毅', 'xxx车', 'xxx', 33333.0], ['xxxx公司', '张三', 'xxx车', 'xxx', 333.0], ['xxxx公司', '张三', 'xxx车', 'xxx', 4343.0]]

   namedict = {}
   for items in total_list:
      if items[1] == None or items[1] == "员工姓名":
         continue
      else:
         if items[1] in namedict.keys():
            namedict[items[1]]["推荐数量"] += 1
            namedict[items[1]]["累计认购金额"] += items[-1]
         else:
            namedict.setdefault(items[1], {})
            namedict[items[1]].setdefault("推荐数量", 1)
            namedict[items[1]].setdefault("累计认购金额", items[-1])
   print(namedict)

   print("-----------------------------")
   for i in namedict.values():
      print(i)

   print("-----------------------------")
   for i, j in namedict.items():
      print(str(i) + ':' + j)

def cc():
   wb = xlrd.open_workbook("templates/xls/团队预定订单数据.xls")
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

def dd():
   # wb = xlrd.open_workbook("templates/xls/团队预定订单数据.xls")
   wb = xlrd.open_workbook("templates/xls/aaa.xls")
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
            namedict[items[5]] += items[8]
         else:
            namedict.setdefault(items[5], items[8])
   print(namedict)

   print("-----------------sort-------------------")
   sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
   print(sortNamedict)
   AGENT_ACCOUNTNAME = []
   MAN = []

   for i in sortNamedict:
      AGENT_ACCOUNTNAME.append(i[0])
      MAN.append(i[1])

   print("-----------------前30个-------------------")
   # 前20个
   lastNamedict = []
   for i in range(30):
      lastNamedict.append(sortNamedict[i])
   print(lastNamedict)


   # print("-----------------键-------------------")
   # print(AGENT_ACCOUNTNAME)
   # print("-----------------值-------------------")
   # print(MAN)
   '''
   print("-----------------删除键不是xxx有限公司的键值对-------------------")
   # for i in namedict:
   #    if (not i[0].__contains__("公司")):
   #       del namedict[i[0]]
   # print(namedict)
   print("-----------------sort-------------------")
   sortNamedict = sorted(namedict.items(),key=lambda namedict:namedict[1],reverse=True)
   print(sortNamedict)
   AGENT_ACCOUNTNAME=[]
   MAN=[]

   print("-----------------前20个-------------------")
# 前20个
   lastNamedict=[]
   for i in range(20):
     lastNamedict.append(sortNamedict[i])
   print(lastNamedict)
   # print("-----------------删除不符合要求的-------------------")
   # index=[1,2,3]
   # for i in reversed(index):
   #    del lastNamedict[i]
   # print(lastNamedict)

   #    AGENT_ACCOUNTNAME.append(i[0])
   #    MAN.append(i[1])
   #
   # print("-----------------键-------------------")
   # print(AGENT_ACCOUNTNAME)
   # print("-----------------值-------------------")
   # print(MAN)


'''

# def bb(AGENT_ACCOUNTNAME,MAN):
def bb():
   # wb = xlrd.open_workbook("templates/xls/团队预定订单数据.xls")
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
   # print(namedict)

   # print("-----------------sort-------------------")
   sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
   # print(sortNamedict)




   # print("-----------------前30个-------------------")
   # 前20个
   lastNamedict = []
   for i in range(30):
      lastNamedict.append(sortNamedict[i])
   print(lastNamedict)

   AGENT_ACCOUNTNAME = []
   MAN = []

   for i in lastNamedict:
      AGENT_ACCOUNTNAME.append(i[0])
      MAN.append(i[1])
   # print("-----------------键-------------------")
   # print(AGENT_ACCOUNTNAME)
   # print("-----------------值-------------------")
   # print(MAN)


def main():
   # AGENT_ACCOUNTNAME = []
   # MAN = []
   # dd(AGENT_ACCOUNTNAME,MAN)
   bb()

if __name__ == '__main__':
   main();