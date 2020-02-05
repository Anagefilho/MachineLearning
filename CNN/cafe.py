# Imports
import tensorflow as tf
import keras as K

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
# Inicializando a Rede Neural Convolucional
classifier = Sequential()

# Passo 1 - Primeira Camada de Convolucao
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Passo 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adicionando a Segunda Camada de Convolucao
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
# Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Passo 3 - Flattening
classifier.add(Flatten())

# Passo 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compilando a rede
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

validation_datagen = ImageDataGenerator(rescale = 1./255)

# Pre-processamento das imagens de treino e validacao
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (16, 16),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

validation_set = validation_datagen.flow_from_directory('dataset/test_set',
                                                        target_size = (16, 16),
                                                        batch_size = 32,
                                                        class_mode = 'binary')

# Executando o treinamento (esse processo pode levar bastante tempo, dependendo do seu computador)
classifier.fit_generator(training_set,
                         steps_per_epoch = 100,
                         epochs = 5,
                         validation_data = validation_set,
                         validation_steps = 400)

import numpy as np
from keras.preprocessing import image

# Testando o algoritmo
acc = []
test_samples = [12,10]
for size in test_samples:
    for i in range(size):
        test_image = image.load_img('dataset/test_set/cereja/c'+str(i+1)+'.jpeg', target_size = (16, 16))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = classifier.predict(test_image)
        training_set.class_indices

        if result[0][0] == 1:
            acc.append(1)
        else:
            acc.append(0)

gtruth = np.append(np.ones(12),np.zeros(0)).astype(int)
print np.mean(np.asarray(acc) == gtruth)
