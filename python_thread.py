#-*- coding:utf-8 -*-  
'''
Created on 2016年4月8日

线程
主要来自廖雪峰
@author: Administrator
'''

#Python的线程是真正的Posix Thread，而不是模拟出来的线程

#########################
#  一、threading 
##########################

# Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：  threading.Thread(target=loop, name='LoopThread')

import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name  #current_thread()函数，它永远返回当前线程的实例  在这里是子线程
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name  #主线程实例的名字叫MainThread

#########################
#  二、Lock 
##########################

#  创建一个锁就是通过threading.Lock()来实现  获取锁lock.acquire() 释放锁lock.release()
#  一定要用try...finally来确保锁一定会被释放

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock() #创建一个锁

def change_it(n):
    # 先存后取，结果应该为0:
    global balance #必须声明全局哦
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        # 放心地改吧
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
            
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance


#########################
#  三、多核CPU 
##########################

# 一个死循环线程会100%占用一个CPU。
# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

import threading, multiprocessing

def loop2():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop2)
    t.start()


#即使启动100个线程，使用率也就170%左右，仍然不到两核。
#但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

############################
# 重要概念！ 
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
# GIL全局解释器锁
############################

# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
#     然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
#     所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# 
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
# 
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

# GIL 的存在导致多线程不能利用多个 CPU 内核的计算能力。好在现在 Python 有了易筋经（multiprocessing）, 吸星大法（C 语言扩展机制）和独孤九剑（ctypes），足以应付多核时代的挑战



############################
# 补充知识 匿名函数 lambda
#############################
# 当我们在"传入"函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。  

#通过对比可以看出，匿名函数lambda x: x * x实际上就是：

def f(x):#参数
    return x * x #返回
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

f = lambda x: x * x
f(3)

#同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


##################################
# ThreadLocal 重要 数据库连接
##################################

# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，
# 因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。

# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦
# 如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
# 这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。
# 有没有更简单的方式？  
# ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，但每个属性如“local_school.student”都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个“dict”，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。