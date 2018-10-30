# f = open(r'D:\数据集\it运维意图识别\x_train.txt', 'r', encoding='utf-8')
# f = open(r'D:\数据集\it运维意图识别\x_test.txt', 'r', encoding='utf-8')
# # for i in range(203):
# #     f.write("0\n")
# # count = len(open(r'D:\数据集\it运维意图识别\x_test.txt', 'r').readlines())
# # print(count)
# # for line in f:
#     # num = num + 1
#     #strings = line.split("|||")
#     #print(strings[0].strip(), strings[1].strip(), strings[2].strip().replace("\n", ""))
# for line in f:
#     print(line) # <do something with line>
# print(num)
# f.close()
import jieba
import random
import wordToken
import json


wordToken = wordToken.WordToken()
# 输入序列长度
input_seq_len = 5
# 输出序列长度
output_seq_len = 5
# 空值填充0
PAD_ID = 0
# 输出序列起始标记
GO_ID = 1
# 结尾标记
EOS_ID = 2
# 在样本中出现频率超过这个值才会进入词表
min_freq = 1

# 放在全局的位置，为了动态算出num_encoder_symbols和num_decoder_symbols
max_token_id = wordToken.load_file_list([r'D:\资料转移\数据集\it运维意图识别\IT运维问题_原本.txt', r'D:\资料转移\数据集\it运维意图识别\小黄鸡_原本.txt'], min_freq)
num_encoder_symbols = max_token_id + 5
num_decoder_symbols = max_token_id + 5

fileobject = open(r'D:\数据集\IT_小黄鸡_onehot.json', 'w', encoding='utf-8')
# print(wordToken.word2id_dict)
jsObj = json.dumps(wordToken.word2id_dict,ensure_ascii=False)
print(jsObj)
fileobject.write(jsObj)
fileobject.close()

#
# def get_id_list_from(sentence):
#     sentence_id_list = []
#     seg_list = jieba.cut(sentence)
#     for str1 in seg_list:
#         aid = wordToken.word2id(str1)
#         if aid:
#             sentence_id_list.append(wordToken.word2id(str1))
#     return sentence_id_list
#
#
# fx_train = open(r'D:\数据集\it运维意图识别\第三组\x_train.txt', 'r', encoding='utf-8')
# fx_test = open(r'D:\数据  集\it运维意图识别\第三组\x_test.txt', 'r', encoding='utf-8')
# fx_train_vec = open(r'D:\数据集\it运维意图识别\第三组\向量\x_train_vec.txt', 'a', encoding='utf-8')
# fx_test_vec = open(r'D:\数据集\it运维意图识别\第三组\向量\x_test_vec.txt', 'a', encoding='utf-8')
#
# for line in fx_train:
#     fx_train_vec.write(repr(get_id_list_from(line)) + "\n")
#
#
# for line in fx_test:
#     fx_test_vec.write(repr(get_id_list_from(line)) + "\n")
#
#
# fx_train.close()
# fx_test.close()
# fx_train_vec.close()
# fx_test_vec.close()
