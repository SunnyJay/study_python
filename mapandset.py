#-*- coding:utf-8 -*-  
'''
Created on 2016年3月17日

映像和集合类型
@author: Administrator
'''

#############################################
#字典是唯一映射类型 字典可以有任意类型的键
#工厂方法dict可以创建字典  
#############################################


#遍历一个字典，可以用.keys()方法。也可以用迭代器如
dict2 = {'name':'sunnanjun','port':80}
#方法一
for key in dict2.keys():
    print key
#方法二 这种更方便 key就是key
for key in dict2:
    print key, dict2[key]
#检查一个集合中是否有某个key的最好方法式in not in; 还可以用has+key
if 'name' in dict2:
    print 'has'
if dict2.has_key('name'):
    print 'has'    

#删除key  pop方法
dict2.pop('port')
print 'dict2',dict2


#更新字典
dict2['age'] = 66 #直接新增
print dict2
#清空字典
dict2.clear()

#字典也可以比较 算法比较复杂：
    #先是比较字典长度 然后是键 最后是值
#len() dict()返回一个创建的字典
#注意 字典中的元素是没有顺序的
dict2 = {'name':'sunnanjun','port':80}
print len(dict2)
print dict(x=1,y=2)

#返回对象的哈希值，也可以判断某个对象是否是可哈希的
print hash('sun')  

#字典内建方法 重要！
print dict2.keys()
print dict2.items() #这个重要
print dict2.values()
print dict2.get('name')
print dict2.setdefault('sex', 'man') #重要 判断是否存在 如果不存在则插入并返回
print dict2

#字典的键必须是可以哈希的
#大部分对象都可以，但是列表字典等可变类型，它们是不能哈希的，所以不能作为键
dict3={():33} #元祖是可以的
dict3={(5,):'df'}
print dict3[(5,)]

#一些可变对象也是可以的，前提是必须实现__hash__方法！类似java


#下标除了更新，还可以增加元素！之前疏忽了！重要！
xxx={}
xxx[1] ='d'
xxx[2] = 'e'
print xxx

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
if 1 in xxx:
    print 'ok!'
print xxx.get(1),xxx.get(4)  #二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：





#############################################
#集合
#python中的集合分为可变集合set、不可变集合frozenset
#集合本身是无序的，无法索引无法切片无法根据键查找
#############################################

#要创建一个set，需要提供一个序列（字符串、list）作为输入集合：
s = set([4, 2,'d', 3]) #list
print s

s = set((1, 2, 3)) #元祖
print s

s = set('jacksun') #元祖
print s

#集合唯一的创建方式：set()和frozenset()   重要
s = set('haha')  #只包含a\h 
print s
print type(s)
print len(s)
#支持in not in

#集合操作 
s.add('z')
s.remove('a') #不存在则会引发错误
s.discard('a') #如果是其原始，则删除；   不存在不会出问题
s.pop() #删除任意元素 重要
s -= set('h')
print s

#== != 集合等价指的是元素
#判断子集超集 > >= < <=
print set('sunnanjun') == frozenset('sunnanjun')
print set('sunnanjun') < set('nanjuncoke')

#集合类型操作符 重要
#联合| 交集& 差集- 对称差分即异或 ^
t=set('sunnanjun')
t=set('nanjuncoke')
print t
print s|t   
print s&t
print s-t
print s^t #不能同时属于

# |= &= -= ^=
# |= 相当于update
s=set('a')
s |= set('vb')
print s
s.update('ct') #并集
print s

#不可变集合
f = frozenset('reysfh')
#f.remove('h')

#set、frozenset的参数必须是可迭代的 如序列、字符串  或支持迭代的对象如文字或字典  重要！！
set()#经常用于初始空集合
print set('fsg')
print set((343,5656))
set([])

# 补充：
#当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
#相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
