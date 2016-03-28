#-*- coding:gb18030 -*
'''
Created on 2016��3��24��
�����ͺ���ʽ��� method
@author: Administrator
'''
#��Ҫ python��void��Ӧ����None ֮ǰ��֪��
def hello():
    print 'xx'
res = hello()

print res #�����None

#ʵ����python��������Ҳ��һ������ ֻ������������

#python֧��Ĭ�ϲ���

#��Ҫ ������  ǧ�������ָ��
#func(*������, **�ؼ��ֲ����ֵ�)

#python ����λ��û��Ӱ�죡��������Բ�������ǰ��������
def bar():
    print 'bar'
def foo():
    print 'foo'
    bar()
    
def foo2():
    print 'foo2'
    bar2()  #���������
def bar2():
    print 'bar2'    
    
#�����ǿ���ӵ�����Ե� ����Զ�̬����  ���ƿռ��ں������
bar2.xx = 'sds'
bar2.version = 0.1
print bar2.xx 
print bar2.version


#��Ƕ����  ֮ǰ��֪�� 
def foo_out():
    def bar_in():  #���ﶨ�壬��Ȼ���ⲿ���ܵ����� 
        print 'bar_in'
    print 'foo_out'
    bar_in() #�������    ֻ���ڲ�����
foo_out()
#foo_out.bar_in()

##########################################################
# ������װ���� ��Ҫ��flask����õ��ˣ�
#    ��ʽ��  @װ������(��ѡ����) 
# װ����ʵ���Ͼ���һ����������@����,������װ��һ���������������Ǻ�������

# ��Python�У�װ����ʵ����ʮ�ַ����
# ԭ���ǣ��������Ա�������ȥ��
# ������Ϊһ������

#װ������һ������,һ��������װ�����ĺ�����װ�����ں���������ɵ�ʱ�򱻵��ã�����֮�󷵻�һ���޸�֮��ĺ������󣬽������¸�ֵԭ���ı�ʶ����������ɥʧ��ԭʼ��������ķ���(�����ĺ���������һ����װ����װ�ι���ĺ���)
#�����Ƕ�ĳ������Ӧ����װ�η����� ��ʵ�͸ı��˱�װ�κ������������õĺ����������ڵ㣬ʹ������ָ������װ�η��������صĺ�����ڵ㡣
#�ɴ����ǿ�����decorator�ı�ĳ��ԭ�к����Ĺ��ܣ���Ӹ��ֲ�����������ȫ�ı�ԭ��ʵ��

#װ������Ϊ�޲���decorator���в���decorator
#װ�����в�/�޲Σ������в�/�޲Σ���Ϲ�4��
###########################################################

#�޲���װ���� �C ��װ�޲�������
def decorator(func):
    print "hello"
    return func
@decorator  #����ֻҪ����ʱ��ִ��װ���� ��Ȼ�󷵻�һ����װ��ĺ������󣬶�������ӻ���food���������Ժ�ʹ��ʱֱ���õľ����µģ�
def food1():
    pass
food1()  #�ȼ��� foo = decorator(foo) ; foo()

#�޲���װ���� �C ��װ����������  ��Ҫ��Ҫ�Դ���ĺ����Ĳ��������ٴ��������ڲ���Ҫ�ٶ���һ��������
def decorator_func_args(func):
    def handle_args(*args, **kwargs): #�����뺯���Ĳ���
        print "begin"
        func(*args, **kwargs)   #��������
        print "end"
    return handle_args

@decorator_func_args
def food2(a, b=2):
    print a, b

food2(1)  #�ȼ���  foo2 = decorator_func_args(foo2);foo2(1)

#������װ���� �C ��װ�޲�������
def decorator_with_params(arg_of_decorator):#������װ�����Ĳ���
    print arg_of_decorator  #���Ƕ��˸��������ѣ�ûʲô�ѵ�
    #���ձ����صĺ���
    def newDecorator(func):
        print func
        return func
    return newDecorator
@decorator_with_params("deco_args")
def food3():
    pass
food3()     #�ȴ�ӡ����deco_args,Ȼ����Ǳ���װ����

#python ����װ����  staticmethod,classmethod, property

#1. staticmethod ���ж����ʵ��������ɾ�̬����  �൱��ȫ�ֺ��� �����ھ�̬�����еľ�̬����
     #�����Ϻ�һ��ȫ�ֺ������(����Ҫ����self��ֻ��һ��Ĳ���)��ֻ��������ͨ��������ʵ�����������ã�������ʽ�ش����κβ�����
#2. property
    #�������ԵĲ�����������java�ж���getter/setter
    
class A():
    @staticmethod
    def test_static():
        print "static"
    def test_normal(self):
        print "normal"
    @classmethod
    def test_class(cls):
        print "class", cls

a = A()
A.test_static()  #��������.����
a.test_static()
a.test_normal()
a.test_class()


class B():
    def __init__(self):
        self.__prop = 1
    @property
    def prop(self):
        print "call get"
        return self.__prop
    @prop.setter
    def prop(self, value):
        print "call set"
        self.__prop = value
    @prop.deleter
    def prop(self):
        print "call del"
        del self.__prop
        
#װ������˳�����Ҫ����Ҫע��
# @A
# @B
# @C
# def f ():
# �ȼ��� f = A(B(C(f)))



