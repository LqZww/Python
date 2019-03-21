#格式化字符串 

str1 = "version" 
num = 1.0
format = "%s" % str1 
print (format) 
format = "%s %d" %(str1, num) 
print (format)


#字符串对齐
word = "version3.0"                       #10个字符 
print (word.center(20))                   #在20字符宽度中位于中间。因此，输出：version3.0 两边各5个空格 
print (word.center(20, "*"))              #*****version3.0***** 
print (word.ljust(0))                     #ljust()使输出结果左对齐 
print (word.rjust(20))                    #在20字符宽度中右对齐 
print("%30s" % word)                      # "%30" 表示先输出30个空格

#strip()去掉转义字符 
word = "\thello world\n" 
print ("strip()后输出:",  word.strip())    #strip()后输出:hello world （去掉了转义字符后输出） 
print ("lstrip()后输出:", word.lstrip())   #lstrip()后输出:hello world （去掉了句首转义字符\t，句尾\n保留） 
print ("rstrip()后输出:", word.rstrip())   #rstrip()后输出:hello world（去掉了\n，保留句尾句首转义字符\t）

# 使用join()连接字符串
strs = ["hello ", "world ", "hello ", "China "]
result = "".join(strs)
print (result)                       #hello world hello China


# 使用reduce()连接字符串
from functools import reduce
import operator
strs = ["hello ", "world ", "hello ", "China "]
result = reduce(operator.add, strs, "")
print (reduce)


# 切片语法

                             # 从第start个索引到第end个索引，步长为step          

# 特殊切片截取子串
str1 = "hello world"
print (str1[0:3])                 # hell
print (str1[::2])                  # hlowrd
print (str1[1::2])                # el ol"



# 使用split()获取子串
sentence = "Bob said: 1, 2, 3, 4"
print (sentence.split())              # 使用空格分割  ['Bob', 'said:', '1,', '2,' '3', '4']
print (sentence.split(","))           # 使用逗号分割
print (sentence.split(",",2))        # 使用两个逗号分割   



# startswith()用法
word = "hello world"
print ("hello" == word[0:5])
print (word.startswith("hello"))



# 循环输出反转的字符串
def reverse(s):
    out = ""
    li = list(s)
    for i in range(len(li), 0, -1):
        out += "".join(li[i-1])
    return out


# 方法二
def reverse(s):
    li = list(s)
    li.reverse()
    s = "".join(li)
    return s
print (reverse("hello world"))


# find()函数
sentence = "this is a apple."
print (sentence.find("a"))                  # 8
print (sentence.rfind("a"))                 # 10


# replace()函数
sentence = "hello world, hello China"
print (sentence.replace("hello","hi"))            # hi world, hi China
print (sentence.replace("hello","hi", 1))        # hi world, hello China
print (sentence.replace("abc","hi"))              # hello world, hello China

