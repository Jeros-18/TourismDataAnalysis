
import xlrd
import xlwt
from collections import Counter
import pandas as pd
from datetime import datetime
from xlrd import xldate_as_tuple

import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算

# import jieba
import collections
import re
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

'''
danGao
'''

# 驴妈妈 总评 xxxxx
def lmm():
    fn = open('../templates/txt/驴妈妈.txt', 'r', encoding='utf-8')  # 打开文件
    img = Image.open('../templates/img/xihongshi.jpg')  # 打开遮罩图片
    could(fn, img)


# 驴妈妈 项目
def lmmNatue():
    wb = xlrd.open_workbook("../templates/xls/comment_驴妈妈.xls")
    n = 3
    name = "票类型"
    print("驴妈妈 项目", num(wb,n,name)) # [('喊泉1元体验票', 692), ('成人票（含玻璃栈道+玻璃桥）', 175), ('驴迹电子导览（不含门票）', 160), ('飞拉达 - 体验票', 149),
# 驴妈妈 喊泉1元体验票 舆情分析
def lmm1():
    fn = open('../templates/txt/驴妈妈-喊泉.txt', 'r', encoding='utf-8')  # 打开文件
    img = Image.open('../templates/img/tree.jpg')  # 打开遮罩图片
    could(fn, img)
    plt.savefig('../templates/could/lmm1.jpg', dpi=500)

# 驴妈妈 玻璃栈道+玻璃桥 舆情分析
def lmm2():
    fn = open('../templates/txt/驴妈妈-玻璃栈道桥.txt', 'r', encoding='utf-8')  # 打开文件
    img = Image.open('../templates/img/tree.jpg')  # 打开遮罩图片
    could(fn, img)
# 驴妈妈 驴迹电子导览 舆情分析
def lmm3():
    fn = open('../templates/txt/驴妈妈-驴迹电子导览.txt', 'r', encoding='utf-8')  # 打开文件
    img = Image.open('../templates/img/tree.jpg')  # 打开遮罩图片
    could(fn, img)

# 美团
def meiTuan():
    wb = xlrd.open_workbook("../templates/xls/comment_美团.xls")
    n = 1
    name = "套餐"
    print("美团 项目", num(wb, n, name))
# 石燕湖景区悬崖秋千体验票
def meiQiuQian():
    a=1
#  石燕湖景区晃桥体验票
def meiHuangQiao():
    a=1
# 石燕湖地下峡谷漂流
def meiXiaGu():
    a=1



def could(fn,img):    # 读取文件

    string_data = fn.read()  # 读出整个文件
    fn.close()  # 关闭文件

    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    text = re.sub(pattern, '', string_data)  # 将符合模式的字符去除
    # print(text)

    #分词
    cut = jieba.cut(text)
    string = ' '.join(cut)
    # print(string)
    # print(len(string))


    img_array = np.array(img)   #将图片转换为数组
    wc = WordCloud(
        # background_color='black',
        mask=img_array,
        font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
    )
    wc.generate_from_text(string)



    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')     #是否显示坐标轴

    # plt.show()    #显示生成的词云图片

def num(wb,n,name):
    ws = wb.sheet_by_index(0)
    # print(ws.row_values(0))  # 每一行作为一个列表
    total_list = []
    for row in range(ws.nrows):
        row_list = ws.row_values(row)
        total_list.append(row_list)

    namedict = {}
    for items in total_list:
        if items[n] == None or items[n] == name:
            continue
        else:
            if items[n] in namedict.keys():
                namedict[items[n]] += 1
            else:
                namedict.setdefault(items[n], 1)

    sortNamedict = sorted(namedict.items(), key=lambda namedict: namedict[1], reverse=True)
    return sortNamedict


if __name__ == '__main__':
    meiTuan()