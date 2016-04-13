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

###################################    
# 主要方法
###################################
# #返回pattern对象
# re.compile(string[,flag])  
# #以下为匹配所用函数
# re.match(pattern, string[, flags])
# re.search(pattern, string[, flags])
# re.split(pattern, string[, maxsplit])
# re.findall(pattern, string[, flags])
# re.finditer(pattern, string[, flags])
# re.sub(pattern, repl, string[, count])
# re.subn(pattern, repl, string[, count])  

# 另外大家可能注意到了另一个参数 flags，在这里解释一下这个参数的含义：
# 
# 参数 flag 是匹配模式，取值可以使用按位或运算符’|’表示同时生效，比如 re.I | re.M。
# 
# 可选值有：
# 
#  • re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
#  • re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
#  • re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
#  • re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
#  • re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
#  • re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

m = re.findall(r'\d+','3df43',re.I)
print 'test', m



# 属性：
# 1.string: 匹配时使用的文本。
# 2.re: 匹配时使用的Pattern对象。
# 3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
# 4.endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
# 5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
# 6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
# 方法：
# 1.group([group1, …]):
# 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
# 2.groups([default]):
# 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
# 3.groupdict([default]):
# 返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
# 4.start([group]):
# 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
# 5.end([group]):
# 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
# 6.span([group]):
# 返回(start(group), end(group))。
# 7.expand(template):
# 将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。


m = re.match(r'(\w+) (\w+)*', 'hello world!')
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')


#re.search(pattern, string[, flags])
# search 方法与 match 方法极其类似，区别在于 match() 函数只检测 re 是不是在 string的开始位置匹配，search() 会扫描整个 string 查找匹配，
# match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match() 就返回 None。
# 同样，search 方法的返回对象同样 match() 返回对象的方法和属性。我们用一个例子感受一下

#re.findall(pattern, string[, flags])
#搜索 string，以列表形式返回全部能匹配的子串。我们通过这个例子来感受一下
import re

pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')

#re.finditer(pattern, string[, flags])
#搜索 string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。我们通过下面的例子来感受一下
import re

pattern = re.compile(r'\d+')
for m in re.finditer(pattern,'one1two2three3four4'):
    print m.group(),
