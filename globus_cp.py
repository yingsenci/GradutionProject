#!/usr/bin/env python

import os
import time
import sys

def crypt(f_name, way):
    fo = open("res.txt","a+")
    key = "qwaszx+=vcfdrekg"
    out_file = ""
    command =""
    if way == "en":
        out_file = "en_"+f_name
        command = "openssl enc -e -aes-128-cbc" + " -k " + key + " -in " + f_name + " -out " + out_file
        print command.replace(key,"key.key")
    if way == "de":
        out_file = f_name.replace("en", "de")
        command = "openssl enc -d -aes-128-cbc" + " -k " + key + " -in " + f_name + " -out " + out_file
    begin_time = time.time()
    os.system(command)
    end_time = time.time()
    print way + "crypt_time is: ",end_time-begin_time
    fo.write(way + "crypt_time is: "+str(end_time-begin_time)+"\n")
    fo.close()
def transfer(file_size):
    fo = open("res.txt","a+")
    file_name = file_size+".iso"
    os.system("fallocate -l "+file_size+" "+file_name)
    os.system("fallocate -l "+file_size+" e"+file_name)
    #no_encryption
    cmd = " "
    command = "globus-url-copy -vb" + cmd + "file:///home/terry/ysc/" + file_name + " gsiftp://ubuntu/home/terry/ysc/"
    print "command: ", command
    fo.write("command: "+command+"\n")
    begin_time = time.time()
    process = os.popen(command)
    res = process.read()
    end_time = time.time()
    process.close()
    print res
    fo.write(res+"\n")
    print "transfer time: ", end_time-begin_time
    fo.write("transfer time: "+str(end_time-begin_time)+"\n")
    #encryption
    cmd = " -dcpriv "
    command = "globus-url-copy -vb" + cmd + "file:///home/terry/ysc/" + "e" + file_name + " gsiftp://ubuntu/home/terry/ysc/"
    print "command: ", command
    fo.write("command: "+command+"\n")
    begin_time = time.time()
    process = os.popen(command)
    res = process.read()
    end_time = time.time()
    process.close()
    print res
    fo.write(res+"\n")
    print "transfer time: ", end_time-begin_time
    fo.write("transfer time: "+str(end_time-begin_time)+"\n")
    fo.close()
    os.system("rm *.iso")
    #openssl aes encrypt and decrypt
    #crypt(file_name, "en")
    #crypt("en_"+file_name, "de")


if __name__ == "__main__":
    file_size = input("please input the filesize:\n")
    for size in range(file_size,file_size+10):
        if size == 0 :
            continue
        transfer(str(size)+"G")
        
