# -*- coding: utf-8 -*-
"""model from scratch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GRJ_IA0z6b-u0CY_7SIW2nF0FgSzuK5S
"""

! pip install numpy

from google.colab import drive

"""convolution block  from scratch"""

import numpy as np
from numpy import asarray
import cv2
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image  
# image.ImageDataGenerator()
# image.load_img()

drive.mount('/content/drive')

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential

model = Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(layers.Dense(64, activation='relu'))
# Add another:
model.add(layers.Dense(64, activation='relu'))
# Add an output layer with 10 output units:
model.add(layers.Dense(10))

