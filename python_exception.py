#-*- coding:gb18030 -*

'''
Created on 2016��3��24��
������쳣
BaseException �������쳣�Ļ���   Exception�ǳ������Ļ���
@author: Administrator
'''

#�����쳣
#NameError name 'foo' is not defined
#AttributeError ���Է���δ֪�Ķ�������

#try������֣�tryexcept  tryfinally 
try:
    f=open('blah', 'r')
except Exception,e:  #����eָ�쳣����  
    print 'could not open file:',e

#', e'���Բ�Ҫ
try:
    f=open('blah', 'r')
except Exception:  #����eָ�쳣��Ϣ  ', e'���Բ�Ҫ
    print 'could not open file'   

#���ж��except��䣬Ҳ������һ��except�д������쳣
try:
    f=open('blah', 'r')
except (ValueError, TypeError):  #����eָ�쳣��Ϣ  
    print 'could not open file:',e

#��Ҫ�������Ҫ���������쳣��ʹ��BaseException

#Exception,e:
#e��Exception���һ��ʵ��
#ʹ��str(e)�ܷ���һ�����ÿ̿ɶ����쳣
try:
    f=open('blah', 'r')
except Exception,e:  #����eָ�쳣����  
    ret = str(e)
    
#��Ҫ�� elseҲ�������try  ���try�еĴ���û�з����쳣����ִ��else!
try:
    f=open('blah', 'r')
except Exception,e:  #����eָ�쳣����  
    ret = str(e)
else:
    print 'û�з�����'
# ����д��    

# try
# except
# else
# finally

# try
# finally

#�����Ĺ���  ��Ҫ
# with���ڼ���Դ���ͷ� ������δ��뿪ʼ�����м���߽��������쳣��with����ִ��������룬��Ȼ���Զ��رգ�  
with open('/etc/passwd','r') as f:
    for eachLine in f:
        #code...
        
        
#�����쳣 ���׳��쳣 raise  ��ʽ�Ƚ϶�
# raise �쳣���� ��ѡ���������������쳣�� 
# һ��ʹ��raise ��  �Ϳ����ˣ� �������ַ����쳣

#����
#assert 1 == 0

#��Ȼ��Ҳ�ܴ����쳣 �̳����쳣��
# class NetWorkError(IOError):
#     pass