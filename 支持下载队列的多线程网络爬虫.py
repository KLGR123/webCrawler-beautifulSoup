from urllib import request
import re, os, sys, io
from bs4 import BeautifulSoup
from time import ctime, sleep
import threading

#�ڵ�ǰĿ¼�´���urls��Ŀ¼ �洢����HTML�ļ�
os.makedirs('urls', exist_ok=True)

firstUrl = str(input("������Ҫ��ȡ����ҳurl:"))
#�������ض��� ������url��ʼ���
insertUrl = [firstUrl]

#�洢�Ѿ������url
delUrl = []

#�������غͷ���HTML����ĺ��� ��ʹ���ڶ���߳���ִ��
def getUrl():
    while True:
        global insertUrl, delUrl
        try:
            if len(insertUrl) > 0:
                #�Ӷ�ͷȡ��һ��url
                html = request.urlopen(insertUrl[0]).read()
                soup = BeautifulSoup(html, 'lxml')

                #find�����ҵ�nameֵ����title�ı�ǩ ����title��ǩ ����TAG��
                #����TAG���get_text()�������ر�ǩ���� replace()�����ѡ�\n���滻Ϊ�� ��������
                title = soup.find(name='title').get_text().replace('\n', '')

                #�����ļ� ���Ѷ�Ӧ��htmlҳ������д��
                fp = open("./urls/" + str(title) + ".html", 'w', encoding='utf-8')
                fp.write(str(html.decode('utf-8')))
                fp.close()

                #��ʼ��д�������в�������a��ǩ
                #�����µ�findall�������� ������tag�๹�ɵ��б�
                href_ = soup.find_all(name='a')
                for each in href_:
                    #get�����ҵ�href���Բ���ֵ
                    urlStr = each.get('href')
                    #���������http��ͷ����û�д������URL
                    if str(urlStr)[:4] == 'http' and urlStr not in insertUrl:
                        insertUrl.append(urlStr)
                        print(urlStr) #�����Ļ

                #�Ӷ���ɾ����������ɶ���
                delUrl.append(insertUrl[0])
                del insertUrl[0]
        except:
            #������� ��ɾ������ ������ɶ��� ������
            delUrl.append(insertUrl[0])
            del insertUrl[0]
            continue

        sleep(1)

#���������߳� ������getUrl����
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


