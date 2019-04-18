'''
for s in "PYTHON 3x is new":
    if s == 'x':
        break   #终止循环
        print('.',end='')   #x后面的都不显示
    print(s,end='')
'''



'''
for s in "PYTHON 3.x is new":
    if s == "3" or s == 'x':
        continue            #不执行其后缩进相同的语句
        print('',end='')    #不显示3和x
    print(s,end='')
print('-----不显示3和x')
'''


while True:
    try:        #正常执行下面两行代码
        a = eval(input('请输入一个数字：'))
        print(a)
        break
    except:     #异常处理分支执行下面代码
        print('请你输入一个数字')
