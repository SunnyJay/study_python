#-*- coding:gb18030 -*-

'''
Python对象、数字

@author: Administrator
'''

# type()函数可以得到特定对象的类型信息
print type(42)
print type('sunnanjun')
# 类型也是对象，所有类型对象的类型是type 是所有python类型的根和所有python标准类的默认元类metaclass
print type(type(42))

# None是python的Null对象(其布尔值总是False)

#对象值比较
print 2 != 2
print 2 <> 2 #这种写法不建议

#对象引用比较（即对象身份比价）id方法与is关键字
a = 'sun'; b = 'sun';c = 'nan'
print id(a) == id(b) #与下面等同
print a is b 
print a is not c

#id方法 获得对象的引用值
print id(a), id(b)

#布尔类型 and or not
print not(a is b)

#python支持这种一个表达式多种比较操作  3<4<5
print 3<4<7
a = 4
if 2<a<5:
   print 'OK'

#标准类型内建函数 cmp str type repr或`obj` 他们都用于基本类型
print cmp(3,4) #返回-1 0 1
print str(3) #这个重要 返回对象的可读性好的字符串，对用户友好
print repr(3),`3` #注意与str的区别，这个是官方字符串表示，对python友好

#python不支持方法或函数重载！切记！
print type([]),type({}),type(())

#使用isinstance  首先导入types模块
import types #或from types import IntType
num=4
if type(num)==types.IntType:
    print 'is int'
if isinstance(num, int): #int其实是个类
    print 'is int'

#python不支持的类型
#char byte
#python支持的数字类型：
#整型、长整型、布尔型、双精度浮点型、十进制浮点型、复数
#python标准整型等同于c的long
#长整型加L即可
num = 12234454546545L
print num
#未来将统一整型和长整型 用户感觉不到长整型的存在，必要时整型会自动转换为长

#python除法和其他语言一样
print 1/2,1.0/2.0,8%3
#幂运算
print 3**3 #pow
#位操作符
print ~1 #按位取反

#针对数字类型的内建函数 重要
#int() long() float() complex() bool()  注意python是有布尔类型的
print int(23.4),float(4),bool(3),bool(0),bool(-1)
#abs() pow() round()四舍五入
print abs(-4),pow(3,3)

#进制转换函数 直接返回对象进制字符串 重要
#hex()  oct()
print hex(234)
print type(hex(234)) #返回类型是str

#ascii转换函数 重要 ord chr
print ord('3')
print chr(97)

#布尔类型 
#重要 数学运算中True和False分别对应1 0  可以直接运算
print 232+True
print 232+False