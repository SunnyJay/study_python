#-*- coding:gb18030 -*
'''
Created on 2016��4��1��
���ı�� ��ʮ���� ִ�л���
@author: Administrator
'''
##############################
#һ���ɵ��ö���
##############################
# python�����ֿɵ��ö��� �������������ࡢ�Լ�ʵ��
# ��Ҫ����: ֮ǰ��֪��
#       Python��Function(��������methon(�������ǲ�ͬ�ģ�       �����Ͷ�����أ������Ͷ����޹ء�
# 1. ����
#    ���֣�  
#�������������ڽ�������built-in-function����������c/c++��д�ģ� ���Ƕ���__builtins__ģ���Ȼ����
#����                 �û��Զ��庯�� user-defined   
#          lambda���ʽ
# 2. ����
#
# 3. �� ���ǿɵ��õ�
#
# 4. ʵ��:   
#    Ҫ���þ͵���д__call__() Ĭ��û��ʵ��
#    ʵ��Ĭ�϶��ǲ��ܵ��õģ���Ҫ����������()���� �� c= Cat()    c() �����Ǵ����
class Cat():
    def __call__(self,*args): #�Ὣ��ʵ�����õĲ���ȫ������call
        print '������',args
c=Cat()
c(2,43,54) #����__call__()

##############################
#һ���������  
# ����Ϊ�������߷�������
##############################





############################
# osģ��
# ��ƽ̨�޹� 
# ��Ҫ���� ����ȫ���ǵ�
############################
# ��������һ�������ڱ�д����Ҫ�κθĶ���Ҳ���ᷢ���κ����⣬�Ϳ�����Linux��Windows�����С�
# һ�����Ӿ���ʹ��os.sep����ȡ������ϵͳ�ض���·���ָ��

# os.name�ַ���ָʾ������ʹ�õ�ƽ̨���������Windows������'nt'��������Linux/Unix�û�������'posix'��
# os.getcwd()�����õ���ǰ����Ŀ¼������ǰPython�ű�������Ŀ¼·����
# os.getenv()��os.putenv()�����ֱ�������ȡ�����û���������
# os.listdir()����ָ��Ŀ¼�µ������ļ���Ŀ¼����
# os.remove()��������ɾ��һ���ļ���
# os.system()������������shell���  �����������еķ�����
# os.linesep�ַ���������ǰƽ̨ʹ�õ�����ֹ�������磬Windowsʹ��'\r\n'��Linuxʹ��'\n'��Macʹ��'\r'��
# os.path.split()��������һ��·����Ŀ¼�����ļ�����
#         >>> os.path.split('/home/swaroop/byte/code/poem.txt')
#         ('/home/swaroop/byte/code', 'poem.txt')
# os.path ϵ��
import os
print os.name
print os.getcwd()
print os.listdir(os.getcwd())
#os.system('cmd') # ��Ҫ���� ֮ǰ��֪���� �ǳ�����
#os.system('dir')
print os.linesep    #os.linesep�ַ���������ǰƽ̨ʹ�õ�����ֹ��  
print os.sep#os.sep ����ȡ������ϵͳ�ض���·���ָ����
print os.path.split('c:\\xx.tex')
# os.path.isfile()��os.path.isdir()�����ֱ���������·����һ���ļ�����Ŀ¼��
print os.path.isdir(os.getcwd())
print os.path.exists(os.getcwd()) #�����������������·���Ƿ���ش��� ��Ҫ
print os.path.abspath(os.getcwd()) #��þ���·��
print os.path.splitext('xx.ted') #:�����ļ�������չ��

#��Ҫ
print os.path.join(os.getcwd(),'xx.txt')  #:����Ŀ¼���ļ�����Ŀ¼

print os.path.basename('a.txt') #����ļ���
print os.path.dirname('c:\\Python\\a.txt') #���·����


############################
# sysģ��
# sys������python�Ļ��� ע����os����
############################