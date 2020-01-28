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

except Exception as e:
    print(e)