import re


class file_factory(object):
    def __init__(self):
        self.file_list = []
        self.pattern_ner = re.compile(r'\d', re.A)
        self.pattern_space_repeat = re.compile(r'\s+', re.A)

    def get_nerLabel_relation(self, file, ner_file, relation_file, fenci_file):
        for line in file:
            str_word = line.replace('\n', '').split(",")
            print(str_word)
            if(not str_word[1]):break
            ner_list = self.pattern_ner.findall(str_word[0])
            ner_file.write(' '.join(ner_list)+'\n')
            relation_file.write(str_word[1]+'\n')
            str_word[0] = re.sub(self.pattern_ner, '', str_word[0])
            word_list = re.split(self.pattern_space_repeat, str_word[0])
            fenci_file.write(' '.join(word_list)+'\n')

    # 直接获取所有数字标注信息
    def get_ner_label_list(self, line):
        pattern = re.compile(r'\d+')
        return pattern.findall(line)

    def get_relation_label(self, line):
        return line.split(",")[1]


if __name__ == '__main__':
    file_factory = file_factory()
    file_label = open(r'D:\数据集\KB_训练集\分词结果\IT运维_小黄鸡_分词.csv', 'r', encoding='utf-8')
    file_fenci = open(r'D:\数据集\KB_训练集\分词结果\IT运维_fenci.test', 'a', encoding='utf-8')
    file_ner = open(r'D:\数据集\KB_训练集\分词结果\IT运维_ner_y.test', 'a', encoding='utf-8')
    file_relation = open(r'D:\数据集\KB_训练集\分词结果\IT运维_relation_y.test', 'a', encoding='utf-8')
    file_factory.get_nerLabel_relation(file_label, file_ner, file_relation, file_fenci)
    file_label.close()
    file_fenci.close()
    file_ner.close()
    file_relation.close()