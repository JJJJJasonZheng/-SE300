import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import os
from Functions import *
from sklearn.model_selection import train_test_split
import pandas as pd

word_length = 1000
vocab_size = 1000
label_num = 2


#############    get code vector   #############

wordDict = getWordDict()


atrlist = {'\n':1, ' ':1, '{':1, '}':1, '(':1, ')':1, '[':1, ']':1, ';':1, '#':1, ',':1,
          '+':2, '-':2, '*':2, '/':2, '=':2, '>':2, '<':2, '!':2, '^':2, '&':2, '%':2,          
          }

vector_list = []
label = []

path1 = './dataset_new/good'
filenames1 = os.listdir(path1)
for fname1 in filenames1:
    vector = code2Vect(path1 + '/' + fname1, wordDict, atrlist)
    label.append([1, 1])
    vector_list.append(np.array(vector))
    print(path1 + '/' + fname1 + "is over!")

path2 = './dataset_new/trainset_enter_rm'
filenames2 = os.listdir(path2)
for fname2 in filenames2:
    vector = code2Vect(path2 + '/' + fname2, wordDict, atrlist)
    label.append([0, 1])
    vector_list.append(np.array(vector))
    print(path2 + '/' + fname2 + "is over!")

path2 = './dataset_new/trainset_space_rm'
filenames2 = os.listdir(path2)
for fname2 in filenames2:
    vector = code2Vect(path2 + '/' + fname2, wordDict, atrlist)
    label.append([1, 0])
    vector_list.append(np.array(vector))
    print(path2 + '/' + fname2 + "is over!")

path2 = './dataset_new/trainset_random_rm'
filenames2 = os.listdir(path2)
for fname2 in filenames2:
    vector = code2Vect(path2 + '/' + fname2, wordDict, atrlist)
    label.append([0, 0])
    vector_list.append(np.array(vector))
    print(path2 + '/' + fname2 + "is over!")

label = np.array(label)


################################################
data = keras.preprocessing.sequence.pad_sequences(vector_list,
                                                value=wordDict["<PAD>"],
                                                padding='post',
                                                maxlen=word_length)
data = np.array(data)
label = np.array(label).reshape((-1, 2))
pd.DataFrame(label).to_csv("./label_1.csv")
pd.DataFrame(vector_list).to_csv("./vector_list_1.csv")

train_X, test_X, train_Y, test_Y = train_test_split(data,
                                                   label,
                                                   test_size = 0.2)

code = keras.Input(shape=(word_length,), name='code')
embedding = layers.Embedding(vocab_size, 3, name='embedding')(code)
conv = layers.Conv1D(3, 5, padding='same')(embedding)
x = layers.Flatten()(conv)
x = layers.Dropout(0.5)(x)
x = layers.Dense(256, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001))(x)
x = layers.Dropout(0.5)(x)
x = layers.Dense(16, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001))(x)
output = layers.Dense(label_num, activation=tf.nn.sigmoid, kernel_regularizer=keras.regularizers.l2(0.001))(x)

model = keras.Model(inputs=code, outputs=output)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', 'binary_crossentropy'])

model.summary()

history = model.fit(train_X,
                    train_Y,
                    epochs=30,
                    batch_size=64,
                    validation_data=(test_X, test_Y),
                    verbose=1)

def plot_history(histories, key='binary_crossentropy'):
    plt.figure(figsize=(16,10))
    for name, history in histories:
        val = plt.plot(history.epoch, history.history['val_'+key],
            '--', label=name.title()+' Val')
        plt.plot(history.epoch, history.history[key], color=val[0].get_color(),
            label=name.title()+' Train')
    plt.xlabel('Epochs')
    plt.ylabel(key.replace('_',' ').title())
    plt.legend()
    plt.xlim([0,max(history.epoch)])
    plt.show()
    print("showed")



# code = keras.Input(shape=(word_length,), name='code')
# embedding = layers.Embedding(vocab_size, 16)(code)
# conv = layers.Conv1D(16, 5, padding='same')(embedding)
# x = layers.Flatten()(conv)
# x = layers.Dense(256, activation=tf.nn.relu)(x)
# x = layers.Dense(16, activation=tf.nn.relu)(x)
# output = layers.Dense(label_num, activation=tf.nn.sigmoid)(x)

# model = keras.Model(inputs=code, outputs=output)

# model.compile(optimizer='adam',
#               loss='binary_crossentropy',
#               metrics=['accuracy', 'binary_crossentropy'])

# model.summary()

# compare_history = model.fit(train_X,
#                     train_Y,
#                     epochs=30,
#                     batch_size=64,
#                     validation_data=(test_X, test_Y),
#                     verbose=1)

# plot_history([('History', history), ('Overfitting', compare_history)])


test_model = keras.Model(inputs=model.input, outputs=model.get_layer('embedding').output)
embedding_result = test_model.predict([np.linspace(0, word_length-1, word_length)])

"reserve"