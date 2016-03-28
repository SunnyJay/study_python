#-*- coding:gb18030 -*
'''
Created on 2016年3月16日
序列：成员是有序排列的 包括元祖、字符串、列表
@author: Administrator
'''
########################################################################
#字符串
########################################################################
from __builtin__ import enumerate

#标准类型操作符
#成员关系操作符 in、not in   if (obj in seq)
#切片操作符  ：通过下标访问序列元素的方法通常切片操作，如
        # seq[a,b] 获得下标a到b的元素集合  重要 之前不知道   seq[0:3]等同于seq[:3]
        # 越界访问索引会出现tuple index out of range
        # 正索引、负索引
        # 重要概念：切片操作符包括开始，包括结尾的前一个！
name='sunnanjun'
print name[0:-1] #输出sunnanju
print name[::]
print name[0:9]
print name[0:8]
if name[4] in name:
    print 'find'
if 's' in name:
    print 'find'    

#len获得序列的长度

#list()和tuple()函数在列表和元祖类型互换时非常有用

#字符串  python的字符串也是不可变的
#字符串可以直接比较 安装ascii值比较
#seq1+seq2  连接两个序列 重要 之前不知道 但不能直接连接数字 重要
sex='man'
print sex+name
print 'age'+str(34)  #print 'age'+29 #是错误的
#格式化操作符 %d %% %g  %f %e %s %x
print name, '的年龄是%d' % 24
print '%.2f' % 334.3435

#字符串模板

#原始字符操作符 即你不想转义！直接. 省去了多写一个斜杠的麻烦
print r'\n'
#路径中经常用到  f = open (r'c:\windows\t')

#unicode字符操作符
name = u'abc孙'
print name

#内建函数 cmp()    len()  max()返回字符串中最大的字符    min()返回字符串中最小的字符
#chr()  unichr()转换成Unicode的char
print chr(66),unichr(45)

#raw_input 这个要多用！
#user_input = raw_input("enter your name")
#print user_input

#所谓工厂函数，就是可以产生对应类型的对象 如str   unicode
print isinstance(u'\0xAB', str)  #str是一种类型
print isinstance(u'\0xAB', unicode)
print isinstance(u'\0xAB', basestring)
#unicode和str实际上都是抽象类basestring的子类 重要！ 注意类型叫法
 
#三引号允许一个字符跨越多行 可以包含换行符、制表符等其他特殊字符
#三引号自始至终保持所谓的所见即所得格式 如包含html
hi = '''
dfsdf
'''
print hi #看， 可以作为值 
hi = '''
<html> <head></head> <body> </body></heaml>
'''
print hi #所见即所得

#python处理unicode时要注意：
    #不要使用过时的string模块
    #使用unicode()而不是str()
    #出现字符串一定加u
    #必要的时候才使用encode 和 decode方法编解码（如网络、数据库）

#unicode()函数是和str同理的工厂方法

name = unicode('sunnanjun')
print name

#关键点总结
    #重要！字符应该视为长度为1的字符串 
    #字符或'' 或“”或'''  '''
    #python字符串不是通过'\0结尾的'  你不用关心 字符串只包含你想要的 别担心


########################################################################
#列表   与元祖类型，只不过元祖是不可变的或说只读的        序列（列表、元祖）
#所谓内建方法就是成员方法 built in
########################################################################

#重要！  列表可以包含不同类型的对象 比c要灵活的多
alist = [123,3545,6576,'4545',6456,['a','b',1],(343,(4,3),4546)]
emptylist = []
print alist
print emptylist #只显示一个[]

#append追加
alist.append('sfsf')  #类似+=
print alist

#重要的话 一般来说，程序员不需要去删除一个列表对象 列表对象出了作用域，会自动被析构

#操作符  可以比较 是逐项比较
list1=['abc','123']
list2=['abc','234']
print list1<list2
#当然能切片
print alist[5][2] #因为列表可保护列表

#成员操作符
if(6576 in alist):
    print 'in!'
blist = alist+list1
alist += list2 # 当然也可以这样  类似append
print blist
print alist

#重复操作符！ 之前不知道 *
print list1*2  #重复两遍
list1 *= 3
print list1

#和字符串一样 使用enumerate返回枚举集合 可以查看类型
t = enumerate(alist)
print type(t)
for i in t:
    print i
#sorted
numlist=[34,5,4,6,7,6,8,34,3,634,25]
newlist = sorted(numlist) #注意不会改变原来的 这是工厂函数
print newlist,sum(newlist)
print type(reversed(newlist)) #返回逆向迭代器
for i in reversed(newlist):
    print i
    
#list()和tuple()可以接受一个可迭代对象 然后浅拷贝创造一个新的列表或元组
print tuple(list1) #返回一个新的元组 

#重要，列表没有专门的操作符和成员（内建）函数， 都是来自于序列！
#序列成员方法：remvoe  pop  insert reverse extend sort  注意与工厂方法不同 成员方法(build_in)会改变自身
list1.reverse()
print list1


########################################################################
#元组 tuple 记住英文   不可变！
#元组也能包含各种类型!包括列表
#重要！之前不知道，如果只有一个元素，需要在元素后面加一个逗号，否则会解释成一个普通的括号！
########################################################################
tuple1 = (123,3545,True,'4545',6456,['a','b',1],(343,(4,3),4546))
print tuple1

tuple2 = () #空元组
print tuple2

tuple3 = (3)
print tuple3 #tuple就是3而已
tuple3 = (3,)
print tuple3 #这才是真正的分组

#某种意义上算是改变了元组 但是实际不是的 你懂的
tuple3 = tuple3 + (34,54)
print tuple3

#默认元组 重要！ 我之前不知道
#如果有多个对象的、逗号分隔的、没有明确符号定义的，默认就是元组
#如 
def fun():
    return 1,2,3  # 也就是 return (1,2,3) 所有函数返回的多对象都是元祖
def fun2():
    return (1,23,4)
def fun3():
    return [24,35] #当然你可以返回一个列表
x,y=1,2

#单元素元组切记加逗号

#何时使用元组和列表： 如当你需要维护敏感数据时

print type(__name__)
if __name__ == '__main__':
    print 'duli'
    
    
    