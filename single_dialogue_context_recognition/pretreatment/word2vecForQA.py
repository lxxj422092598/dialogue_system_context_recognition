from gensim.models import word2vec
import logging


logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(r'D:\数据集\wiki_IT_xgj_fenci.txt')
model = word2vec.Word2Vec(sentences, size=200)

model.save(r"D:\数据集\百科_运维_小黄鸡.model")
# model.similarity(u"好", u"还行")
