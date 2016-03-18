#-*- coding:gb18030 -*
'''
Created on 2016年3月18日
文件和输入输出
open('d:\\xx.txt','r+')  #重要！！ window下路径也需要转义
@author: Administrator
'''

#文件内建函数 open file
#open返回一个文件对象，否则引发错误。操作失败会擦汗IOError异常
#r\w\a\U
#r\U必须先存在 w会清空
#buffering 0表示不缓冲 n表示缓冲多少航
#python的open函数来自于linux fopen
#linux下 b可有可无 +表示可读可写
#file_object = open(file_name, access_mode='r', buffering=-1) 
#fp=open('data','r+')

#工厂函数file  重要 file和open可以任意替换 建议用open

#通用换行符支持
# linux windows之间要区分\r\n \n的区别， python会自己处理 这就是UNS支持

#文件内建方法
# read 读取给定数目的字节  -1表示读到文件尾  read*不会删除换行符 所以你要手动删除
# readline 读取一行包括行结束符 一起返回  -1表示读到文件尾
# readlines  读取所有剩余行并作为字符串列表返回
# write 注意没有writeline  重要 wirte*不会写入换行符 所以你要手动写入
# writelines 和 readlines一样 针对列表操作

#文件移动
# seek() 
# tell()返回当前文件的位置
# 文件迭代 重要 一行一行访问文件 可代替read*方法
# for eachLine in fp: #不用写成 for eachLine in fp.readline()
#     pass
#close关闭文件  python会根据引用计数自动关闭哦 但是养成习惯还是显示关闭一下
#flush理解写入缓冲区数据到文件

#下面这个程序在文件很大时候不好 最可靠还是用迭代器
# filename =raw_input('enter file name: ')
# f = open(filename,'r')
# allLines = f.readlines()
# f.close()
# for eachLine in allLines:
#     print eachLine
#     
# f = open(filename,'r')
# for eachLine in f:
#     print eachLine
# f.close()



# 'r'    open for reading (default)
# 'w'    open for writing, truncating the file first
# 'a'    open for writing, appending to the end of the file if it exists
# 'b'    binary mode
# 't'    text mode (default)
# '+'    open a disk file for updating (reading and writing)
# 'U'    universal newline mode (for backwards compatibility; should not be used in new code)

# a   追加模式，只能写在文件末尾
# a+  可读写模式，写只能写在文件末尾
# w+ 可读写，与a+的区别是要清空文件内容
# r+ 可读写，与a+的区别是可以写到文件任何位置

#注意这个问题：
# 其原因在于读写交替过程中必须要有fflush, fseek, fsetpos, rewind这类操作，
# 不然python就不知道当前文件位置在哪啦。最笨的办法就是在关闭文件前只做读或者写一种操作

f = open('d:\\xx.txt','r+')  #重要！！ window下路径也需要转义
line = f.readline()
print line
# print f.tell()
#f.write('testline1\n') 
#f.write('testline2\n') #手动写入换行 当然先转义

# for eachline in f:
#     print eachline
#f.write('testline2\n') #加这一行就失败 很奇怪   
f.write('testline1\n')   

f.close()


#标准文件






