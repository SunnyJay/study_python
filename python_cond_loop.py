#-*- coding:gb18030 -*
'''
Created on 2016��3��18��

������ѭ��
@author: Administrator
'''

#��Ԫ������  X if C else Y
x, y =4, 3#����д���Ҿ�Ȼ��֪�� #������ν�Ķ�Ԫ��ֵ
smaller = x if x < y else y
print smaller

#��Ԫ��ֵ  ��ʵ������Ԫ��
x,y,z=1,2,'a'
print x,y,z 

#��������ֵ
x,y=y,x
print x,y

#���ظ�ֵ
x=y=z=1

#forѭ��
for i in 'sunnanjun':
    print i
    
#for�������ַ��������������������������enumerate����
for i in range(len('sunnanjun')):
    print 'sunnanjun'[i]

for i in enumerate('sunnanjun'):  #ÿ��i��һ��Ԫ��
    print i

#range����  ��Ҫ  ���᷵��һ���б�
# range(begin,end,step=1)
# range(2,19,3)
# range(3,5) ��ʾ3 4 5
# range(5) ��ʾ0-4  ������򵥵��﷨
print range(3,19,3)
print range(6)

#xrange  ����Զ����range

#sorted reversed enumerate zip
#zip��

#pass���
#pass��䲻���κ��� NOP(no operation)
#��Ҫ pass������Ϊ�������� ������������ռλ �Ժ�����ɱ�д
def fun():
    pass

#��Ҫ while��else
#����ifelse�У� whileҲ�ɺ�else���ʹ��
#else����while������ִ�У�����break!
count = 0
while count>4:
    if count >3:
        break;
    count +=1
    
else:
    print count, 'ѭ������'                                                                                                                                                                                                                                                                

#��������iter()����
#��һ���������iter()�������ܵõ�������
myTuple=(123,'zxs',3453.6)
i=iter(myTuple)
print i.next()
#��Ҫ ���л��Զ��Ĳ�����������for i in seq:  ʵ������ʹ�õ������ġ�

#�ֵ���ļ�Ҳ�ǿ��Ե�����
#�ɱ������ ���ɱ������

#�б����   list comps  ���ڶ�̬�����б�
#�����ʱ���о�


#���������ʽ
#�����ʱ���о�
