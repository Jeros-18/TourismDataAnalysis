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

fn = open('../templates/txt/美团-峡谷.txt', 'r', encoding='utf-8')  # 打开文件
img = Image.open('../templates/img/img1.jpg')  # 打开遮罩图片


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
    # background_color='#217093',
    mask=img_array,
    font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)



#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴

# plt.show()    #显示生成的词云图片
plt.savefig('../static/meiXiaGu3.jpg', dpi=500)
plt.show()