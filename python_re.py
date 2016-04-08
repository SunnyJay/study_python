#-*- coding:utf-8 -*- 
'''
Created on 2016年4月7日
主要来自廖雪峰教程
@author: Administrator
'''
import re

# 注意： python本身支持用\转义，但是不推荐用，强烈推荐用r前缀
s = 'ABC\\-001' # Python的字符串
s = r'ABC\-001' # Python的字符串  推荐

# match方法 成功返回Match对象，失败返回None
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print 'ok'
else:
    print 'failed'
    
###################################    
# 切分字符串
###################################
print 'a b   c'.split(' ')

#可以分割任意空格
print re.split(r'\s+', 'a b   c')  #正则 \s+表示1到无数个空白符  重要！！！

#可以分割空格和逗号
print re.split(r'[\s\,]+', 'a,b, c  d')
#还有分号
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

###################################    
# 分组  可以用来提取子串！很常用
###################################
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

# 重要 注意到group(0)永远是原始字符串
print m.group(0)
print m.group(1)
print m.groups()  #元祖

###################################    
# 贪婪匹配  加一个？就不贪了
###################################

print re.match(r'^(\d+)(0*)$', '102300').groups()  #太贪了 \d+全部匹配完了
print re.match(r'^(\d+?)(0*)$', '102300').groups()  #加?采用非贪婪 先满足后面的0*


###################################    
# 编译  处于效率考虑
###################################

# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$') #以后直接拿来用
print re_telephone.match('010-12345').groups() #各种用
print re_telephone.match('010-8086').groups()