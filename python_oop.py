#-*- coding:gb18030 -*-
'''
Created on 2016年3月30日
  很多来自廖雪峰的教程
@author: Administrator
'''
#如何查看类有哪些属性  两种方法：1. dir() 列表     2. __dict__属性  字典
from types import MethodType

# 同Java语言一样，Python使用了引用计数这一简单技术来追踪内存中的对象。
# 在Python内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。
#但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数


#__init__()类似构造器 但实际上不是构造器

class Animal:
    '类文档字符串'  #重要，类定义，之前不知道，可以用__doc__打印出来
    name = 'ss'  #类变量！重要！
    def __init__(self,name):
        self.name = name #对象变量！
        
    def show(self):
        print 'name is',self.name,Animal.name
        

animal = Animal('jack')  #和其他面向对象语言一样，如果你提供了有参构造，则系统不会提供默认构造 下面的调用就会出错
#animal = Animal() #会出错
animal.show()
print Animal.__dict__
dir(Animal)


class Dog(Animal):
    'Dog class'
    def __init__(self,name):
        self.name = name #对象变量！
        
    def show(self):
        print 'dog name is',self.name

dog = Dog('哈巴')
dog.show()


########################
# 特殊类属性  这些都不会继承
#######################
print '类属性**********************************'
print Dog.__name__
print Dog.__doc__
print Dog.__bases__  #父类组成的元组
print Dog.__dict__   #属性
print Dog.__module__  #所在模块
print dog.__class__ #示例对应的类
print type(Dog),type(dog)   #一个类、一个实例


#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数


#析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "销毁"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # 打印对象的id
del pt1
del pt2
del pt3


########################
#继承
########################
# 在python中继承中的一些特点：
# 1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。  重要 和其他语言不一样
# 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数  重要 
# 3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"

   def parentMethod(self):
      print '调用父类方法'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "父类属性 :", Parent.parentAttr
   def fun(self):
       print '父类方法'

class Child(Parent): # 定义子类
   def __init__(self):
      print "调用子类构造方法"

   def childMethod(self):
      print '调用子类方法 child method'
   def fun(self):
      #Parent.foo(self)  这种方法推荐
      print '子类方法'
   def __str__(self):
       return '我是孩子'
p = Parent()
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
c.fun()
Parent.fun(c)  #调用父类的中被覆盖的方法！ 但是一般不这样做。 而是在子类fun中先调用P.foo(self)
print c

##########################
#基础重载方法
##########################
# __init__ ( self [,args...] )
# 构造函数
# 简单的调用方法: obj = className(args)

# __del__( self )
# 析构方法, 删除一个对象
# 简单的调用方法 : dell obj

# __repr__( self )
# 转化为供解释器读取的形式
# 简单的调用方法 : repr(obj)

# __str__( self )  相当于tostring
# 用于将值转化为适于人阅读的形式
# 简单的调用方法 : str(obj)

# __cmp__ ( self, x )
# 对象比较
# 简单的调用方法 : cmp(obj, x)

# __iter__
##########################
#运算符重载   __str__  __add__  __iadd__(原位加法：即+=)  
##########################
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):  #重载 + 
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2



#############################
#类属性与方法  
# 1.重要  默认情况下属性都是公开的   最好弄get set
# 2.非常重要的一点  可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性（即类中没有，但是可以动态的给实例绑定）
#############################
# 私有属性：
# _private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 私有方法：
#private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount  # 报错，实例不能访问私有变量

#重要！
#Python不允许实例化的类（注意 实例化）访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的最后一行代码：
print counter._JustCounter__secretCount

#动态绑定属性
counter.newA = 3  # newA是动态绑定的 类没有 其他该类的对象都没！ 重要
print counter.newA  #也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同 

#############################
#多态  
#任何类，最终都可以追溯到根类object
##############################

#判断一个变量是否是某个类型可以用isinstance()判断：
print isinstance(c, Child)
print isinstance(c, Parent)
#看来c不仅仅是Dog，c还是Animal！

def run_twice(Parent):
    Parent.fun()
    Parent.fun()
    
# 这就是多态
run_twice(c)
run_twice(p)

################################
# 获取对象信息
#################################

#我们来判断对象类型，使用type()函数
#Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入
import types
print type('abc')==types.StringType

