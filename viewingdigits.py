import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['toolbar'] = 'None'
bgColor = '#08041c'
sns.set_theme(palette="muted")

data_train = pd.read_csv('C:/Users/Grayson/Dropbox/PC/Downloads/train.csv/train.csv')
data_test = pd.read_csv('C:/Users/Grayson/Dropbox/PC/Downloads/test.csv/test.csv')

x_train = data_train.drop(labels=["label"], axis=1)
y_train = data_train["label"]

def get_image_matrix(row, dataset):
    row_values = dataset.iloc[row].values
    image_matrix = row_values.reshape(28, 28)
    return image_matrix

fig, ax = plt.subplots(1, 10, figsize=(12, 9), dpi=120)
plt.setp(ax, xticks=[], yticks=[])

fig.set_facecolor(bgColor)
plt.get_current_fig_manager().canvas.set_window_title('Digits')

numbers = []
numbers = random.sample(range(1, 2000), 10)

ax_num=0
for i in numbers:
    ax[ax_num].imshow(get_image_matrix(i, x_train))
    ax_num+=1

plt.show()