###########################################################
#  Ĭ�ϲ����Ϳɱ����
#  ���б�Ҫ������Ҫ��Ĭ�ϲ���֮ǰ
###########################################################
#Ĭ�ϲ���
# λ�ñ��뿿��
# def taxme2(rate=0.23,cost) #����
def taxme2(cost, rate=0.23):  #��ȷ
    print 'cost',cost,'rate',rate
    pass
# ���õ�ʱ�����ָ���˲����������Բ�����˳�����
taxme2(3,4)
taxme2(3)
taxme2(cost=4)
#taxme2(rate=4)
taxme2(rate=4,cost=5) #���Բ�����˳��

# �ɱ䳤���� ��Ҫ��֮ǰ���˽⣬�������֣��ǹؼ��ֿɱ������Ԫ�棩���ؼ��ֿɱ�������ֵ䣩��  **�����ع��ˣ��Ա㲻�������㷢�ͻ���
# �ǹؼ��ɱ䳤�Ĳ���Ԫ�������λ�ú�Ĭ�ϲ���֮��
# �ؼ��ֿɱ�������뺯�������һ����

#�����ǹؼ��ֿɱ����  *
#�Ǻ�֮��������βν���ΪԪ��the Rest���ݸ�������
def fun1(arg1,arg2='xx',*theRest):  
    print 'arg1:',arg1
    print 'arg2:',arg2
    for arg in theRest:
        print arg
fun1(3,5,6,545,455,34,'f')  # 6�Ժ�Ķ�һ����Ϊһ��Ԫ��theRest��������
list1=(3,3,545)
fun1(3,5,list1)  #��������

#2���ؼ��ֿɱ���� ���ָ������ **
#�ֵ��еļ�Ϊ��������ֵΪ��Ӧ�Ĳ���ֵ��
def fun2(arg1,arg2='xx',**theRest):  #�Ǻ�֮��������βν���Ϊ�ֵ�the Rest���ݸ�������
    print 'arg1:',arg1
    print 'arg2:',arg2
    for arg in theRest:
        print arg,':',theRest[arg]
fun2(3,5,a=6,b=545,c=455,d={'a':'b','c':'d'})  # �ɱ������������һ��Ԫ������ֵ�
dict1={3:4,'3':5,2:545}
fun2(3,dict1)  #��������  #���ﲻ�� Ϊʲ������fun2(3,9,dict1) ��������


###########################################################
#  ����ʽ���
#  ��ʱ����Ҫ�˽�
###########################################################

###########################################################
#  ����������
#  global���
#  �հ�
#global�����������x��ȫ�ֱ������������ں����ڸ�x��ֵʱ�����ĸı�ӳ�䵽������������ʹ�õ�x��ֵ��
###########################################################

#Ϊ����ȷ����һ����������ȫ�ֱ���������ʹ��global��䣡 ���Բ��ô���һ���ֲ�����  ��Ҫ ֮ǰ��֪��
# global a,b,c  

#����������ں��ı�����ᵽ ��Ҫ��
#�ں��������������ı������������ں�����ʹ�õ�����ͬ������û���κι�ϵ�����������ƶԺ�����˵�Ǿֲ��ġ�
#��б����ķ�Χ�����б����������Ǳ������Ŀ�ķ�Χ�������ƶ���ĵ㿪ʼ�� 
def fooo():
    bar = 200
    print 'in bar:',bar
bar = 33
print 'out bar:',bar
fooo()
print 'out bar:',bar  #��fooo�е�bar�������barû�й�ϵ

# global
print '*************************global************************'
def foooo():
    global bar 
    bar = 200  #��������global�� ���Ǿоֲ���
    print 'in bar:',bar
bar = 33
print 'out bar:',bar
foooo()
print 'out bar:',bar  

#�հ� ֮ǰû������
#һ���հ������������һ������A���������A������һ������B���㡣������صĺ���B�ͽ����հ������ڵ��ú���A��ʱ�򴫵ݵĲ����������ɱ�����
#��һ�ֳ��� ����python�к���ҪҲ�ܳ�����һ��ʹ�ó�������װ������PythonΪװ�����ṩ��һ�����Ѻõġ��﷨�ǡ�����@�������ǿ��Ժܷ����ʹ��װ����
#�հ��ⶫ������������Ǻ����׵ģ���Python�е�Ӧ��Ҳ�ܹ㷺
def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()   #my_line����һ��line�����Ķ��� 
print(my_line(5))  

#������  �˽⼴��
#�������ǵ�������ͬʱҲ���������ǵ�����������������֮�����;ʵ���ǲ��࣬�������ǿ��Դ�����˵���������ṩ�˷ǳ�������Զ����������;����
#������ȷ�ţ�����������һ�ֵ�������������ӵ��next����������Ϊ���������ȫ��ͬ������ζ��������Ҳ��������Python��forѭ���С�
#���⣬�����������������﷨֧��ʹ�ñ�дһ�����������Զ���һ������ĵ�����Ҫ�򵥲��٣�����������Ҳ����õ�������֮һ��
def get0_1_2():
    yield 0
    yield 1
    yield 2
xx = get0_1_2()  #��������������������һ����������
print xx.next()
print xx.next()
print xx.next()


