#-*- coding:gb18030 -*
'''
Created on 2016��3��17��

ӳ��ͼ�������
@author: Administrator
'''

#############################################
#�ֵ���Ψһӳ������ �ֵ�������������͵ļ�
#��������dict���Դ����ֵ�  
#############################################


#����һ���ֵ䣬������.keys()������Ҳ�����õ�������
dict2 = {'name':'sunnanjun','port':80}
#����һ
for key in dict2.keys():
    print key
#������ ���ָ����� key����key
for key in dict2:
    print key, dict2[key]
#���һ���������Ƿ���ĳ��key����÷���ʽin not in; ��������has+key
if 'name' in dict2:
    print 'has'
if dict2.has_key('name'):
    print 'has'    


#�����ֵ�
dict2['age'] = 66 #ֱ������
print dict2
#����ֵ�
dict2.clear()

#�ֵ�Ҳ���ԱȽ� �㷨�Ƚϸ��ӣ�
    #���ǱȽ��ֵ䳤�� Ȼ���Ǽ� �����ֵ
#len() dict()����һ���������ֵ�
#ע�� �ֵ��е�Ԫ����û��˳���
dict2 = {'name':'sunnanjun','port':80}
print len(dict2)
print dict(x=1,y=2)

#���ض���Ĺ�ϣֵ��Ҳ�����ж�ĳ�������Ƿ��ǿɹ�ϣ��
print hash('sun')  

#�ֵ��ڽ����� ��Ҫ��
print dict2.keys()
print dict2.items() #�����Ҫ
print dict2.values()
print dict2.get('name')
print dict2.setdefault('sex', 'man') #��Ҫ �ж��Ƿ���� �������������벢����
print dict2

#�ֵ�ļ������ǿ��Թ�ϣ��
#�󲿷ֶ��󶼿��ԣ������б��ֵ�ȿɱ����ͣ������ǲ��ܹ�ϣ�ģ����Բ�����Ϊ��
dict3={():33} #Ԫ���ǿ��Ե�
dict3={(5,):'df'}
print dict3[(5,)]

#һЩ�ɱ����Ҳ�ǿ��Եģ�ǰ���Ǳ���ʵ��__hash__����������java




#############################################
#����
#python�еļ��Ϸ�Ϊ�ɱ伯��set�����ɱ伯��frozenset
#���ϱ���������ģ��޷������޷���Ƭ�޷����ݼ�����
#############################################


#����Ψһ�Ĵ�����ʽ��set()��frozenset()   ��Ҫ
s = set('haha')  #ֻ����a\h 
print s
print type(s)
print len(s)
#֧��in not in

#���ϲ��� 
s.add('z')
s.remove('a') #�����������������
s.discard('a') #�������ԭʼ����ɾ����   �����ڲ��������
s.pop() #ɾ������Ԫ�� ��Ҫ
s -= set('h')
print s

#== != ���ϵȼ�ָ����Ԫ��
#�ж��Ӽ����� > >= < <=
print set('sunnanjun') == frozenset('sunnanjun')
print set('sunnanjun') < set('nanjuncoke')

#�������Ͳ����� ��Ҫ
#����| ����& �- �ԳƲ�ּ���� ^
t=set('sunnanjun')
t=set('nanjuncoke')
print t
print s|t   
print s&t
print s-t
print s^t #����ͬʱ����

# |= &= -= ^=
# |= �൱��update
s=set('a')
s |= set('vb')
print s
s.update('ct') #����
print s

#���ɱ伯��
f = frozenset('reysfh')
#f.remove('h')

#set��frozenset�Ĳ��������ǿɵ����� �����С��ַ���  ��֧�ֵ����Ķ��������ֻ��ֵ�  ��Ҫ����
set()#�������ڳ�ʼ�ռ���
print set('fsg')
print set((343,5656))
set([])


