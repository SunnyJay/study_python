#-*- coding:gb18030 -*-
'''
Created on 2016��3��30��
  �ܶ�������ѩ��Ľ̳�
@author: Administrator
'''
#��β鿴������Щ����  ���ַ�����1. dir() �б�     2. __dict__����  �ֵ�
from types import MethodType

# ͬJava����һ����Pythonʹ�������ü�����һ�򵥼�����׷���ڴ��еĶ���
# ��Python�ڲ���¼������ʹ���еĶ�����ж������á�
# һ���ڲ����ٱ�������Ϊһ�����ü�������
# �����󱻴���ʱ�� �ʹ�����һ�����ü����� �������������Ҫʱ�� Ҳ����˵�� �����������ü�����Ϊ0 ʱ�� �����������ա�
#���ǻ��ղ���"����"�ģ� �ɽ��������ʵ���ʱ��������������ռ�õ��ڴ�ռ���ա�

a = 40      # ��������  <40>
b = a       # �������ã� <40> �ļ���
c = [b]     # ��������.  <40> �ļ���

del a       # �������� <40> �ļ���
b = 100     # �������� <40> �ļ���
c[0] = -1   # �������� <40> �ļ���


#__init__()���ƹ����� ��ʵ���ϲ��ǹ�����

class Animal:
    '���ĵ��ַ���'  #��Ҫ���ඨ�壬֮ǰ��֪����������__doc__��ӡ����
    name = 'ss'  #���������Ҫ��
    def __init__(self,name):
        self.name = name #���������
        
    def show(self):
        print 'name is',self.name,Animal.name
        

animal = Animal('jack')  #�����������������һ����������ṩ���вι��죬��ϵͳ�����ṩĬ�Ϲ��� ����ĵ��þͻ����
#animal = Animal() #�����
animal.show()
print Animal.__dict__
dir(Animal)


class Dog(Animal):
    'Dog class'
    def __init__(self,name):
        self.name = name #���������
        
    def show(self):
        print 'dog name is',self.name

dog = Dog('����')
dog.show()


########################
# ����������  ��Щ������̳�
#######################
print '������**********************************'
print Dog.__name__
print Dog.__doc__
print Dog.__bases__  #������ɵ�Ԫ��
print Dog.__dict__   #����
print Dog.__module__  #����ģ��
print dog.__class__ #ʾ����Ӧ����
print type(Dog),type(dog)   #һ���ࡢһ��ʵ��


#����__init__�������ڴ���ʵ����ʱ�򣬾Ͳ��ܴ���յĲ����ˣ����봫����__init__����ƥ��Ĳ���


#�������� __del__ ��__del__�ڶ������ٵ�ʱ�򱻵��ã��������ٱ�ʹ��ʱ��__del__�������У�
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "����"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # ��ӡ�����id
del pt1
del pt2
del pt3


########################
#�̳�
########################
# ��python�м̳��е�һЩ�ص㣺
# 1���ڼ̳��л���Ĺ��죨__init__()���������ᱻ�Զ����ã�����Ҫ����������Ĺ���������ר�ŵ��á�  ��Ҫ ���������Բ�һ��
# 2���ڵ��û���ķ���ʱ����Ҫ���ϻ��������ǰ׺������Ҫ����self���������������������е�����ͨ����ʱ������Ҫ����self����  ��Ҫ 
# 3��Python�������Ȳ��Ҷ�Ӧ���͵ķ�������������������������ҵ���Ӧ�ķ��������ſ�ʼ��������������ҡ������ڱ����в��ҵ��õķ������Ҳ�����ȥ�������ң���
# ����ڼ̳�Ԫ��������һ�����ϵ��࣬��ô���ͱ�����"���ؼ̳�" ��
class Parent:        # ���常��
   parentAttr = 100
   def __init__(self):
      print "���ø��๹�캯��"

   def parentMethod(self):
      print '���ø��෽��'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "�������� :", Parent.parentAttr
   def fun(self):
       print '���෽��'

class Child(Parent): # ��������
   def __init__(self):
      print "�������๹�췽��"

   def childMethod(self):
      print '�������෽�� child method'
   def fun(self):
      #Parent.foo(self)  ���ַ����Ƽ�
      print '���෽��'
   def __str__(self):
       return '���Ǻ���'
p = Parent()
c = Child()          # ʵ��������
c.childMethod()      # ��������ķ���
c.parentMethod()     # ���ø��෽��
c.setAttr(200)       # �ٴε��ø���ķ���
c.getAttr()          # �ٴε��ø���ķ���
c.fun()
Parent.fun(c)  #���ø�����б����ǵķ����� ����һ�㲻�������� ����������fun���ȵ���P.foo(self)
print c

