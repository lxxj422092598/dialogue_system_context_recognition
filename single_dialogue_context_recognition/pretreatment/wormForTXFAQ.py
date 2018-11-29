from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def scrapeFAQ(address, file):
    html = urlopen(address).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    while True:
        all_q_href = soup.find_all('a', {"class": "xst", "href": re.compile(".*")})
        for l in all_q_href:
            print(l.get_text() + ' ' + l["href"])
            recordFAQ(l["href"], file, l.get_text())
        nxt_href = soup.find_all('a', {"class": "nxt", "href": re.compile(".*")})
        if len(nxt_href) != 0:
            html = urlopen("http://bbs.guanjia.qq.com/" + nxt_href[0]['href']).read().decode('utf-8')
            soup = BeautifulSoup(html, features='lxml')
        else:
            break


def recordFAQ(href, file, qname):
    file.write(qname + "\n")
    html = urlopen("http://bbs.guanjia.qq.com/"+href).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    answers = soup.find_all('td', {"class": 't_f'})
    for answer in answers:
        qcontent1 = answer.get_text().replace("下载附件", "").replace("上传", "").replace("\n", "")

        file.write(qcontent1)
    file.write("\n" + "\n")


f = open(r'D:\数据集\腾讯管家电脑故障FAQ.txt',  'a', encoding='utf-8')
scrapeFAQ("http://bbs.guanjia.qq.com/forum-125-1.html", f)
f.close()
# if has Chinese, apply decode()
# html = urlopen("http://bbs.guanjia.qq.com/forum-125-1.html").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
# print(soup.h1)
# print('\n', soup.p)

# all_href = soup.find_all('a', {"class": "xst", "href": re.compile(".*")})
# for l in all_href:
#     print(l.get_text())
# print

