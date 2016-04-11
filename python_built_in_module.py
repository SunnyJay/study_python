#-*- coding:utf-8 -*-
'''
Created on 2016年4月11日
常用内置模块
主要来自廖雪峰
@author: Administrator
'''

################################
# 一、collections
# 是Python内建的一个集合模块，提供了许多有用的集合类。
################################

# 1.namedtuple  可以定义一个不变的对象 作用：用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
# 

from collections import namedtuple
Point = namedtuple("Point", ['x','y']) #Ponit是一个不变的类型，其具有x y两个属性
p = Point(1, 2)
print p.x, p.y

#Point对象是tuple的一种子类
print isinstance(p, Point)

# 2.deque 重要
#   deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
#   deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('d')
print q
q.pop()
print q

# 3. Counter
#    Counter是一个简单的计数器，其key是字符，可以统计字符出现的个数
#    Counter实际上也是dict的一个子类
# 好东西 先填充进去
from collections import Counter
c = Counter()
for ch in 'programming4':
    c[ch] +=  1 #桶排序的思想
print c
    
# 3. defaultdict 
#    有默认值，并且可以设定 
#    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict。除了默认值，用法和dict完全一样
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')  #设定默认值  注意参数是一个函数对象    
dd['key1'] = 'abc'
print  dd['key1']
print dd['key2']

# 4. OrderedDict  
#    重要！它的顺序是插入的顺序，而不是key本身的顺序 不要搞错了 
#    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  #插入顺序是 a b c
print od

od = OrderedDict([('z', 1), ('x', 2), ('y', 3)])  #插入顺序是 z x y 而不是 x y z 
print od

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key


################################
# 二、hashlib
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。  摘要算法呢？摘要算法又称哈希算法、散列算法
# 不是加密算法：
#     要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
################################

import hashlib
md5 = hashlib.md5()
md5.update('sunnanjun')
print md5.hexdigest()

# md5 128位 记得！
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1() #sha1
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest() # SHA1的结果是160 bit字
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。

# 重要！
# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞，
# 比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。


################################
# 三、itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
################################


################################
# 四、XML

#    XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用。但还是建议你不要用XML，改成JSON。
#    操作XML有两种方法：DOM和SAX。
#                   DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
#                   SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。  正常情况下，优先考虑SAX，因为DOM实在太占内存。
################################

# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了

# 举个例子，当SAX解析器读到一个节点时：
# 会产生3个事件：
#     start_element事件，在读取<a href="/">时；
#     char_data事件，在读取python时；
#     end_element事件，在读取</a>时。

from xml.parsers.expat import ParserCreate
# 把处理的函数赋给paser解析器对应的handler

def start_element(name,attr):
    print name, attr
def end_element(name):
    print name
def char_data(text):
    print text     
    
parser = ParserCreate()
parser.StartElementHandler = start_element  #注册
parser.EndElementHandler = end_element
parser.CharacterDataHandler = char_data

parser.returns_unicode = True #当设置returns_unicode为True时，返回的所有element名称和char_data都是unicode，处理国际化更方便。

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
parser.Parse(xml)