##########################
#�������ط���
##########################
# __init__ ( self [,args...] )
# ���캯��
# �򵥵ĵ��÷���: obj = className(args)

# __del__( self )
# ��������, ɾ��һ������
# �򵥵ĵ��÷��� : dell obj

# __repr__( self )
# ת��Ϊ����������ȡ����ʽ
# �򵥵ĵ��÷��� : repr(obj)

# __str__( self )  �൱��tostring
# ���ڽ�ֵת��Ϊ�������Ķ�����ʽ
# �򵥵ĵ��÷��� : str(obj)

# __cmp__ ( self, x )
# ����Ƚ�
# �򵥵ĵ��÷��� : cmp(obj, x)

# __iter__
##########################
#���������   __str__  __add__  __iadd__(ԭλ�ӷ�����+=)  
##########################
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):  #���� + 
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2



#############################
#�������뷽��  
# 1.��Ҫ  Ĭ����������Զ��ǹ�����   ���Ūget set
# 2.�ǳ���Ҫ��һ��  �������ɵظ�һ��ʵ�����������ԣ����磬��ʵ��bart��һ��name���ԣ�������û�У����ǿ��Զ�̬�ĸ�ʵ���󶨣�
#############################
# ˽�����ԣ�
# _private_attrs�������»��߿�ͷ������������Ϊ˽�У�����������ⲿ��ʹ�û�ֱ�ӷ��ʡ������ڲ��ķ�����ʹ��ʱ self.__private_attrs��
# ˽�з�����
#private_method�������»��߿�ͷ�������÷���Ϊ˽�з���������������ⲿ���á�������ڲ����� self.__private_methods

class JustCounter:
    __secretCount = 0  # ˽�б���
    publicCount = 0    # ��������

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount  # ����ʵ�����ܷ���˽�б���

#��Ҫ��
#Python������ʵ�������ࣨע�� ʵ����������˽�����ݣ��������ʹ�� object._className__attrName �������ԣ������´����滻���ϴ�������һ�д��룺
print counter._JustCounter__secretCount

#��̬������
counter.newA = 3  # newA�Ƕ�̬�󶨵� ��û�� ��������Ķ���û�� ��Ҫ
print counter.newA  #Ҳ����˵����������ʵ����������Ȼ���Ƕ���ͬһ����Ĳ�ͬʵ������ӵ�еı������ƶ����ܲ�ͬ 

#############################
#��̬  
#�κ��࣬���ն�����׷�ݵ�����object
##############################

#�ж�һ�������Ƿ���ĳ�����Ϳ�����isinstance()�жϣ�
print isinstance(c, Child)
print isinstance(c, Parent)
#����c��������Dog��c����Animal��

def run_twice(Parent):
    Parent.fun()
    Parent.fun()
    
# ����Ƕ�̬
run_twice(c)
run_twice(p)

################################
# ��ȡ������Ϣ
#################################

#�������ж϶������ͣ�ʹ��type()����
#Python��ÿ��type���Ͷ�������˳���������typesģ���ʹ��֮ǰ����Ҫ�ȵ���
import types
print type('abc')==types.StringType

#isinstance()
#����class�ļ̳й�ϵ��˵��ʹ��type()�ͺܲ����㡣����Ҫ�ж�class�����ͣ�����ʹ��isinstance()������

#����__xxx__�����Ժͷ�����Python�ж�����������;�ģ�����__len__�������س���
# len()��ʵ�ȼ���l__len()__
    #��������len()������ͼ��ȡһ������ĳ��ȣ�ʵ���ϣ���len()�����ڲ������Զ�ȥ���øö����__len__()����  ��Ҫ ֮ǰ��֪����
#��Ȼ��Ҳ����д__len__�ͺ� __str__һ��

#��Ҫ������ ֮ǰ��֪����  getattr  setattr    �Լ�hasattr    
#���������Ժͷ����г����ǲ����ģ����getattr()��setattr()�Լ�hasattr()�����ǿ���ֱ�Ӳ���һ�������״̬��  ���Ժͷ�����������

print hasattr(c,'name')
print hasattr(c,'fun')
fun= getattr(c, 'fun') #��ȡ���� 
fun() #�ٵ��÷��� ��Ҫ
setattr(c,'newattr',54)  #���������
print getattr(c,'newattr')  #���������
print c.newattr #���������
# �����ͼ��ȡ�����ڵ����ԣ����׳�AttributeError�Ĵ���
# print c.xx
#���Դ���һ��default������������Բ����ڣ��ͷ���Ĭ��ֵ��
print getattr(c, 'z', 404) # ��ȡ����'z'����������ڣ�����Ĭ��ֵ404

