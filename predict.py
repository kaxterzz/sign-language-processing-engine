from keras.models import load_model
from keras.preprocessing import image

def predict(img):
    model = load_model("testmodel3.h5")

    test_image = image.load_img(img,color_mode="grayscale",target_size=(28,28,1))
    #print(test_image.format)
    #print(test_image.mode)
    #print(test_image.size)

    test_image = image.img_to_array(test_image)
    test_image  = test_image.reshape((-1,) + test_image.shape)

    print(test_image.dtype)
    print(test_image.shape)

    y_pred = model.predict_classes(test_image)
    print(y_pred)
    prediction = y_pred[0]
    classname = y_pred[0]
    print("Class: ",classname)
    print(y_pred)
    return classname