#-*- coding:gb18030 -*-

'''
Python��������

@author: Administrator
'''

# type()�������Եõ��ض������������Ϣ
print type(42)
print type('sunnanjun')
# ����Ҳ�Ƕ����������Ͷ����������type ������python���͵ĸ�������python��׼���Ĭ��Ԫ��metaclass
print type(type(42))

# None��python��Null����(�䲼��ֵ����False)

#����ֵ�Ƚ�
print 2 != 2
print 2 <> 2 #����д��������

#�������ñȽϣ���������ݱȼۣ�id������is�ؼ���
a = 'sun'; b = 'sun';c = 'nan'
print id(a) == id(b) #�������ͬ
print a is b 
print a is not c

#id���� ��ö��������ֵ
print id(a), id(b)

#�������� and or not
print not(a is b)

#python֧������һ�����ʽ���ֱȽϲ���  3<4<5
print 3<4<7
a = 4
if 2<a<5:
   print 'OK'

#��׼�����ڽ����� cmp str type repr��`obj` ���Ƕ����ڻ�������
print cmp(3,4) #����-1 0 1
print str(3) #�����Ҫ ���ض���Ŀɶ��Ժõ��ַ��������û��Ѻ�
print repr(3),`3` #ע����str����������ǹٷ��ַ�����ʾ����python�Ѻ�

#python��֧�ַ����������أ��мǣ�
print type([]),type({}),type(())

#ʹ��isinstance  ���ȵ���typesģ��
import types #��from types import IntType
num=4
if type(num)==types.IntType:
    print 'is int'
if isinstance(num, int): #int��ʵ�Ǹ���
    print 'is int'

#python��֧�ֵ�����
#char byte
#python֧�ֵ��������ͣ�
#���͡������͡������͡�˫���ȸ����͡�ʮ���Ƹ����͡�����
#python��׼���͵�ͬ��c��long
#�����ͼ�L����
num = 12234454546545L
print num
#δ����ͳһ���ͺͳ����� �û��о����������͵Ĵ��ڣ���Ҫʱ���ͻ��Զ�ת��Ϊ��

#python��������������һ��
print 1/2,1.0/2.0,8%3
#������
print 3**3 #pow
#λ������
print ~1 #��λȡ��

#����������͵��ڽ����� ��Ҫ
#int() long() float() complex() bool()  ע��python���в������͵�
print int(23.4),float(4),bool(3),bool(0),bool(-1)
#abs() pow() round()��������
print abs(-4),pow(3,3)

#����ת������ ֱ�ӷ��ض�������ַ��� ��Ҫ
#hex()  oct()
print hex(234)
print type(hex(234)) #����������str

#asciiת������ ��Ҫ ord chr
print ord('3')
print chr(97)

#�������� 
#��Ҫ ��ѧ������True��False�ֱ��Ӧ1 0  ����ֱ������
print 232+True
print 232+False