###########################
#  ��̬������ ��slots
##########################
#ǰ���ᵽ��һ������̬�����ԣ���������ͬ������Ծͻ�ò��������Կ��Ը���class�󶨣�������Ҷ��ܻ��:
def set_score(self, score):
    self.score = score
Child.set_score = MethodType(set_score, None, Child)
c.set_score(23)
print c.score

#���������Ҫ����class��������ô�죿���磬ֻ�����Studentʵ�����name��age���ԡ�
#Ϊ�˴ﵽ���Ƶ�Ŀ�ģ�Python�����ڶ���class��ʱ�򣬶���һ�������__slots__�����������Ƹ�class����ӵ����ԣ�
class Student(object):
    __slots__ = ('name', 'age') # ��tuple��������󶨵���������
s = Student()
s.name = 'Michael'
s.age = 25 # ������'age'
#s.score = 99 # ������'score'  �������

#ʹ��__slots__Ҫע�⣬__slots__��������Խ��Ե�ǰ�������ã��Լ̳е������ǲ������õģ�
#������������Ҳ����__slots__����������������������Ծ��������__slots__���ϸ����__slots__��


####################################
#   ʹ��@property  
#   �㷺Ӧ��
####################################
# ��Ҫֱ�ӱ�¶����  ����ṩget set���� �ͺ�javaһ�� �мǣ�
#�ڰ�����ʱ���������ֱ�Ӱ����Ա�¶��ȥ����Ȼд�����ܼ򵥣����ǣ�û�취�����������¿��԰ѳɼ����ġ����Լ�������
class Student2(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int): #������int���ͣ�
            raise ValueError('score must be an integer!')  #�׳��쳣�� ��Ҫ�ķ�����ֱ���׳�ȥ
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#���ǣ�����ĵ��÷��������Ը��ӣ�û��ֱ����������ôֱ�Ӽ򵥡�
#���ǵ�װ������decorator�����Ը�������̬���Ϲ����𣿶�����ķ�����װ����һ�������á�
#  ���� ������@property
#  Python���õ�@propertyװ�������Ǹ����һ������������Ե��õģ�

class Student3(object):
    #  ��һ��getter����������ԣ�ֻ��Ҫ����@property�Ϳ�����   
    @property
    def score(self):  #���־ͽ�score
        return self._score
    # ��ʱ��@property�����ִ�������һ��װ����@score.setter�������һ��setter����������Ը�ֵ
    @score.setter 
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student3()
s.score = 60 
print s.score 
#s.score = 9999  #��setter������Ե���

#�����Զ���ֻ�����ԣ�ֻ����getter������������setter��������һ��ֻ�����ԣ�
class Student4(object):

    @property  
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property  #age��ֻ����
    def age(self):
        return 2014 - self._birth
# @property  �����õ�����д����̵Ĵ��룬ͬʱ��֤�Բ������б�Ҫ�ļ�飬��������������ʱ�ͼ����˳���Ŀ�����

###########################################
# ������   
# �ǳ���Ҫ
# __iter__  __getitem__  __getattr__
###########################################

# 1. __iter__  �����ʱ�˽����
#���һ�����뱻����for ... inѭ��������list��tuple�������ͱ���ʵ��һ��__iter__()�������÷�������һ����������
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # ��ʼ������������a��b

    def __iter__(self):
        return self # ʵ��������ǵ������󣬹ʷ����Լ�

    def next(self):
        self.a, self.b = self.b, self.a + self.b # ������һ��ֵ
        if self.a > 100000: # �˳�ѭ��������
            raise StopIteration();
        return self.a # ������һ��ֵ

for n in Fib():
    print n

# 2. __getitem__  
#Fibʵ����Ȼ��������forѭ������������list�е��񣬵��ǣ���������list��ʹ�û��ǲ��У����磬ȡ��5��Ԫ�أ�
#Ҫ���ֵ���list���������±�ȡ��Ԫ�أ���Ҫʵ��__getitem__()������
class Num():
    def __getitem__(self, n):
        self.xx = (1,34,5,5)
        return self.xx[n]
n = Num()
print n[2]

# 3. __getattr__
# ע���ǰ��ȫ�ַ���getattr()������
# ����������һ�������ڵ����� �ͻᱨ�� ��Student' object has no attribute 'score'����η���û�����Ե�ʱ�򲻱���������һ����
# Ҫ����������󣬳��˿��Լ���һ��score�����⣬Python������һ�����ƣ��Ǿ���дһ��__getattr__()��������̬����һ�����ԡ��޸����£�

class Student5(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):  #ֻҪ�����Ӣ�������ڵ�attr���ʹ��� �� ���������if�ж�
        if attr=='score':
            return 99
        
