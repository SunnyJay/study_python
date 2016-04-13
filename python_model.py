#-*- coding:utf-8 -*- 
'''
Created on 2016年3月28日
模块
@author: Administrator
'''
import sys

# 模块就是一个含有python语句的文件
# 模块名就是文件名（不要扩展名.py）  重要！模块导入的时候就被执行了！
# 法宝：help()函数看看：
# help('redis')
dir(sys)    #如果不到网页上看，用这种方法可以查看这个标准库提供的各种方法（函数）
print sys.platform
print sys.version
#使用如下语句就可以查找到想要模块的源代码位置：
import copy
#print copy.__file__
#print sys.__doc__
print copy.__all__ #公有接口

# 默认搜索路径更改：
# 修改PYTHONPATH变量
# 通过sys模块的sys.path变量，这是一个列表，你可以通过append方法加入路径, 重要！
print sys.path
sys.path.append('/home')
print sys.path
#使用sys.modules可以找到当前导入的模块来自什么地方，是个字典
print sys.modules

# import的工作流程
# 1. 搜索。就是python要能够找到import的模块
# 2. 编译。
    # 找到模块文件之后，将其编译成字节码，就是那个.pyc文件里面的（关于字节码，下面会介绍，请继续阅读）。
    # 注意，不是什么时候都编译的，只有第一次运行时候才编译，如果mmmm.py文件改变了，相当于又一个新文件，也会从新编译。
    # 其实就是.pyc文件中有一个时间戳，python会自动检查这个时间戳，如果它比同名的.py文件时间戳旧，就会从新编译。否则跳过。
    # 当然，如果根本就没有找到同名的.py源文件，只有字节码文件.pyc，那么就只能运行这个了。
# 3. 运行。执行就是前面已经编译的模块字节码文件，顺理成章要执行了。

# 搜索模块
# 一般情况下，python会自动的完成模块搜索过程。但是，在某些情况下，或许会要求程序员来设定搜索路径。当import一个模块后，python会按照下面的顺序来找那个将要导入的模块文件
# 
# 程序的主目录。上一讲中，在codes这个目录中运行交互模式，这时候的主目录就是codes，当在那个交互模式中运行import mmmm的时候，就首先在codes这个目录中搜索相应的文件（找到.py之后编译成为.pyc）。当然，后面在网页编程中，看官会看到，所谓主目录是可以通过顶层文件设置的目录。
# PYTHONPATH目录。这是一个环境变量设置，如果没有设置则滤去。如何进行环境变量设置，请看官google啦。
# 标准库目录。已经随着Python的安装进入到计算机中的那个。
# 任何.pth文件的内容。如果有这类文件，最后要在这类文件中搜索一下。这是一个简单的方法，在.pth文件中，加入有效目录，使之成为搜索路径。下图就是我的计算机上，存放.pth文件的位置以及里面放着的.pth文件







#################################################################
#知识点很重要，可以看有道笔记
#名称空间 
#命名空间是名字和对象的映射。也就是可以把一个namespace理解为一个字典，实际上很多当前的Python实现namespace就是用的字典。
#各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
#那么哪些可以是一个namespace呢，比如Python的built-in names（包括内置函数，内置常量，内置类型）；一个模块的global names（这个模块定义的函数，类，变量）；
#一个函数的所有local names；还有一个类对象的所有属性（数据成员，成员函数）都组成一个命名空间。 重要理解
#命名空间都是有创建时间和生存期的。对于Python built-in names组成的命名空间，它在Python解释器启动的时候被创建，在解释器退出的时候才被删除；
#对于一个Python模块的global namespace，它在这个module被import的时候创建，在解释器退出的时候退出；
#对于一个函数的local namespace，它在函数每次被调用的时候创建，函数返回的时候被删除。
#［总结］一个模块的引入，函数的调用，类的定义都会引入命名空间，函数中的再定义函数，类中的成员函数定义会在局部namespace中再次引入局部namespace。
#程序在查询上述三种命名空间的时候，就按照从里到外的顺序，即：Local Namespaces --> Global Namesspaces --> Built-in Namesspaces

#作用域
#作用域是指 Python 程序可以直接访问到的命名空间。“直接访问”在这里意味着访问命名空间中的命名时无需加入附加的修饰符。
#程序也是按照搜索命名空间的顺序，搜索相应空间的能够访问到的作用域。
#################################################################

def foo(num,str):
    name = "qiwsir"
    print locals() #访问本地命名空间的方法
foo(221,"qiwsir.github.io")


b = 33
c= 34
def fun():
    c = 22
    print b #全局的
    print c #自己的
fun()

#导入模块
# 推荐导入顺序： python标准库、python第三方、应用程序自定义、空行分隔
# 解释器执行到这条语句时，就会去搜索路径找到并加载。该过程遵循作用域原则：若模块在顶层导入则模块作用域为全局，若为函数中导入，则为局部
# 导入模块指定属性 注意是属性
# 推荐使用这种风格：  from xx import (a,b,c,d,e)  #圆括号

# as 为模块起别名
import redis as rs
from redis import sentinel as s

#模块的导入特性
#加载模块会直接执行模块
#无论你导入多吃少次，一个模块只被加载（执行）一次。这样就避免了重复导入重复执行。
from redis import * #全部导入 不推荐使用
#尽量不要只导入模块名，最好导入到属性级别,避免冲突

#从ZIP文件中导入模块
# python提供了直接从zip中导入模块的功能！

#模块内建函数 重要！
# 1. 模块导入函数  __import__()
__import__('sys')
# 2. globals()和locals()分别返回调用者全局和局部名称空间的字典
def funxx():
    a = 3
    b = 5
    print globals().keys() #返回全局
    print locals().keys()  #返回局部空间字典  在全局名称空间下，locals和globals返回一样
    
# 3. reload()函数   可以重新导入一个已经导入的模块（只能全部导入，而且不能用字符）
reload(rs)

# 包
# 为了组织好模块，会将多个模块分为包。Python 处理包也是相当方便的。简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件。
# 最简单的情况下，只需要一个空的 __init__.py 文件即可。当然它也可以执行包的初始化代码，或者定义稍后介绍的 __all__ 变量。
# 当然包底下也能包含包，这和文件夹一样，还是比较好理解的。
# 用户可以每次只导入包里的特定模块，例如： import sound.efforts.echo   这样就导入了 sound.effects.echo 子模块。它必须通过完整的名称来引用：
# 　　　　 sound.effects.echo.echofilter(input, output, delay=0.7, atten=4) 

#sys.modules是一个字典，里包含了大量载入的模块
#print sys.modules.keys()

#阻止属性导入
#不想导入哪个属性就在属性前加_ 如 import foo._bar

######################################
#重要：源代码编码
#只要在源代码开头写上编码指示    -*-
#    -*- coding:UTF-8 -*-   #-*- coding:gb18030 -*
######################################

#模块执行：有很多方法可以执行一个模块，如shell、execfile、模块导入