#isinstance()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度
# len()其实等价于l__len()__
    #如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法  重要 之前不知道！
#当然你也能重写__len__就和 __str__一样

#重要方法！ 之前不知道！  getattr  setattr    以及hasattr    
#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态。  属性和方法都算属性

print hasattr(c,'name')
print hasattr(c,'fun')
fun= getattr(c, 'fun') #获取方法 
fun() #再调用方法 重要
setattr(c,'newattr',54)  #添加新属性
print getattr(c,'newattr')  #获得新属性
print c.newattr #获得新属性
# 如果试图获取不存在的属性，会抛出AttributeError的错误
# print c.xx
#可以传入一个default参数，如果属性不存在，就返回默认值：
print getattr(c, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

###########################
#  动态绑定属性 、slots
##########################
#前面提到给一个对象动态绑定属性，但是其他同类的属性就获得不到，所以可以给类class绑定，这样大家都能获得:
def set_score(self, score):
    self.score = score
Child.set_score = MethodType(set_score, None, Child)
c.set_score(23)
print c.score

#如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s = Student()
s.name = 'Michael'
s.age = 25 # 绑定属性'age'
#s.score = 99 # 绑定属性'score'  这里出错

#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
#除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。


####################################
#   使用@property  
#   广泛应用
####################################
# 不要直接暴露属性  最好提供get set方法 就和java一样 切记！
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改。可以加以限制
class Student2(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int): #必须是int类型！
            raise ValueError('score must be an integer!')  #抛出异常！ 重要的方法！直接抛出去
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
#  所以 引入了@property
#  Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student3(object):
    #  把一个getter方法变成属性，只需要加上@property就可以了   
    @property
    def score(self):  #名字就叫score
        return self._score
    # 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter 
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student3()
s.score = 60 
print s.score 
#s.score = 9999  #把setter变成属性调用

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student4(object):

    @property  
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property  #age是只读的
    def age(self):
        return 2014 - self._birth
# @property  可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性

###########################################
# 定制类   
# 非常重要
# __iter__  __getitem__  __getattr__
###########################################

# 1. __iter__  这个暂时了解就行
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

for n in Fib():
    print n

# 2. __getitem__  
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Num():
    def __getitem__(self, n):
        self.xx = (1,34,5,5)
        return self.xx[n]
n = Num()
print n[2]

# 3. __getattr__
# 注意和前面全局方法getattr()的区别
# 如果你访问另一个不存在的属性 就会报错 如Student' object has no attribute 'score'，如何访问没有属性的时候不报错，更优雅一点呢
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：

class Student5(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):  #只要你访问英国不存在的attr，就处理 ， 这里可以用if判断
        if attr=='score':
            return 99
        
# 返回函数也是完全可以的：
class Student6(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        
# 实际上可以把一个类的所有属性和方法调用“全部动态化处理”了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。  

#举个例子：    重要！
# REST API
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：     
#         http://api.server/user/friends
#         http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 
# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list


# 3. __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？类似instance()？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student7(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student7('Michael')
s()

#####################################
# 类属性和实例属性
# 重要 python的实例属性必须在__init__(self) 方法中定义，直接跟在类名后边定义的属性都默认是类属性(类似于c++的static变量)。
#####################################
#在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
class Student8(object):
    #self.age = 4 不能在这里定义 错误！ 必须在__init__(self)中
    def __init__(self, name):
        self.name = name

s = Student8('Bob')
s.score = 90

class Student9(object):
    name = 'Student'  #类名后默认都是static
s = Student9()
print(s.name) # 重要！ 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性 
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会"屏蔽"掉类的name属性       
print(Student9.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


##############################################
# 使用元类
##############################################

# 1. type
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# 比方说我们要定义一个Hello的class，就写一个hello.py模块：
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
print(type(Hello)) #Hello是一个class，它的类型就是type
h = Hello()
print(type(h)) #h是一个实例，它的类型就是class Hello

#type还能动态创建类型  （解释直接写的class底层就是用的type）
# 无需通过class Hello(object)...的定义
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

#type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。    

#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


# 2. metaclass  基本用不到  类似java的Class吧
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# 先定义metaclass，就可以创建类，最后创建实例  元类让你来定义某些类时如何被创建的
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码
# 正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到
