#-*- coding:gb18030 -*
'''
Created on 2016��3��16��
���У���Ա���������е� ����Ԫ�桢�ַ������б�
@author: Administrator
'''
########################################################################
#�ַ���
########################################################################
from __builtin__ import enumerate

#��׼���Ͳ�����
#��Ա��ϵ������ in��not in   if (obj in seq)
#��Ƭ������  ��ͨ���±��������Ԫ�صķ���ͨ����Ƭ��������
        # seq[a,b] ����±�a��b��Ԫ�ؼ���  ��Ҫ ֮ǰ��֪��   seq[0:3]��ͬ��seq[:3]
        # Խ��������������tuple index out of range
        # ��������������
        # ��Ҫ�����Ƭ������������ʼ��������β��ǰһ����
name='sunnanjun'
print name[0:-1] #���sunnanju
print name[::]
print name[0:9]
print name[0:8]
if name[4] in name:
    print 'find'
if 's' in name:
    print 'find'    

#len������еĳ���

#list()��tuple()�������б��Ԫ�����ͻ���ʱ�ǳ�����

#�ַ���  python���ַ���Ҳ�ǲ��ɱ��
#�ַ�������ֱ�ӱȽ� ��װasciiֵ�Ƚ�
#seq1+seq2  ������������ ��Ҫ ֮ǰ��֪�� ������ֱ���������� ��Ҫ
sex='man'
print sex+name
print 'age'+str(34)  #print 'age'+29 #�Ǵ����
#��ʽ�������� %d %% %g  %f %e %s %x
print name, '��������%d' % 24
print '%.2f' % 334.3435

#�ַ���ģ��

#ԭʼ�ַ������� ���㲻��ת�壡ֱ��. ʡȥ�˶�дһ��б�ܵ��鷳
print r'\n'
#·���о����õ�  f = open (r'c:\windows\t')

#unicode�ַ�������
name = u'abc��'
print name

#�ڽ����� cmp()    len()  max()�����ַ����������ַ�    min()�����ַ�������С���ַ�
#chr()  unichr()ת����Unicode��char
print chr(66),unichr(45)

#raw_input ���Ҫ���ã�
#user_input = raw_input("enter your name")
#print user_input

#��ν�������������ǿ��Բ�����Ӧ���͵Ķ��� ��str   unicode
print isinstance(u'\0xAB', str)  #str��һ������
print isinstance(u'\0xAB', unicode)
print isinstance(u'\0xAB', basestring)
#unicode��strʵ���϶��ǳ�����basestring������ ��Ҫ�� ע�����ͽз�
 
#����������һ���ַ���Խ���� ���԰������з����Ʊ�������������ַ�
#��������ʼ���ձ�����ν�����������ø�ʽ �����html
hi = '''
dfsdf
'''
print hi #���� ������Ϊֵ 
hi = '''
<html> <head></head> <body> </body></heaml>
'''
print hi #����������

#python����unicodeʱҪע�⣺
    #��Ҫʹ�ù�ʱ��stringģ��
    #ʹ��unicode()������str()
    #�����ַ���һ����u
    #��Ҫ��ʱ���ʹ��encode �� decode��������루�����硢���ݿ⣩

#unicode()�����Ǻ�strͬ��Ĺ�������

name = unicode('sunnanjun')
print name

#�ؼ����ܽ�
    #��Ҫ���ַ�Ӧ����Ϊ����Ϊ1���ַ��� 
    #�ַ���'' �򡰡���'''  '''
    #python�ַ�������ͨ��'\0��β��'  �㲻�ù��� �ַ���ֻ��������Ҫ�� ����


########################################################################
#�б�   ��Ԫ�����ͣ�ֻ����Ԫ���ǲ��ɱ�Ļ�˵ֻ����        ���У��б�Ԫ�棩
#��ν�ڽ��������ǳ�Ա���� built in
########################################################################

#��Ҫ��  �б���԰�����ͬ���͵Ķ��� ��cҪ���Ķ�
alist = [123,3545,6576,'4545',6456,['a','b',1],(343,(4,3),4546)]
emptylist = []
print alist
print emptylist #ֻ��ʾһ��[]

#append׷��
alist.append('sfsf')  #����+=
print alist

#��Ҫ�Ļ� һ����˵������Ա����Ҫȥɾ��һ���б���� �б������������򣬻��Զ�������

#������  ���ԱȽ� ������Ƚ�
list1=['abc','123']
list2=['abc','234']
print list1<list2
#��Ȼ����Ƭ
print alist[5][2] #��Ϊ�б�ɱ����б�

#��Ա������
if(6576 in alist):
    print 'in!'
blist = alist+list1
alist += list2 # ��ȻҲ��������  ����append
print blist
print alist

#�ظ��������� ֮ǰ��֪�� *
print list1*2  #�ظ�����
list1 *= 3
print list1

#���ַ���һ�� ʹ��enumerate����ö�ټ��� ���Բ鿴����
t = enumerate(alist)
print type(t)
for i in t:
    print i
#sorted
numlist=[34,5,4,6,7,6,8,34,3,634,25]
newlist = sorted(numlist) #ע�ⲻ��ı�ԭ���� ���ǹ�������
print newlist,sum(newlist)
print type(reversed(newlist)) #�������������
for i in reversed(newlist):
    print i
    
#list()��tuple()���Խ���һ���ɵ������� Ȼ��ǳ��������һ���µ��б��Ԫ��
print tuple(list1) #����һ���µ�Ԫ�� 

#��Ҫ���б�û��ר�ŵĲ������ͳ�Ա���ڽ��������� �������������У�
#���г�Ա������remvoe  pop  insert reverse extend sort  ע���빤��������ͬ ��Ա����(build_in)��ı�����
list1.reverse()
print list1


########################################################################
#Ԫ�� tuple ��סӢ��   ���ɱ䣡
#Ԫ��Ҳ�ܰ�����������!�����б�
#��Ҫ��֮ǰ��֪�������ֻ��һ��Ԫ�أ���Ҫ��Ԫ�غ����һ�����ţ��������ͳ�һ����ͨ�����ţ�
########################################################################
tuple1 = (123,3545,True,'4545',6456,['a','b',1],(343,(4,3),4546))
print tuple1

tuple2 = () #��Ԫ��
print tuple2

tuple3 = (3)
print tuple3 #tuple����3����
tuple3 = (3,)
print tuple3 #����������ķ���

#ĳ�����������Ǹı���Ԫ�� ����ʵ�ʲ��ǵ� �㶮��
tuple3 = tuple3 + (34,54)
print tuple3

#Ĭ��Ԫ�� ��Ҫ�� ��֮ǰ��֪��
#����ж������ġ����ŷָ��ġ�û����ȷ���Ŷ���ģ�Ĭ�Ͼ���Ԫ��
#�� 
def fun():
    return 1,2,3  # Ҳ���� return (1,2,3) ���к������صĶ������Ԫ��
def fun2():
    return (1,23,4)
def fun3():
    return [24,35] #��Ȼ����Է���һ���б�
x,y=1,2

#��Ԫ��Ԫ���мǼӶ���

#��ʱʹ��Ԫ����б� �統����Ҫά����������ʱ

print type(__name__)
if __name__ == '__main__':
    print 'duli'
    
    
    