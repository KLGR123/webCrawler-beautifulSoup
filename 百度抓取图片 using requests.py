import re
import requests
import os

def downloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    x = eval(input('������ͼƬ����'))
    print('�ҵ��ؼ���:' + keyword + '��ͼƬ�����ڿ�ʼ����ͼƬ...')
    for each in pic_url:
        if i > x:
            return

        print('�������ص�' + str(i) + '��ͼƬ��ͼƬ��ַ:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('�����󡿵�ǰͼƬ�޷�����')
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