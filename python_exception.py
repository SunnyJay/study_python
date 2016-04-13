#-*- coding:utf-8 -*- 

'''
Created on 2016年3月24日
错误和异常
BaseException 是所有异常的基类   Exception是常规错误的基类
@author: Administrator
'''

#常见异常
#NameError name 'foo' is not defined
#AttributeError 尝试访问未知的对象属性

#try语句两种：tryexcept  tryfinally 
try:
    f=open('blah', 'r')
except Exception,e:  #这里e指异常参数  
    print 'could not open file:',e

#', e'可以不要
try:
    f=open('blah', 'r')
except Exception:  #这里e指异常信息  ', e'可以不要
    print 'could not open file'   

#带有多个except语句，也可以在一个except中处理多个异常
# try:
#     f=open('blah', 'r')
# except (ValueError, TypeError):  #这里e指异常信息  
#     print 'could not open file:',e

#重要，如果你要捕获所有异常，使用BaseException

#Exception,e:
#e是Exception类的一个实例
#使用str(e)能返回一个良好刻可读的异常
try:
    f=open('blah', 'r')
except Exception,e:  #这里e指异常参数  
    ret = str(e)
    
#重要！ else也可以配合try  如果try中的代码没有发生异常，则执行else!
try:
    f=open('blah', 'r')
except Exception,e:  #这里e指异常参数  
    ret = str(e)
else:
    print '没有发生！'
# 几种写法    

# try
# except
# else
# finally

# try
# finally

#上下文管理  重要
# with用于简化资源的释放 无论这段代码开始还是中间或者结束发生异常，with都会执行清理代码，仍然会自动关闭！  
# with open('/etc/passwd','r') as f:
#     for eachLine in f:
#         #code...
        
        
#触发异常 即抛出异常 raise  格式比较多
# raise 异常名称 可选参数（用来传给异常） 
# 一般使用raise 类  就可以了， 不建议字符串异常

#断言
#assert 1 == 0
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

#当然你也能创建异常 继承自异常类
# class NetWorkError(IOError):
#     pass


# loging  重要！之前不知道
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(level=logging.INFO)  #重要
s = '0'
n = int(s)
logging.info('n = %d' % n)
#print(10 / n)
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。