# ���غ���Ҳ����ȫ���Եģ�
class Student6(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        
# ʵ���Ͽ��԰�һ������������Ժͷ������á�ȫ����̬�������ˣ�����Ҫ�κ������ֶΡ�
# ������ȫ��̬���õ�������ʲôʵ�������أ����þ��ǣ����������ȫ��̬����������á�  

#�ٸ����ӣ�    ��Ҫ��
# REST API
# ���ںܶ���վ����REST API����������΢��������ɶ�ģ�����API��URL���ƣ�     
#         http://api.server/user/friends
#         http://api.server/user/timeline/list
# ���ҪдSDK����ÿ��URL��Ӧ��API��дһ���������ǵ����������ң�APIһ���Ķ���SDKҲҪ�ġ�
# 
# ������ȫ��̬��__getattr__�����ǿ���д��һ����ʽ���ã�

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list


# 3. __call__
# һ������ʵ���������Լ������Ժͷ����������ǵ���ʵ������ʱ��������instance.method()�����á��ܲ���ֱ����ʵ�������ϵ����أ�����instance()����Python�У����ǿ϶��ġ�
# �κ��ֻ࣬��Ҫ����һ��__call__()�������Ϳ���ֱ�Ӷ�ʵ�����е��á��뿴ʾ����
class Student7(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student7('Michael')
s()

#####################################
# �����Ժ�ʵ������
# ��Ҫ python��ʵ�����Ա�����__init__(self) �����ж��壬ֱ�Ӹ���������߶�������Զ�Ĭ����������(������c++��static����)��
#####################################
#�ڱ�д�����ʱ��ǧ��Ҫ��ʵ�����Ժ�������ʹ����ͬ�����֣���Ϊ��ͬ���Ƶ�ʵ�����Խ����ε������ԣ����ǵ���ɾ��ʵ�����Ժ���ʹ����ͬ�����ƣ����ʵ��Ľ��������ԡ�
class Student8(object):
    #self.age = 4 ���������ﶨ�� ���� ������__init__(self)��
    def __init__(self, name):
        self.name = name

s = Student8('Bob')
s.score = 90

class Student9(object):
    name = 'Student'  #������Ĭ�϶���static
s = Student9()
print(s.name) # ��Ҫ�� ��ӡname���ԣ���Ϊʵ����û��name���ԣ����Ի��������class��name���� 
s.name = 'Michael' # ��ʵ����name����
print(s.name) # ����ʵ���������ȼ��������Ըߣ���ˣ�����"����"�����name����       
print(Student9.name) # ���������Բ�δ��ʧ����Student.name��Ȼ���Է���
del s.name # ���ɾ��ʵ����name����
print(s.name) # �ٴε���s.name������ʵ����name����û���ҵ������name���Ծ���ʾ������


##############################################
# ʹ��Ԫ��
##############################################

# 1. type
# ��̬���Ժ;�̬�������Ĳ�ͬ�����Ǻ�������Ķ��壬���Ǳ���ʱ����ģ���������ʱ��̬�����ġ�
# �ȷ�˵����Ҫ����һ��Hello��class����дһ��hello.pyģ�飺
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
#��Python����������helloģ��ʱ���ͻ�����ִ�и�ģ���������䣬ִ�н�����Ƕ�̬������һ��Hello��class����
print(type(Hello)) #Hello��һ��class���������;���type
h = Hello()
print(type(h)) #h��һ��ʵ�����������;���class Hello

#type���ܶ�̬��������  ������ֱ��д��class�ײ�����õ�type��
# ����ͨ��class Hello(object)...�Ķ���
def fn(self, name='world'): # �ȶ��庯��
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # ����Hello class

#type()�������δ���3��������
# class�����ƣ�
# �̳еĸ��༯�ϣ�ע��Python֧�ֶ��ؼ̳У����ֻ��һ�����࣬������tuple�ĵ�Ԫ��д����
# class�ķ��������뺯���󶨣��������ǰѺ���fn�󶨵�������hello�ϡ�    

#ͨ��type()�������������ֱ��дclass����ȫһ���ģ���ΪPython����������class����ʱ��������ɨ��һ��class������﷨��Ȼ�����type()����������class��


# 2. metaclass  �����ò���  ����java��Class��
# ����ʹ��type()��̬���������⣬Ҫ������Ĵ�����Ϊ��������ʹ��metaclass��
# �ȶ���metaclass���Ϳ��Դ����࣬��󴴽�ʵ��  Ԫ������������ĳЩ��ʱ��α�������
# metaclass��Python���������������⣬Ҳ������ʹ�õ�ħ������
# ��������£��㲻��������Ҫʹ��metaclass����������ԣ��������ݿ�����Ҳû��ϵ����Ϊ�������㲻���õ�
