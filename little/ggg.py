lat = {"六月":["飞","雪"],"七月":"99","八月":"炎阳"}

del lat["八月"] #通过字典的键删除键值对
print(lat)


# print(lat.pop("七月")) #通过字典的键进行删除键值对
# print(lat)
#
# lat_1 = {"1":"123","4":"456","7":"789"}
# lat.clear()
# print(lat)

s = 'abc'

print('s contains a =', s.__contains__('a'))
print('s contains A =', s.__contains__('A'))

vv={'xxx公司':111,'99':10,'9999':00,'xxxx公司':98,'999':11,'9':0}
sortvv = sorted(vv.items(),key=lambda vv:vv[1],reverse=True)
print(sortvv)
print(type(sortvv))
list=[]
s=-1
strB = "公司"
print("--------------------")
for i in sortvv:
    s = s + 1
    if( not (strB in i[0])):
        print(sortvv[s])
        del sortvv[s]

print(sortvv,s)


print(list)


print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
strA = "xxx公司"
strB = "公司"
result = strB in strA
print(not result)
