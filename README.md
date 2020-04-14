# webCrawler-beautifulSoup小白入门 
written by KLGR01

## 一、百度图片的抓取（using requests）
### 0.引用函数库

re:正则表达式实现url指定内容抓取、图片命名
requests：get方法获取url 与网页端相连
os：操作系统 存储指定量图片到位置

### 1.函数实现原理




## 二、利用HTML分析库Beautiful Soup
  抓取到JSON、XML数据后，需要进行分析。
  HTML相比而言更繁琐，如何分析？一是正则，二是Beautiful Soup.
  BS可以做到把HTML转换为*对象树*（所谓对象.对象… 结合后面代码有感受）。
  
  ### 1.pip install beautifulsoup4 之后，了解一下BS4
  bs4的核心类BeautifulSoup.其第一个参数指定要分析的HTML代码；第二个参数表示HTML分析引擎。
     
  - html分析引擎的类型
  - html.parser：python内置标准库 
  - lxml：需安装C语言库 pip 
  - html5lib：以浏览器方式解析，很强 pip
     
  *代码跑一下作为三种引擎的测试*

```
from bs4 import BeautifulSoup
#实例化核心类，并指定为html.parser引擎
soup1 = BeautifulSoup('<title>html.parser test </title>', 'html.parser')

#获取title标签
print(soup1.title)

#获取title里面的文本内容
print(soup1.title.text)

#实例化核心类，并指定为lxml引擎
soup2 = BeautifulSoup('<title>lxml test </title>', 'lxml')
print(soup2.title.text)

html = '''
<html>
    <head><title>html5lib test </title></head>
    <body>
        <a href="a.html">first page</a>
        <p>
        <a href="b.html">second page</a>
        <p>
        <a href="c.html">third page</a>
        <p>
    </body>
</html>
'''

#使用html5lib测试一下
soup3 = BeautifulSoup(html, 'html5lib')
print(soup3.title.text)

#获取第一个a标签的href属性值，比正则舒服多了
print(soup3.a['href'])
```

 ### 2.学习一下Tag对象和通过该对象获取name和string属性
  首先我们用BeautifulSoup对象装载HTML代码。
  HTML代码中的元素会被转变为Tag对象（自定义的也可以），Tag对象的两个属性如下。
  
  - name：获取标签名
  - string / text：获取标签内文本
     
  如下代码中，*soup就是BS对象，soup.a就是一个Tag对象 BS对象.Tag对象.属性*
  ```
  from bs4 import BeautifulSoup

html = '''
<html>
    <head><title>index</title></head>
    <body>
        <a href="a.html">first page</a>
        <p>
        <a href="b.html">second page</a>
        <p>
        <a href="c.html">third page</a>
        <p>
        <x k='klgr01'>hello BS</x>
    </body>
</html>
'''
#创建BS对象并实例化，用lxml引擎
soup = BeautifulSoup(html, 'lxml')

print(soup.a)

#获取body标签中的第一个a标签
print(soup.body.a)

print(soup.a.text)#text获取标签内文本

#设置节点名称
#比如我将第一个a标签改为div标签, 通过name属性获取标签名
soup.a.name = 'div'

print(soup.x)
#获取到我们自定义的x类型标签的文本, string属性获取和设置标签文本
print(soup.x.string)
soup.x.string = 'klgr is the king'
print(soup.x)
print(soup.x.string)

  ```

### 3.疯狂读写标签属性
  节点的属性值就是比如href class attr div等等后面的值。
  一般节点的属性类型有两类。
  - 字符串：如href后面的url
  - 列表：如class属性等*多值属性 
  
  相应地，对二者的操作也与python中对字符串和列表的操作相对应，详见代码。
   ```
   html = '''
<html>
    <head><title>index</title></head>
    <body attr='test1 test2' class='style1 style2'>
        <a href="a.html" rel='ok1 ok2 ok3' class='a1 a2'>first page</a>
        <p>
        <a href="b.html">second page</a>
        <p>
        <a href="c.html">third page</a>
        <p>
        <x k='klgr01' attr1='i love bs' attr2='i love py'>hello BS</x>
    </body>
</html>
'''

from bs4 import *

soup = BeautifulSoup(html, 'lxml')
#获取soup对象的body这个Tag对象的attrs属性的类型 --Dict（字典）
print(type(soup.body.attrs))#attr s 细节

#soup.body['class']返回列表 即class属性值对应的多标签列表
#BS.TAG['属性名'] = [ , , ]
print('body.class', '=', soup.body['class'])

print('body.attr', '=', soup.body['attr']) #返回字符串

print('a.class', '=', soup.body.a['class']) #返回列表

#设置x标签的attr1属性（列表类型）
soup.x['attr1'] = 'klgr changed attr1'
print('x.attr1', '=', soup.x['attr1'])

#设置body标签的class属性值（列表类型）
soup.body['class'] = ['x', 'y', 'z']
#为body标签的class添加一个属性值
soup.body['class'].append('m')
print(soup.body['class'])

#列表的方法随便用 用pop来pop一下
soup.body['class'].pop(3)
print(soup.body['class'])

print(soup.a['rel'])
   ```
   
 有两点需要额外注意：
 - 列表类型的属性是系统内定的。比如说，你可以自定义一个属性并且用多个空格分隔，但是BS类仍然认为它是字符串类的属性。
 - HTML支持的列表属性一共有这些
    - rel
    - class
    - rev
    - accept-charset
    - headers
    - accesskey
    

