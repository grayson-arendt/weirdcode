import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D

bgColor = '#080404'
titlefont = {'fontname':'Franklin Gothic Medium','color':'#dddddd','weight':'bold','size':'15'}

data_train = pd.read_csv('C:/Users/Grayson/Dropbox/PC/Downloads/train.csv/train.csv')
data_test = pd.read_csv('C:/Users/Grayson/Dropbox/PC/Downloads/test.csv/test.csv')

x_train = data_train.drop(labels=["label"], axis=1)
x_trainNormal = data_train.drop(labels=["label"], axis=1)
y_train = data_train["label"]

x_train = x_train/255.0
x_train = np.array(x_train).reshape(-1,28,28)
x_test = data_test/255.0
x_test = np.array(x_test).reshape(-1,28,28)

train_images = np.expand_dims(x_train, axis=-1)
test_images = np.expand_dims(x_test, axis=-1)

labels = np.array(data_train.label)

train_datagen = ImageDataGenerator(rotation_range=20,
                                  zoom_range=0.1)
train_generator = train_datagen.flow(x=train_images,
                                    y=labels,
                                    batch_size=32)

model = Sequential()

model.add(Conv2D(32,3,activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D())

model.add(Conv2D(64,3,activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D())

model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_generator, epochs=5)

results = model.predict(test_images)

y_pred = [np.argmax(pred) for pred in results]
len(y_pred)

fig, ax = plt.subplots(1, 10, figsize=(12, 9), dpi=120)
plt.setp(ax, xticks=[], yticks=[])

fig.set_facecolor(bgColor)

numbers = []
numbers = random.sample(range(1, 2000), 10)

ax_num=0
for i in numbers:
    ax[ax_num].imshow(x_test[i],cmap='gray')
    ax[ax_num].set_title("{}".format(y_pred[i]),fontdict=titlefont)
    ax_num+=1

plt.show()
