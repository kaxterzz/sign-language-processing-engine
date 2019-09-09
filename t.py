from __future__ import absolute_import, division, print_function, unicode_literals
import pandas as pd 
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = pd.read_csv('sources/sign-language-mnist/sign-mnist-train.csv')

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
