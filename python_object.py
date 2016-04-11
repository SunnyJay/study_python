#-*- coding:gb18030 -*-

'''
Python对象、数字

@author: Administrator
'''
import datetime

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
#重要 数学运算中True和False分别对应1、0  可以直接运算
print 232+True
print 232+False
# 重要！！！    空集合、空字符串、所有值为0的数、None的布尔值 是False
dict={}
if not dict:
    print 'false'
if 1:
    print '1'
if not 0:
    print 'not 0'
if not None:
    print 'not none'    
    
#python没有！操作符 代替的是not
if not 3>4:
    print 'x'
    
######################################
# 时间 专题
#####################################
# 时间间隔是以秒为单位的浮点小数。
#Python 提供了一个 time \ calendar\datetime 模块可以用于格式化日期和时间

# 重要区别： time是归类在Generic Operating System Services中，换句话说， 它提供的功能是更加接近于操作系统层面的。
#         由于是基于Unix Timestamp，所以其所能表述的日期范围被限定在 1970 - 2038 之间
#         所以，如果你写的代码需要处理在前面所述范围之外的日期，那可能需要考虑使用datetime模块更好




#########################
# time 
##########################

# Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳
import time
print time.time()  #当然时间戳无法表示1970前

# 1. 获取当前时间 
# struct_time元组（类似linux c中结构体）  timetuple
# localtime方法
localtime = time.localtime(time.time())
print "本地时间为 :", localtime

# 2. 获取格式化的时间
#    最简单的获取可读的时间模式的函数是asctime():  asc!
localtime = time.asctime( time.localtime(time.time()) )  # 进一步封装
print localtime

# 3. 格式化日期, 重要！
# 使用 time 模块的 strftime 方法来格式化日期
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 4. 转换时间戳！重要  mktime
timestamp=time.mktime(time.localtime())
print timestamp
mytime =  time.gmtime(timestamp) #转换成Localtime
print mytime

#########################
# datetime  比time更好用
#########################
#    在datetime 模块,用得比较多的是 datetime.datetime 和 datetime.timedelta
#    使用datetime.datetime.now()可以获得当前时刻的

print datetime.datetime.now() #获取当前datetime
print datetime.date.today()  # 获取当天date

#转换：datetime <=> string
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # strftime

mydatetime =  datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S") 
print type(mydatetime)

#转换datetime <=> date
print datetime.datetime.now().date()

#转换datetime <=> timestamp
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())

print datetime.datetime.fromtimestamp(1421077403.0) #这个重要！


