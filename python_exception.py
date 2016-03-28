#-*- coding:gb18030 -*

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
try:
    f=open('blah', 'r')
except (ValueError, TypeError):  #这里e指异常信息  
    print 'could not open file:',e

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
with open('/etc/passwd','r') as f:
    for eachLine in f:
        #code...
        
        
#触发异常 即抛出异常 raise  格式比较多
# raise 异常名称 可选参数（用来传给异常） 
# 一般使用raise 类  就可以了， 不建议字符串异常

#断言
#assert 1 == 0

#当然你也能创建异常 继承自异常类
# class NetWorkError(IOError):
#     pass