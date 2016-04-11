#-*- coding:gb18030 -*
'''
Created on 2016年4月8日
函数
主要来自廖雪峰
@author: Administrator
'''
# 高阶函数概念：
#    把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#####################
# map/reduce
#####################

#Python内建了map()和reduce()函数。
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数"依次"作用到序列的"每个"元素，并把结果作为新的list返回。
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算.

#实现 int()函数，你完全可以自己写一个把字符串转化为整数的函数：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

print str2int('353467')

#####################
# filter  重要
# Python内建的filter()函数用于过滤序列。
#####################

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n % 2 == 1  #True的保留
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# 结果: [1, 5, 9, 15]


#############################
# sorted 重要
##############################

# Python内置的sorted()函数就可以对list进行排序
print sorted([36, 5, 12, 9, 21])

#此外，sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数：

def mycmp(x, y): #自定义一个倒序排序
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], mycmp)


#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
#现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以：

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)