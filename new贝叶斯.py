'''
一、朴素贝叶斯算法背景知识
    1.概率和条件概率
      P(A)=m/n        n是样本空间S的样本总数，A是S的任一子集，m是A的样本数
      P(B|A)=k/m      B是S的任一子集，k是AB的样本数
      P(B|A)=k/m=(k/n)/(m/n)=P(BA)/P(A)
      P(B|A)*P(A)=P(BA) 同理  P(A|B)*P(B)=P(BA)
    2.朴素贝叶斯公式：
      P(A|B)*P(B)=P(B|A)*P(A)
      P(A1|B)=P(B|A1)*P(A1)/P(B)
      P(A2|B)=P(B|A2)*P(A2)/P(B)
      max{ P(A1|B),P(A2|B)} <==> max{ P(B|A1)*P(A1),P(B|A2)*P(A2)}
      P(A|B)=P(A) <==> 则 P(AB)=P(A)*P(B)
      当 s1s2s3...sj 相互独立时：
      P(s1s2s3...sj)=P(s1)*P(s2)*...*P(sj)
    3.全概率公式：
      P(A+B)=P(A)+P(B)-P(AB)
      AB=0   <==>  P(A+B)=P(A)+P(B)
      当 s1s2s3...sj 互斥时：
      P(s1+s2+s3+...+sj)=P(s1)+P(s2)+...+P(sj)
二、朴素贝叶斯算法：
    1.给出训练一些样本和对这些训练样本的一个分类
    2.取出每个样本中的样本点（去掉重复的），创建一个样本空间（所有样本点（去掉重复的）的集合）
    3.根据每一个训练样本，计算每个样本点在样本空间中出现的次数和位置。
    4.将样本空间S分为两部分：A={非广告样本点子集}和B={广告样本点子集}
      A中每个样本点的条件概率P(Xk|A)=1/len(A)
      B中每个样本点的条件概率P(Yk|B)=1/len(B)
      P(A)=A中样本点个数/S中的样本点总数
      P(B)=B中样本点个数/S中的样本点总数
      P(TP|A)=TP中非广告样本点个数/len(A)
      P(TP|B)=TP中广告样本点个数/len(B)
      计算每个样本点的条件概率
    5.给出一个测试样本TP
      p=max{ P(A|TP),P(B|TP)} <==> p=max{P(TP|A)*P(A),P(TP|B)*P(B)}
      测试样本的分类是p对应的类别（A或B） 。
    6.定义测试函数
      1)创建样本空间
      2)调用traingNB函数
      3)计算每个样本点的条件概率（P(样本点|类别))
      4)给出测试样本
      5)将测试样本转换为数字向量
      6)调用testingNB函数，给出测试样本所属类别
    7.调用测试函数

'''
from numpy import *

# 示例：词汇分类：  1.广告    0.非广告
# 1.给出6个训练样本Xi,0<=i<=5
tringSamples = [['感冒', '高血压', '心绞痛', '肺炎', '头晕'],  # 含若干个样本点
                ['感冒', '头晕', '喷嚏', '恶心', '高血压', '头晕', '咳嗽'],
                ['咳嗽', '高血压', '心绞痛', '肺炎', '头晕', '发烧', '癫痫'],
                ['感冒', '头晕', '喷嚏', '腹泻', '高血压', '咳嗽'],
                ['高血压', '心绞痛', '肺炎', '头晕', '发烧', '癫痫', '休克'],
                ['感冒', '咳嗽', '发烧', '头晕', '腹泻']]
classify = [0, 1, 0, 1, 0, 1]  # 给出1个样本分类 Y=(0,1,0,1,0,1)


# 2.取出每个样本中的样本点（去掉重复的），创建一个有序的样本空间
def createSampleSpace(tringSamples):
    SamplesSpace = set([])  # 创建一个空集
    for Samples in tringSamples:
        SamplesSpace = SamplesSpace | set(Samples)  # 创建集合的并集
    return list(SamplesSpace)


