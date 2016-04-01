#-*- coding:gb18030 -*
'''
Created on 2016年4月1日
核心编程 第十四章 执行环境
@author: Administrator
'''
##############################
#一、可调用对象
##############################
# python有四种可调用对象 函数、方法、类、以及实例
# 重要概念: 之前不知道
#       Python中Function(函数）和methon(方法）是不同的！       方法和对象相关；函数和对象无关。
# 1. 函数
#    三种：  
#　　　　　　内建函数（built-in-function）　都是用c/c++编写的， 他们都在__builtins__模块里，然后导入
#　　                 用户自定义函数 user-defined   
#          lambda表达式
# 2. 方法
#
# 3. 类 都是可调用的
#
# 4. 实例:   
#    要调用就得重写__call__() 默认没有实现
#    实例默认都是不能调用的！重要，即不能用()调用 如 c= Cat()    c() 这样是错误的
class Cat():
    def __call__(self,*args): #会将对实例调用的参数全部传到call
        print '参数：',args
c=Cat()
c(2,43,54) #调用__call__()

##############################
#一、代码对象  
# 可作为函数或者方法调用
##############################





############################
# os模块
# 与平台无关 
# 重要！！ 必须全部记得
############################
# 即它允许一个程序在编写后不需要任何改动，也不会发生任何问题，就可以在Linux和Windows下运行。
# 一个例子就是使用os.sep可以取代操作系统特定的路径分割符

# os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
# os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
# os.listdir()返回指定目录下的所有文件和目录名。
# os.remove()函数用来删除一个文件。
# os.system()函数用来运行shell命令。  返回命令运行的返回码
# os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
# os.path.split()函数返回一个路径的目录名和文件名。
#         >>> os.path.split('/home/swaroop/byte/code/poem.txt')
#         ('/home/swaroop/byte/code', 'poem.txt')
# os.path 系列
import os
print os.name
print os.getcwd()
print os.listdir(os.getcwd())
#os.system('cmd') # 重要！！ 之前不知道！ 非常有用
#os.system('dir')
print os.linesep    #os.linesep字符串给出当前平台使用的行终止符  
print os.sep#os.sep 可以取代操作系统特定的路径分割符。
print os.path.split('c:\\xx.tex')
# os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
print os.path.isdir(os.getcwd())
print os.path.exists(os.getcwd()) #函数用来检验给出的路径是否真地存在 重要
print os.path.abspath(os.getcwd()) #获得绝对路径
print os.path.splitext('xx.ted') #:分离文件名与扩展名

#重要
print os.path.join(os.getcwd(),'xx.txt')  #:连接目录与文件名或目录

print os.path.basename('a.txt') #获得文件名
print os.path.dirname('c:\\Python\\a.txt') #获得路径名


############################
# sys模块
# sys就是你python的环境 注意与os区别
############################