#-*- coding:utf-8 -*-
'''
Created on 2016年4月13日
元类
主要来自廖雪峰
@author: Administrator
'''

##########################################
# metaclass
##########################################

# metaclass，直译为元类，简单的解释就是：
# 
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# 
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
# 
# 我们先看一个简单的例子，这个metaclass可以给我们已经“自定义的MyList“  增加一个add方法：
# 
# 定义ListMetaclass，按照默认习惯，metaclass的“类名”总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类
    
#当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，它指示Python解释器在创建MyList时，
#要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。   
 
# __new__()方法接收到的参数依次是：
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的“一行映射为一个对象”，也就是“一个类对应一个表”，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

##########################################
# ORM
##########################################


# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。
# 虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

class Field(object): #它负责保存数据库表的字段名和字段类型,在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
    
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):  #attrs指的是方法的集合
        if name=='Model':  #排除掉对Model类的修改
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v #添加到映射
        for k in mappings.iterkeys():
            attrs.pop(k) #删除该属性
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs) #动态创建一个类，拥有__table__成员、__mappings__
    
class Model(dict):
    __metaclass__ = ModelMetaclass  #使用Metaclass创建Model

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找__metaclass__，
# 如果没有找到，就继续在父类Model中查找__metaclass__，找到了，就使用Model中定义的__metaclass__的ModelMetaclass来创建User类，
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')  #调用
# 保存到数据库：
u.save()

# 在ModelMetaclass中，一共做了几件事情：
# 排除掉对Model类的修改；
# 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误；
# 把表名保存到__table__中，这里简化为表名默认为类名。
# 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。


