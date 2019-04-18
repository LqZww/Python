'''
#输入一个年份，判断是否为闰年
year = eval(input('请输入一个年份：'))
if(year % 4 == 0 and year % 100 > 0) or (year % 400 == 0):
    print(year,"是闰年")
else:
    print(year,"不是闰年")
'''

'''
#将百分制成绩转换为五分制成绩
score = eval(input("请输出一个百分制成绩："))
if score >= 90.0:
    grade = "A"
elif score >= 80.0:
    grade = "B"
elif score >= 70.0:
    grade = "C"
elif score >= 60.0:
    grade = "D"
else:
    grade = "E"
print("END")
print("对应的五分制成绩是:",format(grade))
'''

'''
#输出1~10偶数之积
fac = 1
for i in range(2,11,2):
    fac = fac * i
    print(i,end=' ')
print("\n fac=",fac)

#将26个小写英文字母逆序隔一个输出一个
for i in range(25,-1,-2):
    print(chr(i+97),end=" ")
'''

'''
#遍历字符串中各字符出现的次数
s = 'I love you more than i can say'
for i in set(s):
    print(i,"出现",s.count(i),"次")
print("字符总数：",len(s),"不重复字符数：",len(set(s)))

#遍历列表
l = ['鹅鹅鹅','曲项向天歌','白毛浮绿水','锄禾日当午']
for i in l:
    print(i)
'''


#列表推导式
lis = [x*x for x in range(1,11)]
print(lis)
lis = [x*x for x in range(1,11) if x % 2 == 0]
print(lis)

#字典推导式
dic = {x:x**2 for x in (2,4,6)}
print(dic)

#集合推导式
s = {x for x in 'abracadabra' if x not in 'abc'}
print(s)




