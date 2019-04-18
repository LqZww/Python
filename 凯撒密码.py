'''输出1~125Unicode编码'''
'''for i in range(1,126):
    print(chr(i),end=' ')'''

'''26个字母'''
'''for p in range(26):
    print(chr(97+p),end=" ")
print('\n')



for p in  range(26):
    print((p+3)%26,end=" ")
print('\n')
'''



'''凯撒加密'''
inputxt=input("请输入一段文本:")
s=''#保存加密结果
for p in inputxt:
    if 'a'<= p <= 'z':
        #print(chr(97+(ord(p)-97+3)%26,end="")
        s=s+chr(97+(ord(p)-97+3)%26)
    elif 'A' <= p <='Z':
        s=s+chr(65+(ord(p)-65+3)%26)
    elif 0x4E00 <= ord(p) <=0x9FA5:
        s=s+chr(ord(p)+3)
    else:
        s=s+chr(ord(p)+3)
print('加密结果='+s+'\n')
        
'''凯撒解密'''
c=''#保存解密结果
for p in s:
    if 'a' <= p <='z':
        c=c+chr(97+(ord(p)-97-3)%26)
    elif 'A' <= p <='Z':
        c=c+chr(65+(ord(p)-65-3)%26)
    elif 0x4E00 <= ord(p) <=0x9FA5:
        c=c+chr(ord(p)-3)
    else:
        c=c+chr(ord(p)-3)
print('解密结果='+c+'\n')
