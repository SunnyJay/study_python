#-*- coding:utf-8 -*- 
'''
Created on 2016年4月12日
编码
主要来自廖雪峰
@author: Administrator
'''


###############
# ascii、unicode、utf-8
# 
#   记住 ascii是utf-8的一部分
#   utf-8 汉字是3个字节 因为是一个字节
###############

# Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了
# Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）
# 
# 1、现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

# 2、如果把ASCII编码的A用Unicode编码，只需要在前面“补0”就可以，因此，A的Unicode编码是00000000 01000001。

# 3、用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
# 4、本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码：
#       重要： UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，“汉字通常是3个字节”，只有很生僻的字符才会被编码成4-6个字节。
#            如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
#            UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分,大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作
# 目前，在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。



#####################################
# python 和 unicode
# 
# python 源文件默认编码是根据环境有关，如在本eclipse下是GBK 所以必须开头声明！
# python 源文件头部更改编码成Utf-8时，如果保存出现乱码，此时回撤，然后再保存，就正常保存了！
#####################################
# 1、因为Python的诞生比Unicode标准发布的时间还要早
# 2、最早的Python只支持ASCII编码，普通的字符串'ABC'在Python内部都是ASCII编码的
# 3、Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换
print ord('f')
print chr(65)

# 4、Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示
print u'中'
# 写u'中'和u'\u4e2d'是一样的，\u后面是十六进制的Unicode码
print u'\u4e2d'

# 字符串'xxx'虽然是ASCII编码，但也可以看成是UTF-8编码，而u'xxx'则只能是Unicode编码    
print u'ABC'.encode('utf-8')  # unicode转utf-8  
print u'中文'.encode('utf-8')  # 

#英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同），而中文字符转换后1个Unicode字符将变为3个UTF-8字符
print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

#反过来，把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法：
abc = 'abc'.decode('utf-8') #返回u'abc'
print type(abc)

##!/usr/bin/env python   #第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释； 重要！！之前我不知道！
## -*- coding: utf-8 -*-


# 如果你使用Notepad++进行编辑，除了要加上# -*- coding: utf-8 -*-外，中文字符串必须是Unicode字符串。    好像不需要啊
print '中文'
#name = raw_input("请输入你的姓名:")
#print name
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保Notepad++正在使用UTF-8 without BOM编码：


# 5、Python当然也支持其他编码方式，比如把Unicode编码成GB2312。
print u'中文'.encode('gb2312')
#重要！    但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记“仅”使用Unicode和UTF-8这两种编码方式。

# 在Python 3.x版本中，把'xxx'和u'xxx'统一成Unicode编码，即写不写前缀u都是一样的，而以字节形式表示的字符串则必须加上b前缀：b'xxx'。






########################################
# 格式化
########################################

# 常见的占位符有：
# %d    整数
# %f    浮点数
# %s    字符串
# %x    十六进制整数


