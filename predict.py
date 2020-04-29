# import socketio
import argparse
from keras.models import load_model
from keras.preprocessing import image

# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--filename", required=True,
#                 help="file name")
# args = vars(ap.parse_args())

# file_name = args["filename"]

# standard Python
# sio = socketio.Client()
# sio.connect('http://139.59.37.180:3770')


def predict(file_name):
    try:
        result = ''
        model = load_model("testmodel3.h5")

        test_image = image.load_img(file_name,color_mode="grayscale",target_size=(28,28,1))
        #print(test_image.format)
        #print(test_image.mode)
        #print(test_image.size)

        test_image = image.img_to_array(test_image)
        test_image = test_image.reshape((-1,) + test_image.shape)

        #print(test_image.dtype)
        #print(test_image.shape)

        y_pred = model.predict_classes(test_image)
        #print(y_pred)
        prediction = y_pred[0]
        classname = y_pred[0]
        print("Class: ",classname)
        print(y_pred)
        if(classname == 0):
            print('Result --> A')
            result = 'A'
        elif(classname == 1):
            print('Result --> B')
            result = 'B'
        elif(classname == 2):
            print('Result --> C')
            result = 'C'
        elif(classname == 3):
            print('Result --> D')
            result = 'D'
        elif(classname == 4):
            print('Result --> E')
            result = 'E'
        elif(classname == 5):
            print('Result --> F')
            result = 'F'
        elif(classname == 6):
            print('Result --> G')
            result = 'G'
        elif(classname == 7):
            print('Result --> H')
            result = 'H'
        elif(classname == 8):
            print('Result --> I')
            result = 'I'
        elif(classname == 9):
            print('Result --> J')
            result = 'J'
        elif(classname == 10):
            print('Result --> K')
            result = 'K'
        elif(classname == 11):
            print('Result --> L')
            result = 'L'
        elif(classname == 12):
            print('Result --> M')
            result = 'M'
        elif(classname == 13):
            print('Result --> N')
            result = 'N'
        elif(classname == 14):
            print('Result --> O')
            result = 'O'
        elif(classname == 15):
            print('Result --> P')
            result = 'P'
        elif(classname == 16):
            print('Result --> Q')
            result = 'Q'
        elif(classname == 17):
            print('Result --> R')
            result = 'R'
        elif(classname == 18):
            print('Result --> S')
            result = 'S'
        elif(classname == 19):
            print('Result --> T')
            result = 'T'
        elif(classname == 20):
            print('Result --> U')
            result = 'U'
        elif(classname == 21):
            print('Result --> V')
            result = 'V'
        elif(classname == 22):
            print('Result --> W')
            result = 'W'
        elif(classname == 23):
            print('Result --> X')
            result = 'X'
        elif(classname == 24):
            print('Result --> Y')
            result = 'Y'
        elif(classname == 25):
            print('Result --> Z')
            result = 'Z'
        else:
            print('Not Found')
            result = 'Not Found'
        # sio.emit('send res',classname)
        return result

    except Exception as e:
        print(e)
        return e
