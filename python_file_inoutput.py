#-*- coding:gb18030 -*
'''
Created on 2016��3��18��
�ļ����������
open('d:\\xx.txt','r+')  #��Ҫ���� window��·��Ҳ��Ҫת��
@author: Administrator
'''

#�ļ��ڽ����� open file
#open����һ���ļ����󣬷����������󡣲���ʧ�ܻ����IOError�쳣
#r\w\a\U
#r\U�����ȴ��� w�����
#buffering 0��ʾ������ n��ʾ������ٺ�
#python��open����������linux fopen
#linux�� b���п��� +��ʾ�ɶ���д
#file_object = open(file_name, access_mode='r', buffering=-1) 
#fp=open('data','r+')

#��������file  ��Ҫ file��open���������滻 ������open

#ͨ�û��з�֧��
# linux windows֮��Ҫ����\r\n \n������ python���Լ����� �����UNS֧��

#�ļ��ڽ�����
# read ��ȡ������Ŀ���ֽ�  -1��ʾ�����ļ�β  read*����ɾ�����з� ������Ҫ�ֶ�ɾ��
# readline ��ȡһ�а����н����� һ�𷵻�  -1��ʾ�����ļ�β
# readlines  ��ȡ����ʣ���в���Ϊ�ַ����б���
# write ע��û��writeline  ��Ҫ wirte*����д�뻻�з� ������Ҫ�ֶ�д��
# writelines �� readlinesһ�� ����б����

#�ļ��ƶ�
# seek() 
# tell()���ص�ǰ�ļ���λ��
# �ļ����� ��Ҫ һ��һ�з����ļ� �ɴ���read*����
# for eachLine in fp: #����д�� for eachLine in fp.readline()
#     pass
#close�ر��ļ�  python��������ü����Զ��ر�Ŷ ��������ϰ�߻�����ʾ�ر�һ��
#flush���д�뻺�������ݵ��ļ�

#��������������ļ��ܴ�ʱ�򲻺� ��ɿ������õ�����
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

# a   ׷��ģʽ��ֻ��д���ļ�ĩβ
# a+  �ɶ�дģʽ��дֻ��д���ļ�ĩβ
# w+ �ɶ�д����a+��������Ҫ����ļ�����
# r+ �ɶ�д����a+�������ǿ���д���ļ��κ�λ��

#ע��������⣺
# ��ԭ�����ڶ�д��������б���Ҫ��fflush, fseek, fsetpos, rewind���������
# ��Ȼpython�Ͳ�֪����ǰ�ļ�λ������������İ취�����ڹر��ļ�ǰֻ��������дһ�ֲ���

f = open('d:\\xx.txt','r+')  #��Ҫ���� window��·��Ҳ��Ҫת��
line = f.readline()
print line
# print f.tell()
#f.write('testline1\n') 
#f.write('testline2\n') #�ֶ�д�뻻�� ��Ȼ��ת��

# for eachline in f:
#     print eachline
#f.write('testline2\n') #����һ�о�ʧ�� �����   
f.write('testline1\n')   

f.close()


#��׼�ļ�






