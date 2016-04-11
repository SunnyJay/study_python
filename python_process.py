#-*- coding:utf-8 -*-
'''
Created on 2016年4月8日

进程
主要来自廖雪峰
@author: Administrator
'''

##################
# 一、多任务
##################
# 多任务的实现有3种方式：
#     多进程模式；
#     多线程模式；
#     多进程+多线程模式。
# 重要理解！！！！：如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型。对应到Python语言，单进程的异步编程模型称为协程

###################
# 二、多进程
# 
# 在Unix/Linux下，可以使用fork()调用实现多进程。
# 要实现跨平台的多进程，可以使用multiprocessing模块。
#    在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节
#    重要：由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
#        所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
###################

# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
import os
# # pid = os.fork()  #windows没有fork调用！所以提供了multiprocessing
# print 'process (%s) start...' % os.getpid()
# if pid == 0:
#     print 'i am child process(%s) and myparent is %s.' % (os.getpid,os.getppid())
# else:
#      print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

########################
# 三、multiprocessing
#    直接使用或继承
########################
#multiprocessing模块就是跨平台版本的多进程模块
# 创建进程的类：Process([group [, target [, name [, args [, kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。name为别名。group实质上不使用。
# 方法：is_alive()、join([timeout])、run()、start()、terminate()


from multiprocessing import Process #一个Process类来代表一个进程对象
#创建子进程时，只需要传入一个‘执行函数’和‘函数的参数’，创建一个Process实例，用‘start()’方法启动，这样创建进程比fork()还要简单。

from multiprocessing import Process
import multiprocessing

# 子进程要执行的代码
def run_proc(name):
    n = 5
    while n > 0:
        print 'Run child process %s (%s)...' % (name, os.getpid())
        n -= 1

# if __name__=='__main__':  # windows 下 if __name__ == '__main__' 是必须的！ 直接运行会出现RuntimeError why?
#     print 'Parent process %s.' % os.getpid()
#     p = Process(target=run_proc, args=('test',))
#     print 'Process will start.'
#     p.start() 
#     p.join()  # 主进程等待子进程结束后再往下走 避免子进程成为僵尸进程  可加时间参数   省略本行后子进程就成僵尸进程了
#     print 'Process end.'
    
print  '我的电脑核数:',multiprocessing.cpu_count() # 可以得到cpu核数  本机是4核
# 重要，还可以继承自multiprocessing，覆盖run方法


# if __name__ == '__main__':
#     p = ClockProcess(3)
#     p.start()       #进程p调用start()时，自动调用run()   


# 实例化一个Process必须要指定target和args。target是新的进程的入口方法，可以认为是main方法。args是该方法的参数列表。
# 启动进程类似于启动Thread，必须要调用start方法。也可以继承Process，覆盖run方法，在run方法中实现该进程的逻辑。

# 重要：  回顾僵尸进程概念：
#      孤儿进程：一个父进程退出，而它的一个或多个子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作。
# 　　      僵尸进程：一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中。这种进程称之为僵死进程。
#      
#      调用join方法会阻塞当前调用进程，直到被调用进程运行结束。
#      p.join() 会阻塞所在位置的进程，然后等待p完成
#      要等待一个进程完成工作并退出，可以使用join()方法。在Linux上，当某个进程终结之后，需要被(注意被)主进程调用wait，否则进程会成为僵尸进程。
#                所以，有必要对每个Process对象调用join()方法，实际上等同于wait。
# 
# 手工终止一个进程可以调用terminate方法，在UNIX系统中，该方法会发送SIGTERM信号量，而在windows系统中，会借助TerminateProcess方法。
# 需要注意的是，exit处理逻辑并不会被执行，该进程的子进程不会被终止，他们只会变成孤儿进程。




########################
# 四、PooL
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
# 分阻塞和非阻塞两种
########################

from multiprocessing import Pool
import os, time, random
 
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
 
# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()  #Pool的默认大小是CPU的核数  如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
#                 # pool = Pool(processes=4)              # start 4 worker processes 最多同时启动4个进程
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))  #从进程池中取出一个进程执行func，args为func的参数
#     print 'Waiting for all subprocesses done...'
#     p.close() #必须先close,等待任务执行完毕,同时停止接收。 与java中的那个一样
#     p.join() #然后主进程再等待    
#     print 'All subprocesses done.'

#  task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
#  回顾那个模型图：  多个进/线程，一个任务队列，当所有进线程都有任务时，新任务就会在那个队列中等待

# 运行结果
# Parent process 7468.
# Waiting for all subprocesses done...
# Run task 0 (7984)...
# Run task 1 (2296)...
# Run task 2 (11080)...
# Run task 3 (12848)...
# Task 2 runs 0.25 seconds.
# Run task 4 (11080)...  #看 Task 2结束了 task 4才开始
# Task 1 runs 0.47 seconds.
# Task 0 runs 1.02 seconds.
# Task 3 runs 2.89 seconds.
# Task 4 runs 2.81 seconds.
# All subprocesses done.

# pool.join()是用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束。
# 但必pool.join()必须使用在pool.close()或者pool.terminate()之后        
# 其中close()跟terminate()的区别在于close()会等待池中的worker进程执行结束再关闭pool,而terminate()则是直接关闭。
# result.successful()表示整个调用执行的状态，如果还有worker没有执行完，则会抛出AssertionError异常。
# 利用multiprocessing下的Pool可以很方便的同时自动处理几百或者上千个并行操作，脚本的复杂性也大大降低。




##############################
# 五、进程间的通信 
#    进程间通信是通过Queue、Pipes等实现的。
##############################

# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process, Queue
# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue() #创建一个Queue传进去
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    
# pipe
# pipe返回了一对连接对象，代表了管道的两端，每一个对象都有send和recv方法，他们之间是管道，是个双工的管道
# 使用pipe注意Synchronization 问题
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe() #返回一对 一个读一个写， 这里有个作为父 一个作为子
    p = Process(target=f, args=(child_conn,))
    p.start()
    print parent_conn.recv()   # prints "[42, None, 'hello']"
    p.join()