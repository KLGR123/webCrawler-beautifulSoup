from urllib import request
import re, os, sys, io
from bs4 import BeautifulSoup
from time import ctime, sleep
import threading

#在当前目录下创建urls子目录 存储下载HTML文件
os.makedirs('urls', exist_ok=True)

firstUrl = str(input("请输入要爬取的网页url:"))
#构建下载队列 并输入url初始入口
insertUrl = [firstUrl]

#存储已经处理的url
delUrl = []

#负责下载和分析HTML代码的函数 并使其在多个线程中执行
def getUrl():
    while True:
        global insertUrl, delUrl
        try:
            if len(insertUrl) > 0:
                #从对头取出一个url
                html = request.urlopen(insertUrl[0]).read()
                soup = BeautifulSoup(html, 'lxml')

                #find方法找到name值等于title的标签 就是title标签 返回TAG类
                #调用TAG类的get_text()方法返回标签内容 replace()方法把‘\n’替换为空 即不换行
                title = soup.find(name='title').get_text().replace('\n', '')

                #命名文件 并把对应的html页面内容写入
                fp = open("./urls/" + str(title) + ".html", 'w', encoding='utf-8')
                fp.write(str(html.decode('utf-8')))
                fp.close()

                #开始在写入内容中查找所有a标签
                #用类下的findall方法查找 并返回tag类构成的列表
                href_ = soup.find_all(name='a')
                for each in href_:
                    #get方法找到href属性并赋值
                    urlStr = each.get('href')
                    #添加所有以http开头并且没有处理过的URL
                    if str(urlStr)[:4] == 'http' and urlStr not in insertUrl:
                        insertUrl.append(urlStr)
                        print(urlStr) #输出屏幕

                #从队列删除并加入完成队列
                delUrl.append(insertUrl[0])
                del insertUrl[0]
        except:
            #如果报错 就删除处理 加入完成队列 并继续
            delUrl.append(insertUrl[0])
            del insertUrl[0]
            continue

        sleep(1)

#启动三个线程 并运行getUrl函数
threads = []
t1 = threading.Thread(target=getUrl)
threads.append(t1)
t2 = threading.Thread(target=getUrl)
threads.append(t2)
t3 = threading.Thread(target=getUrl)
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()


