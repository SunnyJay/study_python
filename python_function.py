#-*- coding:utf-8 -*- 
'''
Created on 2016年3月24日
函数和函数式编程 method
@author: Administrator
'''
#重要 python中void对应就是None 之前不知道  其实是：函数执行完毕也没有return语句时，自动return None。
def hello():
    print 'xx'
res = hello()

print res #结果是None

#实际上python函数返回也是一个对象 只不过看起来像

#python支持默认参数

#重要 参数组  千万别理解成指针
#func(*参数组, **关键字参数字典)

#python 函数位置没有影响！所以你可以不担心向前引用问题
def bar():
    print 'bar'
def foo():
    print 'foo'
    bar()
    
def foo2():
    print 'foo2'
    bar2()  #不会出问题
def bar2():
    print 'bar2'    
    
#函数是可以拥有属性的 你可以动态创建  名称空间在后面介绍
bar2.xx = 'sds'
bar2.version = 0.1
print bar2.xx 
print bar2.version


#内嵌函数  之前不知道 
def foo_out():
    def bar_in():  #这里定义，当然，外部不能调用她 
        print 'bar_in'
    print 'foo_out'
    bar_in() #这里调用    只能内部调用
foo_out()
#foo_out.bar_in()

##########################################################
# 函数与装饰器 重要！flask编程用到了！
#    格式：  @装饰器名(可选参数) 
# 装饰器实际上就是一个函数，用@声明,用来包装另一个函数，参数就是函数对象！

# 在Python中，装饰器实现是十分方便的
# 原因是：函数可以被扔来扔去。
# 函数作为一个对象

#装饰器是一个函数,一个用来包装函数的函数，装饰器在函数申明完成的时候被调用，调用之后返回一个修改之后的函数对象，将其重新赋值原来的标识符，并永久丧失对原始函数对象的访问(申明的函数被换成一个被装饰器装饰过后的函数)
#当我们对某个方法应用了装饰方法后， 其实就改变了被装饰函数名称所引用的函数代码块入口点，使其重新指向了由装饰方法所返回的函数入口点。
#由此我们可以用decorator改变某个原有函数的功能，添加各种操作，或者完全改变原有实现

#装饰器分为无参数decorator，有参数decorator
#装饰器有参/无参，函数有参/无参，组合共4种
###########################################################

#无参数装饰器 – 包装无参数函数
def decorator(func):
    print "hello"
    return func
@decorator  #这里只要声明时就执行装饰器 ，然后返回一个包装后的函数对象，对外的样子还是food，所以你以后使用时直接用的就是新的！
def food1():
    pass
food1()  #等价于 foo = decorator(foo) ; foo()

#无参数装饰器 – 包装带参数函数  重要：要对传入的函数的参数进行再处理，所以内部需要再定义一个处理函数
def decorator_func_args(func):
    def handle_args(*args, **kwargs): #处理传入函数的参数
        print "begin"
        func(*args, **kwargs)   #函数调用
        print "end"
    return handle_args

@decorator_func_args
def food2(a, b=2):
    print a, b

food2(1)  #等价于  foo2 = decorator_func_args(foo2);foo2(1)

#带参数装饰器 – 包装无参数函数
def decorator_with_params(arg_of_decorator):#这里是装饰器的参数
    print arg_of_decorator  #就是多了个参数而已，没什么难的
    #最终被返回的函数
    def newDecorator(func):
        print func
        return func
    return newDecorator
@decorator_with_params("deco_args")
def food3():
    pass
food3()     #先打印参数deco_args,然后就是被包装函数

#python 内置装饰器  staticmethod,classmethod, property

#1. staticmethod 类中定义的实例方法变成静态方法  相当于全局函数 类似于静态语言中的静态方法
     #基本上和一个全局函数差不多(不需要传入self，只有一般的参数)，只不过可以通过类或类的实例对象来调用，不会隐式地传入任何参数。
#2. property
    #对类属性的操作，类似于java中定义getter/setter
    
class A():
    @staticmethod
    def test_static():
        print "static"
    def test_normal(self):
        print "normal"
    @classmethod
    def test_class(cls):
        print "class", cls

a = A()
A.test_static()  #可以类名.调用
a.test_static()
a.test_normal()
a.test_class()


class B():
    def __init__(self):
        self.__prop = 1
    @property
    def prop(self):
        print "call get"
        return self.__prop
    @prop.setter
    def prop(self, value):
        print "call set"
        self.__prop = value
    @prop.deleter
    def prop(self):
        print "call del"
        del self.__prop
        
#装饰器的顺序很重要，需要注意
# @A
# @B
# @C
# def f ():
# 等价于 f = A(B(C(f)))



