import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import scipy

## Class values for Ground truth

## 1 for NCR 
#  2 for ED
## 4 for ET 
## 0 for everyother values

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# https://www.tensorflow.org/tutorials/images/segmentation

data = keras.datasets.mnist
(train_images, train_labels), (test_images,test_labels) = data.load_data()

## Seeding 
seed = 124123
random.seed = seed
np.random.seed = seed
tf.seed = seed

#### 
## We will call data_generator class here


## 80% ## 20%
## classify values
# pixels edges considered as discontinuous local features of images

print("Train images", train_images.shape)
print("Train labels", train_labels.shape)
print("test_images", test_images.shape )
print("test labels", test_labels.shape)

######### We need a data splits


## Load split datasets 
train = dataset['train'].map(load_image_train, num_parallel_calls=tf.data.AUTOTUNE)
test = dataset['test'].map(load_image_test)

# WHat do these do?
train_dataset = train.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()
train_dataset = train_dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
test_dataset = test.batch(BATCH_SIZE)

## U-net is encoder (downsampler)
## We need to train the encoder 
## U-net decoder upsamplers)
## we need to train the decoder
OUTPUT_CHANNELS = 3
## Model call
model = UNet()
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])
model.summary()

## Train model
train_gen = DataGen(train_ids, train_path, image_size=image_size, batch_size=batch_size)
valid_gen = DataGen(valid_ids, train_path, image_size=image_size, batch_size=batch_size)

train_steps = len(train_ids)//batch_size
valid_steps = len(valid_ids)//batch_size

model.fit_generator(train_gen, validation_data=valid_gen, steps_per_epoch=train_steps, validation_steps=valid_steps, 
                    epochs=epochs)

## Somehow save results and assement call