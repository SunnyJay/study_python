#-*- coding:gb18030 -*
'''
Created on 2016��4��1��

@author: Administrator
'''
##########################################
#  ��Ԫ����  PyUnit
##########################################
# Ϊ�˱�д��Ԫ���ԣ�������Ҫ����Python�Դ���unittestģ��
# ��д��Ԫ����ʱ��������Ҫ��дһ�������࣬��unittest.TestCase�̳�
import unittest
class Calculate:
    def add(self, a, b):
        return a + b
    def minus(self, a, b):
        return a - b
    
class mytest(unittest.TestCase):
    #��test��ͷ�ķ������ǲ��Է���������test��ͷ�ķ���������Ϊ�ǲ��Է��������Ե�ʱ�򲻻ᱻִ��
    def testAdd(self):
        cal = Calculate()
        sum = cal.add(1,4)
        #��õĶ��Ծ���assertEqual()
        self.assertEqual(sum, 5)
    def testMinus(self):
        cal = Calculate()
        ret = cal.minus(5,4)
        #��õĶ��Ծ���assertEqual()
        self.assertEqual(ret, 1)        
    #�����ڵ�Ԫ�����б�д���������setUp()��tearDown()����
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')
    
if __name__ == '__main__':  # һ����д�õ�Ԫ���ԣ����ǾͿ������е�Ԫ���ԡ���򵥵����з�ʽ����mydict_test.py�����������д��룺
    unittest.main() #д���̶�    

#��һ�ַ�������������ͨ������-m unittestֱ�����е�Ԫ���ԣ�       


####################################
#  doctest �ĵ����� Ҳ�Ǹ���׼ģ��
#################################### 