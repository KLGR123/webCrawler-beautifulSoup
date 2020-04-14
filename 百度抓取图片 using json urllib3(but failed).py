from urllib3 import *
import os
import re
import json

http = PoolManager()
disable_warnings()

os.makedirs('download/images', exist_ok=True)#建立用来存储图片的子目录

#从image_headers.txt文件读取http请求头，返回字典
def str2Headers(file):
    headerDict = {}
    f = open(file, 'r')
    headerText = f.read()

    #windows用\n作为换行符，分隔每一行存入headers列表
    headers = re.split('\n', headerText)

    #把每个HTTP请求头加入字典
    for header in headers:
        result = re.split(":", header, maxsplit=1)#最多分割一次
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict

#将HTTP请求头转化为字典对象
Headers = str2Headers('image_headers.txt')

#处理每一个抓取到的JSON文档
def processResponse(response):
    global count
    if count > 20:
        return
    s = response.data.decode('utf-8')

    #将下载的JSON文本转化为JSON对象
    d = json.loads(s)
    n = len(d['data'])
    for i in range(n-1):
        if count > 20:
            return

        #获取图像url
        imageUrl = d['data'][i]['hoverURL'].strip()
        if imageUrl != '':
            print(imageUrl)
            r = http.request('GET', imageUrl, headers=Headers)
            count += 1
            print(r.data)
            #将图片保存至本地，文件名命名时三位，不足前补0
            imageFile = open('download/images/%0.3d.jpg' % count, 'wb')
            imageFile.write(r.data)
            imageFile.close()

count = 0
pn = 30
rn = 30

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct' \
      '=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%9B%BD%E9%98%9F%E9%95' \
      '%BF&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=' \
      '&copyright=&word=%E7%BE%8E%E5%9B%BD%E9%98%9F%E9%95%BF&s=&se=&tab=&' \
      'width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={pn}' \
      '&rn={rn}&gsm=1e&1586783397999='.format(pn=pn, rn=rn)

while count <= 20:
    r = http.request('GET', url)
    processResponse(r)
    pn += 30







