# In[4]:
# 网址来源
# https://github.com/fchollet/keras/blob/master/examples/imdb_lstm.py
from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb
import numpy as np

max_features = 62805
maxlen = 100  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
# (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
# np.savetxt("x_train.txt", x_train)
# np.savetxt("x_test.txt", x_test)
# np.savetxt(" y_train.txt", y_train)
# np.savetxt("y_test.txt", y_test)

# In[2]:


x_train = np.loadtxt(r'D:\资料转移\数据集\it运维意图识别\第三组\向量\x_train_vec.txt', encoding='utf-8').reshape((62805, 100, 1))
y_train = np.loadtxt(r'D:\资料转移\数据集\it运维意图识别\第三组\向量\y_train.txt', encoding='utf-8')
x_test = np.loadtxt(r'D:\资料转移\数据集\it运维意图识别\第三组\向量\x_test_vec.txt', encoding='utf-8').reshape((5731, 100, 1))
y_test = np.loadtxt(r'D:\资料转移\数据集\it运维意图识别\第三组\向量\y_test.txt', encoding='utf-8')

# In[5]:


print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

# In[6]:


print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

# In[10]: 0


print('Build model...')
model = Sequential()
# model.add(Dense(128, input_dim=300))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2, input_shape=(100, 1)))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=10,
          validation_data=(x_test, y_test))

score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)

print('Test score:', score)
print('Test accuracy:', acc)
model.save(r'D:\数据集\it运维意图识别\第三组\my_model.h5')