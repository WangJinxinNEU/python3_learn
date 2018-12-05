g = (x * x for x in range(10))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# a = 5
# b = 1
# a, b = b, a + b
#
# b = a + b
#
# def fabi(input):
#     first=1
#     second=1
#     index =2
#     result=2
#     print(first)
#     print(second)
#     while index < input:
#
#         result=first+second
#         print(result)
#         first=second
#         second=result
#         index = index +1
#
# print(fabi(6))

n=[1]
n=n+[0]

# for i in range(len(n)):
#     print(i)
n=n[-1]+n[0]
print(n)



# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    N = [1]
    while True:
        yield N
        N = N + [0]
        N = [N[i-1] + N[i] for i in range(len(N))]

def triangles1():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]



