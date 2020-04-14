# webCrawler-beautifulSoup说明

## 一、百度图片的抓取（using requests）
### 0.引用函数库

re:正则表达式实现url指定内容抓取、图片命名
requests：get方法获取url 与网页端相连
os：操作系统 存储指定量图片到位置

### 1.函数实现原理




## 二、利用HTML分析库Beautiful Soup
  抓取到JSON、XML数据后，需要进行分析。
  HTML相比而言更繁琐，如何分析？一是正则，二是Beautiful Soup.
  BS可以做到把HTML转换为*对象树*。
  
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

