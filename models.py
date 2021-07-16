import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import scipy
## parallel programming to web 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


data = keras.datasets.mnist
(train_images, train_labels), (test_images,test_labels) = data.load_data()

print("Train images", train_images.shape)
print("Train labels", train_labels.shape)
print("test_images", test_images.shape )
print("test labels", test_labels.shape)

