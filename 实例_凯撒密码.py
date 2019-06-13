
#示例3.1:凯撒加密
inputxt=input("请输入一段文本：")
s=''#保存加密结果
for p in inputxt:
    if 'a'<= p <='z':
        #print(chr(97+(ord(p)-97+3)%26),end="")
        s=s+chr(97+(ord(p)-97+3)%26)
    elif 'A'<= p <='Z':
        #print(chr(65+(ord(p)-65+3)%26),end="")
        s=s+chr(65+(ord(p)-65+3)%26)
    elif 0x4E00 <= ord(p) <=0x9FA5:
        #print(chr(ord(p)+3),end="")
        s=s+chr(ord(p)+3)
    else:
        #print(chr(ord(p)+3),end=" ")
        s=s+chr(ord(p)+3)     
print('加密结果='+s+'\n')

#示例3.2:凯撒解密
c='' #保存解密结果
for p in s:
    if 'a'<= p <='z':
        #print(chr(97+(ord(p)-97-3)%26),end="")
        c=c+chr(97+(ord(p)-97-3)%26)
    elif 'A'<= p <='Z':
        #print(chr(65+(ord(p)-65-3)%26),end="")
        c=c+chr(65+(ord(p)-65-3)%26)
    elif 0x4E00 <= ord(p) <=0x9FA5:
        #print(chr(ord(p)-3),end="")
        c=c+chr(ord(p)-3)
    else:
        #print(chr(ord(p)-3),end=" ")
        c=c+chr(ord(p)-3)
print('解密结果='+c+'\n')
