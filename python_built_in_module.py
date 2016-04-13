#-*- coding:utf-8 -*-  
# 开头这个不需要 本身就是UTF-8编码
'''
Created on 2016年4月11日
常用内置模块
主要来自廖雪峰
@author: Administrator
'''

################################
# 一、collections
# 是Python内建的一个集合模块，提供了许多有用的集合类。
################################

# 1.namedtuple  可以定义一个不变的对象 作用：用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
# 

from collections import namedtuple
Point = namedtuple("Point", ['x','y']) #Ponit是一个不变的类型，其具有x y两个属性
p = Point(1, 2)
print p.x, p.y

#Point对象是tuple的一种子类
print isinstance(p, Point)

# 2.deque 重要
#   deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
#   deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('d')
print q
q.pop()
print q

# 3. Counter
#    Counter是一个简单的计数器，其key是字符，可以统计字符出现的个数
#    Counter实际上也是dict的一个子类
# 好东西 先填充进去
from collections import Counter
c = Counter()
for ch in 'programming4':
    c[ch] +=  1 #桶排序的思想
print c
    
# 3. defaultdict 
#    有默认值，并且可以设定 
#    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict。除了默认值，用法和dict完全一样
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')  #设定默认值  注意参数是一个函数对象    
dd['key1'] = 'abc'
print  dd['key1']
print dd['key2']

# 4. OrderedDict  
#    重要！它的顺序是插入的顺序，而不是key本身的顺序 不要搞错了 
#    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  #插入顺序是 a b c
print od

od = OrderedDict([('z', 1), ('x', 2), ('y', 3)])  #插入顺序是 z x y 而不是 x y z 
print od

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key


################################
# 二、hashlib
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。  摘要算法呢？摘要算法又称哈希算法、散列算法
# 不是加密算法：
#     要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
################################

import hashlib
md5 = hashlib.md5()
md5.update('sunnanjun')
print md5.hexdigest()

# md5 128位 记得！
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1() #sha1
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest() # SHA1的结果是160 bit字
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。

# 重要！
# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞，
# 比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。


################################
# 三、itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
################################


################################
# 四、XML

#    XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用。但还是建议你不要用XML，改成JSON。
#    操作XML有两种方法：DOM和SAX。
#                   DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
#                   SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。  正常情况下，优先考虑SAX，因为DOM实在太占内存。
################################

# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了

# 举个例子，当SAX解析器读到一个节点时：
# 会产生3个事件：
#     start_element事件，在读取<a href="/">时；
#     char_data事件，在读取python时；
#     end_element事件，在读取</a>时。

from xml.parsers.expat import ParserCreate
# 把处理的函数赋给paser解析器对应的handler

def start_element(name,attr):
    print name, attr
def end_element(name):
    print name
def char_data(text):
    print text     
    
parser = ParserCreate()
parser.StartElementHandler = start_element  #注册
parser.EndElementHandler = end_element
parser.CharacterDataHandler = char_data

parser.returns_unicode = True #当设置returns_unicode为True时，返回的所有element名称和char_data都是unicode，处理国际化更方便。

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
parser.Parse(xml)

################################
# 五、HTML Parser

# 如果我们要编写一个搜索引擎:第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频内存。
# HTML本质上是XML的子集,但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
################################

from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
        
parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')        
    
################################
# 六、常用的第三方模块

# 基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用easy_install或者pip安装
################################

################################
# 七、图形界面

# Python支持多种图形界面的第三方库：
#   Tk wxWidgets Qt GTK
################################




################################
# 八、urllib

# urllib提供了一系列用于操作URL的功能。
# 3.x的版本urllib与urllib2已经合并为一个urllib库
# Python的urllib和urllib2模块都做与请求URL相关的操作，但他们提供不同的功能。他们两个最显着的差异如下：

# urllib2可以接受一个Request对象，并以此可以来设置一个URL的headers，但是urllib只接收一个URL。这意味着，你不能伪装你的用户代理字符串等。
# urllib模块可以提供进行urlencode的方法，该方法用于GET查询字符串的生成，urllib2的不具有这样的功能。这就是urllib与urllib2经常在一起使用的原因。
################################

