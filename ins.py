import os

try:
    os.system("pip install --upgrade setuptools")
    os.system("pip install numpy")
    os.system("pip install wheel")
    os.system("pip install matplotlib")
    os.system("pip install seaborn")
    os.system("pip install sklearn")
    os.system("pip install keras")
    os.system("pip install opencv-python")
    os.system("pip install tensorflow")
    os.system("pip install tf-nightly")
    os.system("pip install cloud-tpu-client")
    os.system("pip install pillow")
    os.system("pip install socketio")

    # export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-linux_x86_64.whl
    # pip install — upgrade $TF_BINARY_URL
    # https://medium.com/analytics-vidhya/sign-language-recognition-using-cnn-and-opencv-beginner-level-72091ca35a19

except Exception as e:
    print(e)