# 3.计算每个样本点在样本空间中出现的次数和位置，存放在SamplesVec中，
def SamplesToVector(SamplesSpace, Samples):
    SamplesVec = [0] * len(SamplesSpace)  # 创建一个元素都为0，长度为len(SamplesSpace)的列表
    for sp in Samples:
        if sp in SamplesSpace:
            SamplesVec[SamplesSpace.index(sp)] += 1  # Samples中每个样本点sp在SamplesSpace位置和出现的次数
        else:
            print('The sample: %s is not in SamplesSpace!' % sp)
    return SamplesVec


# print(SamplesToVector(createSamplesSpace(tringSamples),tringSamples[1]))
#  4.根据训练样本，计算每个样本点的条件概率P(样本点|类别)
def traingNB(SamplesSpace, classify):
    row = len(tringSamples)
    col = len(SamplesSpace)
    p0Num = zeros(col)  # 避免一个概率值为0,最后的乘积也为0
    p1Num = zeros(col)  # 用来统计两类数据中，各词的词频
    p0Tatall = 0  # 用于统计0类中的总数
    p1Tatall = 0  # 用于统计1类中的总数

    trainMat = []
    for SamplesLine in tringSamples:
        trainMat.append(SamplesToVector(SamplesSpace, SamplesLine))

    # 计算每个样本点的条件概率P(Xk|Yi)=Xk个数/Yi本点的总数
    for i in range(row):
        if classify[i] == 0:
            # 样本中非广告词出现的次数
            p0Num += SamplesToVector(SamplesSpace, tringSamples[i])
            p0Tatall += sum(p0Num)  # 非广告词总数
        else:
            # 样本中广告词出现的次数
            p1Num += SamplesToVector(SamplesSpace, tringSamples[i])
            p1Tatall += sum(p1Num)  # 广告词总数

    p0V = p0Num / p0Tatall  # p0V=｛P(每个样本点|非广告)｝
    p1V = p1Num / p1Tatall  # p1V=｛P(每个样本点|广告)｝
    PA = p0Tatall / col
    PB = p1Tatall / col

    # 如果x1>x2 那么ln(x1)>ln(x2)，由于概率的值较小，取对数进行比较，避免下溢出或者浮点数舍入导致的错误
    # p1 = log(p1Num / p1Tatall)     # 在类1中的概率P(|)
    # p0 = log(p0Num / p0Tatall)     # 在类0中的概率
    # print (tringSamples)
    # print (SamplesSpace)
    # print ('P(每个样本点|非广告)',p0V)
    # print ('P(每个样本点|广告)',p1V)
    return p0Num, p1Num, p0V, p1V, PA, PB,trainMat


# 5.给出一个测试样本TP=X1+X2+X3+...+Xj，计算p=max{P(类别|样本点),0<=i<=m} p对应Yi就是测试样本的分类。
def testingNB(testVec, p0V, p1V, PA, PB):
    # p=max{ P(A|TP),P(B|TP)} <==> p=max{P(TP|A)*P(A),P(TP|B)*P(B)}
    # P(TP|A)=sum(testVec*p0V)*P(A)
    p0 = sum(testVec * p0V) * PA  # + log(PA)
    p1 = sum(testVec * p1V) * PB  # + log(PB)
    '''
    print (testVec)
    print (p0V)
    print (testVec*p0V)
    print (p1V)
    print (testVec*p1V)
    print (p0,p1)
    '''
    if p0 >= p1:
        return p0,p1,'急诊'
    else:
        return p0,p1,'非急诊'