###########################################################
#  默认参数和可变参数
#  所有必要参数都要在默认参数之前
###########################################################
#默认参数
# 位置必须靠右！
# def taxme2(rate=0.23,cost) #错误
def taxme2(cost, rate=0.23):  #正确
    print 'cost',cost,'rate',rate
    pass
# 调用的时候，如果指定了参数名，可以不按照顺序进行
taxme2(3,4)
taxme2(3)
taxme2(cost=4)
#taxme2(rate=4)
taxme2(rate=4,cost=5) #可以不按照顺序

# 可变长参数 重要！之前不了解，包括两种：非关键字可变参数（元祖）、关键字可变参数（字典）。  **被重载过了，以便不与幂运算发送混淆
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。   当然后面两个都是可选的！

#１．非关键字可变参数  *
#星号之后的所有形参将作为元祖the Rest传递给函数，
def fun1(arg1,arg2='xx',*theRest):  
    print 'arg1:',arg1
    print 'arg2:',arg2
    for arg in theRest:
        print arg
fun1(3,5,6,545,455,34,'f')  # 6以后的都一起作为一个元祖theRest传给函数
list1=(3,3,545)
fun1(3,5,list1)  #放在外面
print '加*'
fun1(3,5,*list1) #最好加个* 表示这是可变参数！ 重要！


#2．关键字可变参数 这种更加灵活 **
#字典中的键为参数名，值为响应的参数值！
def fun2(arg1,arg2=4,**theRest):  #星号之后的所有形参将作为字典the Rest传递给函数，
    print 'arg1:',arg1
    print 'arg2:',arg2
    for arg in theRest:
        print arg,':',theRest[arg]
fun2(3,5,a=6,b=545,c=455,d={'a':'b','c':'d'})  # 可变参数还可以是一个元祖或者字典
#注意，a=6 b=545 这是最简单的写法，但是一般都是先包装好，然后加**传进来
dict1={'1':'A','2':'B','3':'C'}
fun2(3,6,**dict1)  #加**


kw = {'city': 'Beijing', 'job': 'Engineer'}
fun2(3,4,**kw)

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法



###########################################################
#  函数式编程
#  暂时不需要了解
###########################################################

###########################################################
#  变量作用域
#  global语句
#  闭包
#global语句用来声明x是全局变量，当我们在函数内给x赋值时，它的改变映射到我们在主块中使用的x的值。
###########################################################

#为了明确引用一个已命名的全局变量，必须使用global语句！ 可以不用创建一个局部变量  重要 之前不知道
# global a,b,c  

#下面的例子在核心编程中提到 重要！
#在函数定义中声明的变量，他们与在函数外使用的其它同名变量没有任何关系，即变量名称对函数来说是局部的。
#这叫变量的范围。所有变量都有它们被声明的块的范围，从名称定义的点开始。 
def fooo():
    bar = 200
    print 'in bar:',bar
bar = 33
print 'out bar:',bar
fooo()
print 'out bar:',bar  #、fooo中的bar和外面的bar没有关系

# global
print '*************************global************************'
def foooo():
    global bar 
    bar = 200  #声明它是global的 不是拘局部的
    print 'in bar:',bar
bar = 33
print 'out bar:',bar
foooo()
print 'out bar:',bar  

#闭包 之前没有听过
#一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量。
#第一种场景 ，在python中很重要也很常见的一个使用场景就是装饰器，Python为装饰器提供了一个很友好的“语法糖”——@，让我们可以很方便的使用装饰器
#闭包这东西理解起来还是很容易的，在Python中的应用也很广泛
def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()   #my_line就是一个line函数的对象 
print(my_line(5))  

#生成器  了解即可
#生成器是迭代器，同时也并不仅仅是迭代器，不过迭代器之外的用途实在是不多，所以我们可以大声地说：生成器提供了非常方便的自定义迭代器的途径。
#首先请确信，生成器就是一种迭代器。生成器拥有next方法并且行为与迭代器完全相同，这意味着生成器也可以用于Python的for循环中。
#另外，对于生成器的特殊语法支持使得编写一个生成器比自定义一个常规的迭代器要简单不少，所以生成器也是最常用到的特性之一。
def get0_1_2():
    yield 0
    yield 1
    yield 2
xx = get0_1_2()  #调用生成器函数将返回一个生成器；
print xx.next()
print xx.next()
print xx.next()


##########################
# 补充：with
##########################
# Python对with的处理还很聪明。基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
# 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
# 当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。

class Sample:
    def __enter__(self):
        print "In__enter__()"
        return "Foo"
    def __exit__(self, type,value, trace):
        print "In__exit__()"
 
def get_sample():
    return Sample()

with get_sample() as sample:
    print "sample:",sample