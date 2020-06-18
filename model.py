# coding: utf-8
# Dogs vs. Cats
#匯入所需函式庫
#%matplotlib inline
from keras.applications.vgg16 import VGG16,preprocess_input, decode_predictions
from keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import wx


# 用來判斷影像的函式
def predict(filename, featuresize):
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(preprocess_input(x))
    results = decode_predictions(preds, top=featuresize)[0]
    return results

# # 用來顯示影像的函式
def showimg(filename, title, i):
    im = Image.open(filename)
    im_list = np.asarray(im)
    plt.subplot(2, 5, i)
    plt.title(title)
    plt.axis("off")
    plt.imshow(im_list)

# 判斷影像


os.environ['KMP_DUPLICATE_LIB_OK']='True'
# 載入完成學習的模型VGG16
model = VGG16(weights='imagenet')
filename = "train/dog.3059.jpg"
results = predict(filename, 1)
for result in results:
    print(result)