import urllib2
 
# （1）最简单的应用 （request是默认的）
url = r'http://www.baidu.com'
html = urllib2.urlopen(url).read(100)  #可指定读取大小
print html

   # urllib2.urlopen(url[, data][, timeout])
   # urlopen方法是urllib2模块最常用也最简单的方法，它打开URL网址，url参数可以是一个字符串url或者是一个Request对象


# （2）urllib2提供了request的类，可以让用户在发送请求前先构造一个request的对象，然后通过urllib2.urlopen方法来发送请求
# 自定义request对象  发送Get请求
import urllib2
url = r'http://www.baidu.com'
req = urllib2.Request(url) #当然你还可以更改其他request属性 如header data, 但url是必须的
html = urllib2.urlopen(req).read(100)
print html

    # class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
    # data:    重要！！！当请求含有data参数时，HTTP的请求为POST，而不是GET。
    #          数据应该是缓存在一个标准的application/x-www-form-urlencoded格式中。urllib.urlencode()函数用映射或2元组，返回一个这种格式的字符串。如post表单的内容
    # header: 
    
# （3）自定义数据
import urllib 
import urllib2  
  
url = 'http://www.baidu.com/' 
values = {'name' : 'Michael Foord', 'location' : 'Northampton','language' : 'Python' }   
data = urllib.urlencode(values)  #将你要发的数据编码成标准格式的字符串，才能发出去 只有urllib有这个方法 。
req = urllib2.Request(url,data)  
response = urllib2.urlopen(req)  
the_page = response.read(100)
print the_page

# （4）如何构造get请求呢？自定义url呀
import urllib 
import urllib2  
  
url = 'http://www.baidu.com/s'    #https://www.baidu.com/s?wd=查询关键字 
values = {'wd':'杨彦星'}   
data = urllib.urlencode(values)
print data 
url2 = url+'?'+data # 说明不管post还是get,数据的格式都是一样的，只不过一个在请求里，一个在url里
response = urllib2.urlopen(url2)  
the_page = response.read(100)
 
print the_page


# （5）header
# headers——是字典类型，头字典可以作为参数在request时直接传入，也可以把每个键和值作为参数调用add_header()方法来添加。
# 制造post请求
import urllib
import urllib2
url = 'http://10.1.1.71:5000/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username' : 'admin',  'password' : 'default' }    # 少写一个就错了 因为网页服务端要解析这两个参数，结果没提供，就出错

headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(req,timeout=10)
the_page = response.read()
#print the_page


# (6)cookie

# 当你获取一个 URL 你使用一个 opener(一个 urllib2.OpenerDirector 的实例)。在前面，我们都是使用的默认的 opener，也就是 urlopen。
# 它是一个特殊的 opener，可以理解成opener 的一个特殊实例，传入的参数仅仅是 url，data，timeout。
# 如果我们需要用到 Cookie，只用这个 opener 是不能达到目的的，所以我们需要创建更一般的opener 来实现对 Cookie 的设置。

# 1.先创建cookie对象（该模块主要的对象有 CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。）
# 2.再创建cookie处理器
# 3.再用处理器创建一个新的opener build_opener

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie)) #build_opener
postdata = urllib.urlencode({
           'username' : 'admin',  'password' : 'default'
        })
#登录教务系统的URL
loginUrl = 'http://10.1.1.71:5000/login'

#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)   #除了这种方式，还可以使用install_opener配合urlopen 如下面：

#urllib2.install_opener(opener)  #两种方式都可以 但是不建议使用这种
#result = urllib2.urlopen(loginUrl,postdata)

#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)

#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://10.1.1.71:5000/login'
#请求访问成绩查询网址
result = opener.open(gradeUrl) #自动使用cookie
print result.read()  






import urllib2
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code,e.reason
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"  


# （7）反盗链
# 某些站点有所谓的反盗链设置，其实说穿了很简单，
# 就是检查你发送请求的header里面，referer站点是不是他自己

headers = { 'User-Agent' : user_agent,'Referer':'http://www.cnbeta.com/articles' }

