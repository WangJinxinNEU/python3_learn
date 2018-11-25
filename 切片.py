L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

List = list(range(10))
# print(List)
# print(List[-3:])
# print(List[-1:-3])
print(List[:1])
print(List[1:])
print(List[-1:])
print(List[:-1])


########
# 练习:利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
########
####自己写的程序:
# def trim(input):
#     index1 = 0
#     index2 = len(input) - 1
#     #print(len(input))
#     for i in range(len(input)-1):
#         if (i < len(input)-1):
#             if ((input[i] == ' ') and (input[i+1] != ' ')):
#                 index1 = i
#                 print("index1= ",index1)
#             if ((input[i] != ' ') and (input[i+1] == ' ')):
#                 index2 = i
#                 print("index2 =",index2)
#     print(input[index1:index2+1])
#     if (index1 == 0):
#         out = input[index1:index2 + 1]
#         return out
#     else:
#         out = input[index1+1:index2 + 1]
#         return out


#  大神的程序,递归解决问题
def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    if s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')


#网站上的程序：
