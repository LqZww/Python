'''
1）给定数据集dataSet矩阵（m行n列，每行作为一个点，每个点有n项数据），
   计算每列的minj和maxj,0<=j<n,给定聚类个数k,计算：minj+(maxj-minj) * k个随机小数，
   得到k个点作为初始的聚类中心点，构成聚类中心矩阵centroids（k行n列）
2）计算dataSet中每个点与centroids中k个点之间的距离(共m*k个)，distEclud(Xi,Cj),0<=i<m , 0<=j<k
   计算出Xi与距离最小的中心点Cj，Xi标记为j类，j和i分别保存在clusterAssment矩阵的第1列和第2列
3）重新计算中心点的平均值Cj=mean{cjp, 0<=p<n}=sum{ cjp, 0<=p<n}/n
4）聚类中心点变化否？若有变化重复2），若无变化结束。

'''



from numpy import *
#'''
print('--------原始数据集---------')
x = [1,3,6,7,7,9,3,4,5]  # x坐标列表
y = [1,1,3,3,3,6,6,6,6]  # y坐标列表
print(list(zip(x,y)))
A = array(list(zip(x,y)))
print(A)
print (A[:1])
print (A[:,1])
m,n = shape(A)
print(m,n)
print('--------sum , mean & nan---------')
print (sum(A[:,0]))
#print (sum(A[:,0])/9)
print (mean(A[:,0]))
print (sum(A))
print (sum(A[:,0])+sum(A[:,1]))
print ((sum(A[:,0])/9+sum(A[:,1]))/9)
print (sum(A)/18)
print (mean(A))
print (mean([]))
print('--------zeros, mat,nonzero,random.rand & enumerate---------')
print(zeros((3,2)))
print(mat(zeros((3,2))))
print ([0,6,7,8],nonzero([0,6,7,8])[0])
print (nonzero(A[:,1])[0])
print (nonzero(A[:,1]== 6)[0])
print (A[nonzero(A[:,1]== 6)[0]])
print (A[[5,6,7,8]])
print(random.rand(3,1))
for i,c in  enumerate(A):
    print(i,c)
print('--------初始聚类中心---------')
k=3
C = mat(zeros((k,n)))
print(zeros((k,n)))
min0 = min(A[:,0])         # 计算第j列最小值       
max0 = max(A[:,0])         # 计算第j列最大值 
range0 = float(max0 - min0)      # 计算第j列范围
C[:,0] = min0 + range0 * random.rand(k, 1) #存第j个中心的n个值
print(C)
min1 = min(A[:,1])         # 计算第j列最小值       
max1 = max(A[:,1])         # 计算第j列最大值 
range1 = float(max1 - min1)      # 计算第j列范围
C[:,1] = min1 + range1 * random.rand(k, 1) #存第j个中心的n个值
print(C)
print('--------初始聚类结果---------')

print ('---A=',A)

#print ('---nonzero(A[:,1])=',nonzero(A[:,1]))


print('--------聚类算法结果---------')
C[0,:]=mean(A[nonzero(A[:,1] == 1)[0]])
C[1,:]=mean(A[nonzero(A[:,1] == 3)[0]])
C[2,:]=mean(A[nonzero(A[:,1] == 6)[0]])
print(C)
#'''
'''
print('--------聚类算法---------')
x = [1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9]  # x坐标列表
y = [1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3]  # y坐标列表
dataSet = array(list(zip(x,y)))
m,n= shape(dataSet) 
min0 = min(dataSet[:,0])         # 计算第j列最小值       
max0 = max(dataSet[:,0])         # 计算第j列最大值 
range0 = float(max0 - min0)      # 计算第j列范围
min1 = min(dataSet[:,1])         # 计算第j列最小值       
max1 = max(dataSet[:,1])         # 计算第j列最大值 
range1 = float(max1 - min1)      # 计算第j列范围
k=3
C = mat(zeros((3,n)))
'''
for i in range(3):
    C[i,0] = min0 + range0 *i/(k-1)
    C[i,1] = min1 + range1 *i/(k-1)
    