# 6.定义测试函数
'''
1)创建样本空间
2)调用traingNB函数
3)计算每个样本点的条件概率（P(样本点|类别))
4)给出测试样本
5)将测试样本转换为数字向量
6)调用testingNB函数，给出测试样本所属类别
'''
def testing3():
    #根据训练样本，创建样本空间
    SamplesSpace = createSampleSpace(tringSamples)
    #调用traingNB函数，计算每个样本点的条件概率（P(样本点|类别)），存放在Mat矩阵中
    p0Num,p1Num,p0V,p1V,PA,PB= traingNB(SamplesSpace, classify)
    #给出测试样本
    testSamples = ['感冒', '高血压', '心绞痛']
    #将测试样本转换为数字向量
   
    testVec = SamplesToVector(SamplesSpace, testSamples)
    #调用testingNB函数，给出测试样本所属类别
    print (testSamples,'推测为： ', testingNB (testVec, p0V, p1V, PA,PB))
    #print (testVec*p1V)
    #给出测试样本
    testSamples = ['感冒', '头晕','咳嗽']
    #将测试样本转换为数字向量
    testVec = SamplesToVector(SamplesSpace, testSamples)
    #调用testingNB函数，给出测试样本所属类别
    print (testSamples, '推测为： ', testingNB (testVec, p0V, p1V,  PA,PB))
    #print (testVec*p0V)
    #print (testVec*p1V)
    #给出测试样本
    testSamples = [ '喷嚏', '头晕' , '腹泻']
    #将测试样本转换为数字向量
    testVec = SamplesToVector(SamplesSpace, testSamples)
    #调用testingNB函数，给出测试样本所属类别
    print (testSamples, '推测为： ', testingNB (testVec, p0V, p1V,  PA,PB))
    #给出测试样本
    testSamples = ['头晕','心绞痛','咳嗽']
    #将测试样本转换为数字向量
    testVec = SamplesToVector(SamplesSpace, testSamples)
    #调用testingNB函数，给出测试样本所属类别
    print (testSamples, '推测为： ', testingNB (testVec, p0V, p1V,  PA,PB))
# 7.调用测试函数


def testing():
    pass


# 7.调用测试函数
if __name__ == '__main__':
    #testing3()
    testing()
from tkinter import *
import tkinter.font

# 声明窗口
master = Tk()
# 声明窗口大小
w = Canvas(master, width=1300, height=800)
# 绘制窗口
w.pack()
SamplesSpace = createSampleSpace(tringSamples)


def drawdata(List_Elem, classfi):
    RectWith = 50  # 宽度
    RectHeight = 20  # 高度
    LR_spacing = 5  # 左右间距
    UD_spacing = 10  # 上下间距
    Color = 'white'
    titleFont = ('微软雅黑', 10, 'bold')
    for row_len, words in enumerate(classfi):
        if words == 1:
            RectColor = 'blue'
        else:
            RectColor = 'red'
        for col_len, word in enumerate(List_Elem[row_len]):
            # 绘制矩形
            w.create_rectangle((RectWith + LR_spacing) * col_len,  # 矩形起点X
                               (RectHeight + UD_spacing) * row_len,  # 矩形起点Y
                               (RectWith + LR_spacing) * col_len + RectWith,  # 矩形终点X
                               (RectHeight + UD_spacing) * row_len + RectHeight,  # 矩形终点Y
                               fill=Color)
            # 绘制文字
            w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                          (RectHeight + UD_spacing) * row_len + 10,  # 文字起点Y
                          text=word,
                          font=titleFont,
                          fill=RectColor,
                          anchor=W,
                          justify=LEFT)

#绘制样本向量
def drawSamplesSpace(List_Elem):
    RectWith = 40  # 宽度
    RectHeight = 20  # 高度
    LR_spacing = 5  # 左右间距
    UD_spacing = 10  # 上下间距
    site = 160
    titleFont = ('微软雅黑', 10, 'bold')
    row_len = 1
    for col_len, word in enumerate(List_Elem):
        # 绘制矩形
        w.create_rectangle((RectWith + LR_spacing) * col_len,  # 矩形起点X
                           (RectHeight + UD_spacing) * row_len + site,  # 矩形起点Y
                           (RectWith + LR_spacing) * col_len + RectWith,  # 矩形终点X
                           (RectHeight + UD_spacing) * row_len + RectHeight + site,  # 矩形终点Y
                           fill='white')
        # 绘制文字
        w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                      text=word,
                      font=titleFont,
                      fill='green',
                      anchor=W,
                      justify=LEFT)


