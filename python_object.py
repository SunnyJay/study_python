#-*- coding:gb18030 -*-

'''
Python��������

@author: Administrator
'''
import datetime

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
#��Ҫ ��ѧ������True��False�ֱ��Ӧ1��0  ����ֱ������
print 232+True
print 232+False
# ��Ҫ������    �ռ��ϡ����ַ���������ֵΪ0������None�Ĳ���ֵ ��False
dict={}
if not dict:
    print 'false'
if 1:
    print '1'
if not 0:
    print 'not 0'
if not None:
    print 'not none'    
    
#pythonû�У������� �������not
if not 3>4:
    print 'x'
    
######################################
# ʱ�� ר��
#####################################
# ʱ����������Ϊ��λ�ĸ���С����
#Python �ṩ��һ�� time \ calendar\datetime ģ��������ڸ�ʽ�����ں�ʱ��

# ��Ҫ���� time�ǹ�����Generic Operating System Services�У����仰˵�� ���ṩ�Ĺ����Ǹ��ӽӽ��ڲ���ϵͳ����ġ�
#         �����ǻ���Unix Timestamp�����������ܱ��������ڷ�Χ���޶��� 1970 - 2038 ֮��
#         ���ԣ������д�Ĵ�����Ҫ������ǰ��������Χ֮������ڣ��ǿ�����Ҫ����ʹ��datetimeģ�����




#########################
# time 
##########################

# Python �� time ģ�����кܶຯ������ת���������ڸ�ʽ���纯��time.time()���ڻ�ȡ��ǰʱ���
import time
print time.time()  #��Ȼʱ����޷���ʾ1970ǰ

# 1. ��ȡ��ǰʱ�� 
# struct_timeԪ�飨����linux c�нṹ�壩  timetuple
# localtime����
localtime = time.localtime(time.time())
print "����ʱ��Ϊ :", localtime

# 2. ��ȡ��ʽ����ʱ��
#    ��򵥵Ļ�ȡ�ɶ���ʱ��ģʽ�ĺ�����asctime():  asc!
localtime = time.asctime( time.localtime(time.time()) )  # ��һ����װ
print localtime

# 3. ��ʽ������, ��Ҫ��
# ʹ�� time ģ��� strftime ��������ʽ������
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 4. ת��ʱ�������Ҫ  mktime
timestamp=time.mktime(time.localtime())
print timestamp
mytime =  time.gmtime(timestamp) #ת����Localtime
print mytime

#########################
# datetime  ��time������
#########################
#    ��datetime ģ��,�õñȽ϶���� datetime.datetime �� datetime.timedelta
#    ʹ��datetime.datetime.now()���Ի�õ�ǰʱ�̵�

print datetime.datetime.now() #��ȡ��ǰdatetime
print datetime.date.today()  # ��ȡ����date

#ת����datetime <=> string
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # strftime

mydatetime =  datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S") 
print type(mydatetime)

#ת��datetime <=> date
print datetime.datetime.now().date()

#ת��datetime <=> timestamp
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())

print datetime.datetime.fromtimestamp(1421077403.0) #�����Ҫ��


