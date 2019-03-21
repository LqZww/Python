#利用变量求1-100的和、乘积
sum,fac,i=0,1,0
for i in range(1,101):
    sum=sum+i
    fac=fac*i
    i=i+1
print("1-100 求和 sum=",sum)
print("1-100 乘积 fac=",fac)