#绘制 训练样本
def drawtraingNB(trainMat):
    RectWith = 40  # 宽度
    RectHeight = 20  # 高度
    LR_spacing = 5  # 左右间距
    UD_spacing = 10  # 上下间距
    site=250
    titleFont = ('微软雅黑', 15, 'bold')
    for row_len ,SamplesVec in enumerate(trainMat):
        for col_len, word in enumerate(trainMat[row_len]):
            # 绘制矩形
            if row_len%2==0:
                if word >= 1:
                    color = 'red'
                    titleFont = ('微软雅黑', 15, 'bold')
                else:
                    color = 'green'
                    titleFont = ('微软雅黑', 10)
            elif row_len%2!=0:
                if word >= 1:
                    color = 'blue'
                    titleFont = ('微软雅黑', 15, 'bold')
                else:
                    color = 'green'
                    titleFont = ('微软雅黑', 10)
            w.create_rectangle((RectWith + LR_spacing) * col_len,  # 矩形起点X
                               (RectHeight + UD_spacing) * row_len + site,  # 矩形起点Y
                               (RectWith + LR_spacing) * col_len + RectWith,  # 矩形终点X
                               (RectHeight + UD_spacing) * row_len + RectHeight + site,  # 矩形终点Y
                               fill='white')
            # 绘制文字
            w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                          (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                          text=word,
                          font=titleFont,
                          fill=color,
                          anchor=W,
                          justify=LEFT)



# 绘制 训练样本在总样本中的位置
def drawtraing(train1, train2, p0, p1):
    RectWith = 40  # 宽度
    RectHeight = 20  # 高度
    LR_spacing = 5  # 左右间距
    UD_spacing = 10  # 上下间距
    site = 430
    titleFont = ('微软雅黑', 15, 'bold')
    row_len = 1
    # 绘制 合并后的第一行（个数行）
    for col_len, word in enumerate(train1):

        # 绘制矩形
        if word >= 1:
            color = 'red'
        else:
            color = 'blue'
        word = int(word)
        w.create_rectangle((RectWith + LR_spacing) * col_len,  # 矩形起点X
                           (RectHeight + UD_spacing) * row_len + site,  # 矩形起点Y
                           (RectWith + LR_spacing) * col_len + RectWith,  # 矩形终点X
                           (RectHeight + UD_spacing) * row_len + RectHeight + site,  # 矩形终点Y
                           fill="white")
        # 绘制文字
        w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                      text=word,
                      font=titleFont,
                      fill=color,
                      anchor=W,
                      justify=LEFT)
    site = 450
    # 绘制 合并后的第二行（小数行）
    for col_len, word in enumerate(p0):
        # 绘制文字
        w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                      text=round(word, 3),  # 小数点3位
                      font=('微软雅黑', 10, 'bold'),
                      fill='red',
                      anchor=W,
                      justify=LEFT)
    site = 475
    # 绘制 合并后的第三行（个数行）
    for col_len, word in enumerate(train2):
        # 绘制矩形
        if word >= 1:
            color = 'blue'
        else:
            color = 'red'
        word = int(word)
        w.create_rectangle((RectWith + LR_spacing) * col_len,  # 矩形起点X
                           (RectHeight + UD_spacing) * row_len + site,  # 矩形起点Y
                           (RectWith + LR_spacing) * col_len + RectWith,  # 矩形终点X
                           (RectHeight + UD_spacing) * row_len + RectHeight + site,  # 矩形终点Y
                           fill='white')
        # 绘制文字
        w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                      text=round(word),
                      font=titleFont,
                      fill=color,
                      anchor=W,
                      justify=LEFT)

    site = 495
    # 绘制 合并后的第四行（小数行）
    for col_len, word in enumerate(p0):
        # 绘制文字
        w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                      text=round(word, 3),  # 小数点3位
                      font=('微软雅黑', 10, 'bold'),
                      fill='red',
                      anchor=W,
                      justify=LEFT)


