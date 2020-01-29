from flask import Flask, request, Blueprint, jsonify
import string
import random
import os
import subprocess
from base64 import b64decode

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route("/test" , methods=['POST'])
def test():
    try:
        if request.method == 'POST':
            val = request.form['test']
            print(val)
            return val
        else:
            return "err"
    except Exception as e:
        print(e)
        return e

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route('/upload-image', methods=['POST'])
def upload_files():
    try:
        if request.method == 'POST':
            f = request.files['file']  
            random_file_name = 'images/'+randomString()+'.png'
            f.save(random_file_name)
            #res = predict(random_file_name)
            #process = subprocess.Popen(['python', 'predict.py', '--filename', random_file_name])
            cmd = "python predict.py --filename "+random_file_name
            os.system(cmd)
            print('Running in process', process.pid)
            process.wait(timeout=15)
            return "true"
        else:
            return "false"

    except Exception as e:
        print(e)
        return e

# @app.route('/upload-image', methods=['POST'])
# def upload_files():
#     try:
#         if request.method == 'POST':
#             data = request.get_json(silent=True)
#             file_data = data.get('image')
            
#             img_name = secure_filename(static_file.filename)
#             Decode the Base64 string, making sure that it contains only valid characters
#             data = b64decode(file_data)
#             print(static_file_name)
#             random_file_name = 'images/'+randomString()+'.png'
            
#             f = open(random_file_name, 'wb')
#             f.write(data)
#             f.close()
#             status = static_file.save(path + img_name)
#             full_file = path + static_file_name
#             res = predict(str(random_file_name))
#             #return "true"
#             return jsonify(res)
#         else:
#             return "false"

#     except Exception as e:
#         print(e)
#         return e


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True,port="1230")
