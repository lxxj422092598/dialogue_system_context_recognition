import jieba
import linecache
import random
import re

count = len(open('D:\数据集\IT运维FAQ数据库导出数据\IT运维问题_原本_规则替换分词.txt', 'r', encoding='utf-8').readlines())
count_xhj = len(open('D:\数据集\原数据集\it运维意图识别\小黄鸡_原本.txt', 'r', encoding='utf-8').readlines())

file1 = open(r'D:\数据集\IT运维FAQ数据库导出数据\IT运维问题_原本_规则替换分词.txt', 'r', encoding='utf-8')
file2 = open(r'D:\数据集\原数据集\it运维意图识别\小黄鸡_原本.txt', 'r', encoding='utf-8')
file3 = open(r'D:\数据集\KB_训练集\分词结果\IT运维_小黄鸡_分词.csv', 'a', encoding='utf-8')

for i in range(2000):
    ran = random.randrange(1, count)
    line = linecache.getline(r'D:\数据集\IT运维FAQ数据库导出数据\IT运维问题_原本_规则替换分词.txt', ran)
    file3.write(line.replace('\n', '')+',' + '\n')


pattern1 = re.compile(r'[+—\-—！，。？、~@#￥%……&*（）：;；:¶:,.()!/~*&%^$#@{}"\'“”]+', re.A)
pattern2 = re.compile(r'<.*>|(&nbsp;)', re.A)

for i in range(300):
    ran = random.randrange(1, count_xhj)
    line = linecache.getline(r'D:\数据集\原数据集\it运维意图识别\小黄鸡_原本.txt', ran)
    line = re.sub(pattern1, "", line.replace('\n', '').replace('\t', '').replace(" ", ""))
    strshuzu = jieba.cut(line)
    file3.write(" ".join(strshuzu)+',\n')

