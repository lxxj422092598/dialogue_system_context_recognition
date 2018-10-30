import jieba
import jieba.posseg as pseg
import re

# jieba.load_userdict(r'D:\数据集\IT运维FAQ数据库导出数据\IT运维词典.dic')
# jieba.load_userdict(r'D:\数据集\IT运维FAQ数据库导出数据\computer.dic')

# line = 'M7020/M7030WINXP系统下载驱动安装方法'
# file1 = open(r'D:\数据集\IT运维FAQ数据库导出数据\问题-关键词-描述-类型.txt', 'r', encoding='utf-8')
file2 = open(r'D:\数据集\knowledge_graph\printerDeviceDriver-utf8.csv', 'r', encoding='utf-8')
file3 = open(r'D:\数据集\knowledge_graph\printerDriver_install&uninstall_windows-utf8.csv', 'a', encoding='utf-8')
# dayinji = []
#
# for line in file1:
#     if "打印机" in line:
#         words = pseg.cut(line)
#         for w in words:
#             if w.word not in dayinji and re.findall('[a-zA-Z0-9]', w.word):
#                 dayinji.append(w.word)


# for i in dayinji:
#     file2.write(','+i+', '+'\n')
file3.write("from_id,安装方法,卸载方法,to_id"+'\n')
# n = 338
# m = 135
# for i in range(202):
#     file3.write(str(n)+','+str(m)+'\n')
#     n = n+1
#     m = m+1
n = 96
for line in file2:
    if line.split(",")[0].isdigit():
        for i in range(96, 108):
            file3.write(line.split(',')[0]+', , ,'+str(i)+'\n')

# for i in range(135,177):
#     file3.write(str(i)+', ,5'+'\n')
# for i in range(177, 337):
#     file3.write(str(i)+', ,22'+'\n')

file2.close()
file3.close()