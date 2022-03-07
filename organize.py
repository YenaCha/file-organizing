import os
import shutil
files = os.listdir('C:/Users/yena0/Downloads/Python/class 99/dummy')
for f in files:
    root,ext = os.path.splitext('C:/Users/yena0/Downloads/Python/class 99/dummy/'+f)
    isexist = os.path.exists('C:/Users/yena0/Downloads/Python/class 99/dummy/'+ext)
    if(isexist == False):
        os.mkdir('C:/Users/yena0/Downloads/Python/class 99/dummy/'+ext)
        source = 'C:/Users/yena0/Downloads/Python/class 99/dummy/'+f
        destination = 'C:/Users/yena0/Downloads/Python/class 99/dummy/'+ext
        shutil.move(source, destination)
    elif(isexist == True):
        source = 'C:/Users/yena0/Downloads/Python/class 99/dummy/'+f
        destination = 'C:/Users/yena0/Downloads/Python/class 99/dummy/'+ext
        shutil.move(source, destination)