# 绘制测试样本
def drawtesting(trainMat, s,p0p,p1p,end):
    RectWith = 40  # 宽度
    RectHeight = 20  # 高度
    LR_spacing = 5  # 左右间距
    UD_spacing = 10  # 上下间距
    site = 530 + s
    titleFont = ('微软雅黑', 15, 'bold')
    row_len = 1
    rang=10#精度
  
    p0p=round(p0p,rang)#控制精度
    p1p = round(p1p, rang)#控制精度


    for col_len, word in enumerate(trainMat):
        if word >= 1:
            if end=='急诊':
                color = 'black'
            else:
                color = 'black'
        else:
            color = 'white'
        w.create_rectangle((RectWith + LR_spacing) * col_len,  # 矩形起点X
                           (RectHeight + UD_spacing) * row_len + site,  # 矩形起点Y
                           (RectWith + LR_spacing) * col_len + RectWith,  # 矩形终点X
                           (RectHeight + UD_spacing) * row_len + RectHeight + site,  # 矩形终点Y
                           fill='white')
        # 绘制文字
        w.create_text((RectWith + LR_spacing) * col_len,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + 10 + site,  # 文字起点Y
                      text=word,
                      font=titleFont,
                      fill=color,
                      anchor=W,
                      justify=LEFT)
    site = 560 + s
    begain=0
    len=500
    for x in range(1,3):
        if end=='急诊':
            if x % 2 != 0:
                if p0p >= p1p:
                    word = p0p
                    color = 'red'
                else:
                    word = p1p
                    color = 'blue'
            else:
                if p0p >= p1p:
                    word = p1p
                    color = 'blue'
                else:
                    word = p0p
                    color = 'red'
        else:
            if x % 2 == 0:
                if p0p >= p1p:
                    word = p0p
                    color = 'red'
                else:
                    word = p1p
                    color = 'blue'
            else:
                if p0p >= p1p:
                    word = p1p
                    color = 'blue'
                else:
                    word = p0p
                    color = 'red'

        w.create_rectangle (begain,  # 矩形起点X
                           (RectHeight + UD_spacing) * row_len + site,  # 矩形起点Y
                           begain+len* (p0p*((x+2)%2)+p1p * ((x+1)%2)),  # 矩形终点X
                           (RectHeight + UD_spacing) * row_len + RectHeight + site,  # 矩形终点Y
                           fill=color)
        # 绘制文字
        w.create_text(begain,  # 文字起点X
                      (RectHeight + UD_spacing) * row_len + site+10,  # 文字起点Y
                      text=word,
                      font=titleFont,
                      fill='yellow',
                      anchor=W,
                      justify=LEFT)

        begain = len* (p0p*((x+2)%2)+p1p * ((x+1)%2))

# 定义绘画方法 让Button调用
def dw1():
    drawdata(tringSamples, classify)


def dw2():
    drawSamplesSpace(SamplesSpace)


def dw3():
    drawtraingNB(traingNB(SamplesSpace, classify)[-1])

def dw4():
    p0Num, p1Num, p0V, p1V, PA, PB,trainMat = traingNB(SamplesSpace, classify)
    drawtraing(p0Num, p1Num, p0V, p1V)



def dw5():
    # 根据训练样本，创建样本空间
  #  SamplesSpace = createSampleSpace(tringSamples)
    # 调用traingNB函数，计算每个样本点的条件概率（P(样本点|类别)），存放在Mat矩阵中
    p0Num, p1Num, p0V, p1V, PA, PB, trainMat = traingNB(SamplesSpace, classify)
    # 给出测试样本
    testSamples = ['感冒', '高血压', '心绞痛']
    testVec = SamplesToVector(SamplesSpace, testSamples)
    # 调用testingNB函数，给出测试样本所属类别
    p0p,p1p,end=testingNB(testVec, p0V, p1V, PA, PB)
    drawtesting(SamplesToVector(SamplesSpace, testSamples),0,p0p,p1p,end)




    testSamples = ['感冒', '头晕','咳嗽']
    testVec = SamplesToVector(SamplesSpace, testSamples)
    # 调用testingNB函数，给出测试样本所属类别
    p0p, p1p,end = testingNB(testVec, p0V, p1V, PA, PB)
    drawtesting(SamplesToVector(SamplesSpace, testSamples), 70,p0p,p1p,end)


# 标签
ft = tkinter.font.Font(size=15)
# 按钮
B1 = tkinter.Button(text="训练集", font=ft, fg='blue', command=dw1)
B1.place(x=1100, y=10)
B2 = tkinter.Button(text="样本空间", font=ft, fg='blue', command=dw2)
B2.place(x=1100, y=40)
B3 = tkinter.Button(text="训练训练", font=ft, fg='blue', command=dw3)
B3.place(x=1100, y=70)
B4 = tkinter.Button(text="训练结果", font=ft, fg='blue', command=dw4)
B4.place(x=1100, y=100)
B5 = tkinter.Button(text="测试样本", font=ft, fg='blue', command=dw5)
B5.place(x=1100, y=130)
mainloop()