'''
C[:,0] = min0 + range0 * random.rand(3, 1) #存第j个中心的n个值
A= zeros((m,n))
def distEclud(X,Y):
    return sqrt(sum(power(X - Y, 2))) # 求两个向量之间的
# k-means 聚类算法
def kMeans(dataSet,k):
    Changed = True                 #来判断聚类是否结束
    while Changed:
        Changed = False
        #2)计算数据集中m个点与聚类中心中k个点之间的距离(共m*k个)，(Xi-Cj)**2 , 0<=i<m , 0<=j<k
        for i in range(m):                # 把每一行数据划分到离它最近的中心
            minD = inf
            minI = -1
            for j in range(k):
                distJI = distEclud(C[j,:], dataSet[i,:])
                if distJI < minD:       #如果i到第j个中心点更近 
                    minD = distJI
                    minI = j           # 将i行归属为j类，
            if A[i,1] != minI:
               Changed = True         # 4)如果分配发生变化，则需要继续
            A[i,:] =i,minI      # 并将第i个数据点的分配情况存入字典
        #3)重新计算中心点的平均值Cj=mean{cjp, 0<=p<n}=sum{ cjp, 0<=p<n}/n
        for c in range(k):  
            ptsInClust = dataSet[nonzero(A[:,1] == c)[0]]   # 去掉第一列等于cent的所有列
            C[c,:] = mean(ptsInClust, axis = 0)             # 算出这些数据的中心点的值
    return C,A

C,A = kMeans(dataSet,3)
print(dataSet)
print('------------------------------------------')
print (C)
print('------------------------------------------')
print (A)
print (A[:,1])
print (set(A[:,1]))
import matplotlib.pyplot as plt

#绘点函数
def xyshow(x, y, color):
    plt.figure(1, figsize=(10, 6))
    plt.plot(x, y, color )
    

for i,c in  enumerate(A[:,1]):
    print(i,c)
    c=int(c)
    if   c==0:
         color='ro'
    elif c==1:
         color='g^'
    else :
         color='ys'
    xyshow(x[i], y[i], color) 
plt.show()




'''




'''
n = shape(dataSet)[1]                #n=dataSet的列数
k=3
m=3
centroids = mat(zeros((k,n)))        # 生成k行n列矩阵，k个中心，每个中心有n个值
for j in range(n):                   # 计算k个中心的值
    minJ = min(dataSet[:,j])         # 计算第j列最小值       
    maxJ = max(dataSet[:,j])         # 计算第j列最大值 
    rangeJ = float(maxJ - minJ)      # 计算第j列范围
    centroids[:,j] = minJ + rangeJ * random.rand(k, 1) #存第j个中心的n个值
   
print (centroids)
print (centroids[:,0])
print (shape(dataSet)[1])
#print (random.rand(k, 1))
#print (rangeJ *random.rand(k, 1))
clusterAssment = mat(zeros((m,2)))
for i in range(m):
    clusterAssment[i,0]=i
for cent in range(k):   # 重新计算中心的值
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]   # 去掉第一列等于cent的所有列
            centroids[cent,:] = mean(ptsInClust, axis = 0)  # 算出这些数据的中心点的值
            print('------------PPPPPPPPPPP------------------------------')
            print (ptsInClust)
print('------------TTTTTTTTTTTT------------------------------')
clusterAssment = mat(zeros((m,2)))
print (clusterAssment[:,0].A==0)
print('------------TTTTTTTTTTTT------------------------------')
print (centroids)
print (nonzero(0)[0])
print (sum(dataSet)/6)
print ((sum(dataSet[:,0])+sum(dataSet[:,1]))/6)
print (mean(dataSet))
print (sum(dataSet[:,0])/3,+sum(dataSet[:,1])/3)


x = array([1,3,6])  # x坐标列表
y = array([2,2,2])  # y坐标列表
dataSet = array(list(zip(x,y)))

'''
'''
print (dataSet)
m,k=shape(dataSet)
print(m,k)
print (shape(dataSet)[0])
print (dataSet[:,0])
print (dataSet[:,1])
print (dataSet[:])
print (dataSet[:,:])
print (dataSet[:0])
print (dataSet[:1])
print (shape(dataSet)[0])
print (shape(dataSet)[1])
print (shape(dataSet)[1])
print('sum',sum(x-y))                 # 求两个向量之差
print('sump',sum(power(x-y, 2)))      # 求两个向量之差的平方和
print('sqr',sqrt(sum(power(x-y, 2)))) # 求两个向量之间的距离


print (random.rand(3, 1))
#nonzero函数是numpy中用于得到数组array中非零元素的索引
clusterAssment=mat(array(([[1,50],[2,50],[1,50],])))
print(clusterAssment[:,0])
k,m=nonzero(clusterAssment[:,0])
print(k,m)
ptsInClust = dataSet[k]
print(ptsInClust)
ptsInClust = dataSet[nonzero(clusterAssment[:,0] == 1)[0]]
print(ptsInClust)
clusterAssment[2,:]=3,3
print('---44------',clusterAssment[2,:])
print (sum(dataSet)/6)
print ((sum(dataSet[:,0])+sum(dataSet[:,1]))/6)
print (mean(dataSet))
print (sum(dataSet[:,0])/3,+sum(dataSet[:,1])/3)
print (mean(dataSet,axis =0))
print (mean(x))
print (max(dataSet[:,0]) )
print (mean(dataSet,axis =0))
print (mean(x))
print (max(dataSet[:,0]) )
'''

