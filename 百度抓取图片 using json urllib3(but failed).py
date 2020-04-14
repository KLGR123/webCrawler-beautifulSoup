from urllib3 import *
import os
import re
import json

http = PoolManager()
disable_warnings()

os.makedirs('download/images', exist_ok=True)#���������洢ͼƬ����Ŀ¼

#��image_headers.txt�ļ���ȡhttp����ͷ�������ֵ�
def str2Headers(file):
    headerDict = {}
    f = open(file, 'r')
    headerText = f.read()

    #windows��\n��Ϊ���з����ָ�ÿһ�д���headers�б�
    headers = re.split('\n', headerText)

    #��ÿ��HTTP����ͷ�����ֵ�
    for header in headers:
        result = re.split(":", header, maxsplit=1)#���ָ�һ��
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict

#��HTTP����ͷת��Ϊ�ֵ����
Headers = str2Headers('image_headers.txt')

#����ÿһ��ץȡ����JSON�ĵ�
def processResponse(response):
    global count
    if count > 20:
        return
    s = response.data.decode('utf-8')

    #�����ص�JSON�ı�ת��ΪJSON����
    d = json.loads(s)
    n = len(d['data'])
    for i in range(n-1):
        if count > 20:
            return

        #��ȡͼ��url
        imageUrl = d['data'][i]['hoverURL'].strip()
        if imageUrl != '':
            print(imageUrl)
            r = http.request('GET', imageUrl, headers=Headers)
            count += 1
            print(r.data)
            #��ͼƬ���������أ��ļ�������ʱ��λ������ǰ��0
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







