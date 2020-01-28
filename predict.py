import socketio
import argparse
from keras.models import load_model
from keras.preprocessing import image

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--filename", required=True,
                help="file name")
args = vars(ap.parse_args())

file_name = args["filename"]

# standard Python
sio = socketio.Client()
sio.connect('http://139.59.37.180:3770')

def predict(file_name):
    model = load_model("testmodel3.h5")

    test_image = image.load_img(file_name,color_mode="grayscale",target_size=(28,28,1))
    #print(test_image.format)
    #print(test_image.mode)
    #print(test_image.size)

    test_image = image.img_to_array(test_image)
    test_image = test_image.reshape((-1,) + test_image.shape)

    print(test_image.dtype)
    print(test_image.shape)

    y_pred = model.predict_classes(test_image)
    print(y_pred)
    prediction = y_pred[0]
    classname = y_pred[0]
    print("Class: ",classname)
    print(y_pred)
    f = open('results.txt','w') 
    f.write(classname)
    f.close() 
    sio.emit('send_res', classname)
    return classname

predict(file_name)