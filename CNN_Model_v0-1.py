
# # Import



import os
import sys
sys.path.append('/home/calanin/.local/lib/python3.6/site-packages')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



os.chdir('/media/calanin/Second HDD/Data_science/Personal_projects/Tinder/captured_pics')



from keras.applications import VGG16
from keras import layers
from keras import models
from keras import optimizers

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


# # Create input generator


train_dir = os.path.join(os.getcwd(),'train')

val_dir = os.path.join(os.getcwd(),'val')

test_dir = os.path.join(os.getcwd(),'test')


from keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)



train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode = 'binary'
)

val_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),
    batch_size=15,
    class_mode = 'binary'
)



for data_batch, labels_batch in train_generator:
    print('data batch shape:' , data_batch.shape)
    print('labels batch shape:', labels_batch.shape)
    break


# # Modeling

# ## Load Pre-train 

conv_base = VGG16(weights = 'imagenet',
                      include_top = False,
                      input_shape = (150,150,3))


conv_base.summary()


# ## Build layer on top 

model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))

model.summary()

model.compile(loss = 'binary_crossentropy',
             optimizer=optimizers.RMSprop(lr=1e-4),
             metrics=['acc'])


# ## Train 

history = model.fit_generator(
    train_generator,
    steps_per_epoch=3,
    epochs = 30,
    validation_data=val_generator,
    validation_steps=2
)


model.save('tinder_beta_model_v-0-2.h5')


acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1 , len(acc) + 1)

plt.plot(epochs, acc, 'bo' , label='Training acc')
plt.plot(epochs, val_acc, 'b' , label='validation acc', c ='r')
plt.title('Training and validation accuracy')
plt.legend()


plt.plot(epochs, loss, 'bo' , label='Training loss')
plt.plot(epochs, val_loss, 'b' , label='validation loss', c='r')
plt.title('Training and validation loss')
plt.legend()

plt.figure()




