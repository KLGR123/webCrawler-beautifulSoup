import re
import requests
import os

def downloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    x = eval(input('请输入图片数量'))
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        if i > x:
            return

        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        fp = open('download/images/%0.3d.jpg' % i, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    os.makedirs('download/images', exist_ok=True)
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    print(result)
    downloadPic(result.text, word)