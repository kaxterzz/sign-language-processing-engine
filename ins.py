import os

try:
    os.system("sudo pip install --upgrade setuptools")
    os.system("sudo pip install numpy")
    os.system("sudo pip install wheel")
    os.system("sudo pip install matplotlib")
    os.system("sudo pip install seaborn")
    os.system("sudo pip install sklearn")
    os.system("sudo pip install keras")
    os.system("sudo pip install opencv-python")
    os.system("sudo pip install tensorflow")
    

except Exception as e:
    print(e)