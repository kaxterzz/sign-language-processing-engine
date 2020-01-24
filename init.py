import numpy as np 
import pandas as pd 
import cv2
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
import keras 
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from sklearn.metrics import accuracy_score
from keras.models import load_model
from keras.preprocessing import image

try:
    # train = pd.read_csv('sources/sign-language-mnist/sign-mnist-train.csv')
    test = pd.read_csv('sources/sign-language-mnist/sign-mnist-test.csv')

    # print(train.head())

    # print(train.shape)

    # #Image('sources/sign-language-mnist/american_sign_language.PNG')

    # labels = train['label'].values

    # unique_val = np.array(labels)
    # np.unique(unique_val)

    # print(plt.figure(figsize = (18,8)))

    # print(sns.countplot(x = labels))

    # train.drop('label', axis = 1, inplace = True)

    images = train.values
    images = np.array([np.reshape(i, (28,28)) for i in images])
    images = np.array([i.flatten() for i in images])

    # label_binrizer = LabelBinarizer()
    # labels = label_binrizer.fit_transform(labels)

    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size = 0.3, random_state = 101)

    # batch_size = 128
    # num_classes = 24
    # epochs = 50

    # x_train = x_train / 255
    # x_test = x_test /255

    # x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    # x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

    # plt.imshow(x_train[0].reshape(28,28))

   

    # model = Sequential()
    # model.add(Conv2D(64, kernel_size=(3,3), activation = 'relu', input_shape=(28, 28 ,1) ))
    # model.add(MaxPooling2D(pool_size = (2, 2)))

    # model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
    # model.add(MaxPooling2D(pool_size = (2, 2)))

    # model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
    # model.add(MaxPooling2D(pool_size = (2, 2)))

    # model.add(Flatten())
    # model.add(Dense(128, activation = 'relu'))
    # model.add(Dropout(0.20))
    # model.add(Dense(num_classes, activation = 'softmax'))

    # model.compile(loss = keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

    # history = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs=epochs, batch_size=batch_size)

    # plt.plot(history.history['acc'])
    # plt.plot(history.history['val_acc'])
    # plt.title("Accuracy")
    # plt.xlabel('epoch')
    # plt.ylabel('accuracy')
    # plt.legend(['train','test'])
    # plt.show()

    # model.save("testmodel_ofz.h5")

    # test_images = test.values
    # test_images = np.array([np.reshape(i, (28, 28)) for i in test_images])
    # test_images = np.array([i.flatten() for i in test_images])

    # test_labels = label_binrizer.fit_transform(test_labels)
    # test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
    # test_images.shape
    # y_pred = model.predict(test_images)
    # print(accuracy_score(test_labels, y_pred.round()))

    model = load_model("testmodel.h5")

    test_image = image.load_img('sources/images/a.png',color_mode="grayscale",target_size=(28,28))

    print(test_image.format)
    print(test_image.mode)
    print(test_image.size)

    test_image = image.img_to_array(test_image)

    print(test_image.dtype)
    print(test_image.shape)

    test_image = test_image.reshape(28,28)

    test_labels = test['label']
    test.drop('label', axis = 1, inplace = True)
    
    #result = model.predict(test_image)
    result = model.predict(X_train.reshape(1,28,28,3))

    print(result)



except Exception as e:
    print(e)




