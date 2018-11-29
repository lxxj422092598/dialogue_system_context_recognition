# coding:utf-8
import sys
import jieba


class WordToken(object):
    def __init__(self):
        # 最小起始id号, 保留的用于表示特殊标记
        self.START_ID = 1
        self.word2id_dict = {}
        self.id2word_dict = {}


    def load_file_list(self, file_list, min_freq,file2):
        """
        加载样本文件列表，全部切词后统计词频，按词频由高到低排序后顺次编号
        并存到self.word2id_dict和self.id2word_dict中
        """
        words_count = {}
        for file in file_list:
            with open(file, 'r', encoding='utf-8') as file_object:
                for line in file_object.readlines():
                    line = line.strip().replace(" ", "%20%")
                    file2.write(line+' '+'100'+' ityw'+'\n')
                    # print(line)
                    # seg_list = jieba.cut(line)
                    # for str in seg_list:
                    #     if str in words_count:
                    #         words_count[str] = words_count[str] + 1
                    #     else:
                    #         words_count[str] = 1
        #             if line in words_count:
        #                 words_count[line] = words_count[line] + 1
        #             else:
        #                 words_count[line] = 1
        # print(words_count.items())
        # sorted_list = [[v[1], v[0]] for v in words_count.items()]
        # print(sorted_list)
        # sorted_list.sort(reverse=True)
        # for index, item in enumerate(sorted_list):
        #     word = item[1]
        #     if item[0] < min_freq:
        #         self.word2id_dict[word] = self.START_ID + index
        #         self.id2word_dict[self.START_ID + index] = word
        # return index



    #
    # def word2id(self, word):
    #     if not isinstance(word, str):
    #         print("Exception: error word not unicode")
    #         sys.exit(1)
    #     if word in self.word2id_dict:
    #         return self.word2id_dict[word]
    #     else:
    #         return None
    #
    # def id2word(self, aid):
    #     aid = int(aid)
    #     if aid in self.id2word_dict:
    #         return self.id2word_dict[aid]
    #     else:
    #         return None
if __name__ == '__main__':
    wordToken = WordToken()
    file = open(r'D:\数据集\IT运维FAQ数据库导出数据\IT运维词典.dic', 'a', encoding='utf-8')
    wordToken.load_file_list([r'D:\数据集\IT运维FAQ数据库导出数据\驱动补丁及大小等_去除斜杠括号.txt',
                              r'D:\数据集\IT运维FAQ数据库导出数据\分类名_去除斜杠.txt',
                              r'D:\数据集\IT运维FAQ数据库导出数据\电脑方面词汇.txt',
                              r'D:\数据集\IT运维FAQ数据库导出数据\关键词_去掉逗号.txt'], 1, file)
    #
    # file.write(str(wordToken.word2id_dict))
    file.close()