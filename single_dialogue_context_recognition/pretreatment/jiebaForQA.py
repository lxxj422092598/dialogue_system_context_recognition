import jieba


f1 = open(r'D:\数据集\test.txt', 'a', encoding='utf-8')
f = open(r'D:\数据集\wiki_zh_分行.txt', 'r', encoding='utf-8')
for line in f:
    f1.write(" ".join(jieba.cut(line)))
f.close()
f1.close()
