#!/usr/bin/env python
import time
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex


class MyCrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, contain):
        item = AES.new(self.key, self.mode, self.key)
        length = 16
        cnt = len(contain)
        additon = length - (cnt % length)
        contain += '\0' * additon
        self.ciphertext = item.encrypt(contain)
        return b2a_hex(self.ciphertext)

    def decrypt(self,contain):
        item = AES.new(self.key, self.mode, self.key)
        ans = item.decrypt(a2b_hex(contain))
        return ans.rstrip('\0')


def getpath(path):
    pos = -1;
    for i in range(0, len(path)):
        if path[i] == '/':
            pos = i
    if pos == -1:
        print "error: the path you input may be wrong\n"
        return -1
    else:
        return pos, path[0:pos]


def getfile(path,site):
    pos = -1
    for i in range(len(path)-1, -1, -1):
        if path[i]=='.':
            pos = i
            break
    return path[site:pos], path[pos:]


if __name__ == '__main__':
    key = "qwertyuiop+=zxas"
    orders = raw_input("please input the mode(encrypt or decrypt) and the filepath,split them with a space \n")
    start_time = time.time()
    ls = orders.split(' ')
    order = ls[0]
    path = ls[1]
    pos, rootpath = getpath(path)
    filename, filetype = getfile(path, pos)
    filename = filename.replace('/', '')
    #print rootpath, filename, filetype
    fi = open(path, "rb")
    string = fi.read()
    file_open_time = time.time()
    print "file_open_time: ", file_open_time-start_time
    mycrypt = MyCrypt(key)
    if order == "encrypt":
        en = mycrypt.encrypt(string)
        encrypt_time = time.time()
        print "encrypt_time: ", encrypt_time-file_open_time
        encryt_filename = rootpath+"/AES_en_"+filename+filetype
        print "the result of encryption:\n", en
        fo = open(encryt_filename, "wb")
        fo.write(en)
        fo.close()
        file_write_time = time.time()
        print "file_write_time: ", file_write_time-encrypt_time
    if order == "decrypt":
        de = mycrypt.decrypt(string)
        decrypt_time = time.time()
        print "decrypt_time: ", decrypt_time-file_open_time
        filename = filename.replace("AES_en", "/AES_de")
        decryt_filename = rootpath+filename+filetype
        print "the result of decryption:\n", de
        fo = open(decryt_filename,"wb")
        fo.write(de)
        fo.close()
        file_write_time = time.time()
        print "file_write_time: ", file_write_time-decrypt_time
    fi.close()