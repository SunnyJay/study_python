#-*- coding:utf-8 -*-  
'''
Created on 2016年4月1日

@author: Administrator
'''
##########################################
#  单元测试  PyUnit
##########################################
# 为了编写单元测试，我们需要引入Python自带的unittest模块
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
import unittest
class Calculate:
    def add(self, a, b):
        return a + b
    def minus(self, a, b):
        return a - b
    
class mytest(unittest.TestCase):
    #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    def testAdd(self):
        cal = Calculate()
        sum = cal.add(1,4)
        #最常用的断言就是assertEqual()
        self.assertEqual(sum, 5)
    def testMinus(self):
        cal = Calculate()
        ret = cal.minus(5,4)
        #最常用的断言就是assertEqual()
        self.assertEqual(ret, 1)        
    #可以在单元测试中编写两个特殊的setUp()和tearDown()方法
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')
    
if __name__ == '__main__':  # 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
    unittest.main() #写法固定    

#另一种方法是在命令行通过参数-m unittest直接运行单元测试：       


####################################
#  doctest 文档测试 也是个标准模块
#################################### 