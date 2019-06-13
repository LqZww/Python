#分析一：
#一号门 二号门 三号门 
#  羊     车     羊 
#玩家选一号门，换（得车），不换（得羊）
#玩家选二号门，换（得羊），不换（得车）
#玩家选三号门，换（得车），不换（得羊）
#综上：玩家不换,得车的概率为1/3; 玩家换,得到车的概率为2/3。
#分析二：
#不换,玩家选中车的概率为1/3。
#换,换与不换是互补事件，换选中车的概率为=1-(1/3)=2/3。

import random            #引入随机函数库
change=nochange=0        #设置变量初始值
x=100
for i in range(1,x+1):
  #a=1 #车在1号门
  a=random.randint(1,3)  #车在1--3号门
  #b=1 #选择1号门
  b=random.randint(1,3)  #选择1--3号门
  if a==b:               #不换，随机生成两个数字（1到3）相等的概率=1/3         
    nochange=nochange+1
  else:                  #换，随机生成两个数字（1到3）不相等的概率=2/3 
    change=change+1
print("不换得到汽车的概率为{}".format(nochange/x))
print("换得到汽车的概率为{}".format(change/x))
print(nochange+change)




