#-*- coding:utf-8 -*-
'''
Created on 2016年4月7日
序列化  pickling
主要来自廖雪峰
@author: Administrator
'''

#定义 我们把变量从内存中变成可存储或传输的过程称之为序列化
# 在Python中叫pickling    当然有unpickling

#Python提供两个模块来实现序列化：cPickle和pickle  重要
# 这两个模块功能是一样的，区别在于：
#      cPickle是C语言写的，速度快，
#      pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
#      用的时候，先尝试导入cPickle，如果失败，再导入pickle

try:
    import cPickle as pickle #起别名
except ImportError:
    import pickle
    
#pickle.dumps()方法把任意对象序列化成一个str
#pickle.loads()方法反序列化出对象

d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#再读进来
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()


###################################
# JSON 重要！
##################################

# JSON的特定 之前不清楚 重要！！！     标准、更快、易读取
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
# 比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

#JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# JSON类型    Python类型
# {}    dict
# []    list
# "string"    'str'或u'unicode'
# 1234.56    int或float
# true/false    True/False
# null    None

#Python内置的json模块  提供了非常完善的Python对象到JSON格式的转换

import json
d = dict(name='Bob', age=20, score=88)  #重要 Python的dict对象可以直接序列化为JSON的{}
print json.dumps(d)

#用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)  #loads从字符串反序列化                   有 u, 默认都是unicode而不是str


###########################
# 序列化自定义类  这个才是常用的
###########################
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#print(json.dumps(s))  #这里会报错！ not JSON serializable

# 这是因为默认情况下dumps不知道如何序列化    
# dumps方法有一系列的参数:
# 1:default
#    可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：

#先提供一个转换函数  先转换成 dict,然后再转换为JSON
def student2dict(std):
    return {  'name': std.name,'age': std.age,'score': std.score}  #dict
print(json.dumps(s, default=student2dict)) #指定转换函数

# 2:object_hook
#    loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
student = json.loads(json_str, object_hook=dict2student)  #loads先转为dict, dict2student再转为Student
print student.name



    