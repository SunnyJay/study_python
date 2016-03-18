#-*- coding:gb18030 -*
'''
Created on 2016年3月18日

条件和循环
@author: Administrator
'''

#三元操作符  X if C else Y
x, y =4, 3#这种写法我竟然不知道 #这是所谓的多元赋值
smaller = x if x < y else y
print smaller

#多元赋值  其实两边是元祖
x,y,z=1,2,'a'
print x,y,z 

#交换两个值
x,y=y,x
print x,y

#多重赋值
x=y=z=1

#for循环
for i in 'sunnanjun':
    print i
    
#for迭代三种方法：序列项迭代、索引迭代、enumerate迭代
for i in range(len('sunnanjun')):
    print 'sunnanjun'[i]

for i in enumerate('sunnanjun'):  #每个i是一个元祖
    print i

#range方法  重要  它会返回一个列表
# range(begin,end,step=1)
# range(2,19,3)
# range(3,5) 表示3 4 5
# range(5) 表示0-4  这是最简单的语法
print range(3,19,3)
print range(6)

#xrange  性能远高于range

#sorted reversed enumerate zip
#zip？

#pass语句
#pass语句不做任何事 NOP(no operation)
#重要 pass可以作为开发技巧 即可以用来先占位 以后再完成编写
def fun():
    pass

#重要 while和else
#除了ifelse中， while也可和else配合使用
#else会在while结束后执行，包括break!
count = 0
while count>4:
    if count >3:
        break;
    count +=1
    
else:
    print count, '循环结束'                                                                                                                                                                                                                                                                

#迭代器和iter()函数
#对一个对象调用iter()方法就能得到迭代器
myTuple=(123,'zxs',3453.6)
i=iter(myTuple)
print i.next()
#重要 序列会自动的产生迭代器，for i in seq:  实际上市使用迭代器的。

#字典和文件也是可以迭代的
#可变迭代器 不可变迭代器

#列表解析   list comps  用于动态创建列表
#这个暂时不研究


#生成器表达式
#这个暂时不研究
