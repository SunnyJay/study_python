#-*- coding:gb18030 -*
'''
Created on 2016��4��8��
����
��Ҫ������ѩ��
@author: Administrator
'''
# �߽׺������
#    �Ѻ�����Ϊ�������룬�����ĺ�����Ϊ�߽׺���������ʽ��̾���ָ���ָ߶ȳ���ı�̷�ʽ��

#####################
# map/reduce
#####################

#Python�ڽ���map()��reduce()������
# map()������������������һ���Ǻ�����һ�������У�map������ĺ���"����"���õ����е�"ÿ��"Ԫ�أ����ѽ����Ϊ�µ�list���ء�
# reduce��һ������������һ������[x1, x2, x3...]�ϣ�������������������������reduce�ѽ�����������е���һ��Ԫ�����ۻ�����.

#ʵ�� int()����������ȫ�����Լ�дһ�����ַ���ת��Ϊ�����ĺ�����
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

print str2int('353467')

#####################
# filter  ��Ҫ
# Python�ڽ���filter()�������ڹ������С�
#####################

# ��map()���ƣ�filter()Ҳ����һ��������һ�����С���map()��ͬ��ʱ��filter()�Ѵ���ĺ�������������ÿ��Ԫ�أ�Ȼ����ݷ���ֵ��True����False�����������Ƕ�����Ԫ�ء�
#���磬��һ��list�У�ɾ��ż����ֻ����������������ôд��

def is_odd(n):
    return n % 2 == 1  #True�ı���
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# ���: [1, 5, 9, 15]


#############################
# sorted ��Ҫ
##############################

# Python���õ�sorted()�����Ϳ��Զ�list��������
print sorted([36, 5, 12, 9, 21])

#���⣬sorted()����Ҳ��һ���߽׺������������Խ���һ���ȽϺ�����ʵ���Զ�������򡣱��磬���Ҫ�����������ǾͿ����Զ���һ��reversed_cmp������

def mycmp(x, y): #�Զ���һ����������
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], mycmp)


#Ĭ������£����ַ��������ǰ���ASCII�Ĵ�С�Ƚϵģ�����'Z' < 'a'���������д��ĸZ������Сд��ĸa��ǰ�档
#���ڣ������������Ӧ�ú��Դ�Сд��������ĸ������Ҫʵ������㷨�����ض����д����ӸĶ���ֻҪ�����ܶ�������Դ�Сд�ıȽ��㷨�Ϳ��ԣ�

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)