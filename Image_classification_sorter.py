# https://www.tensorflow.org/tutorials/images/classification


import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

#Load PNGs using image_dataset_from_directory - untility 
#PNG to tf.data.Dataset our folder system

## to png
## then call DataSet

# main_directory/
# ...class_a/
# ......a_image_1.jpg
# ......a_image_2.jpg
# ...class_b/
# ......b_image_1.jpg
# ......b_image_2.jpg
# https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory

# https://www.tensorflow.org/tutorials/load_data/images



## CREATE datasett

batch_size = 32
img_height = 180
img_width = 180