#!/usr/bin/env python

import sys
import time
import os


def crypt(f_name, way):
    out_file = ""
    command =""
    if way == "en":
        out_file = "en_"+f_name
        command = "openssl enc -e -aes-128-cbc" + " -k " + key + " -in " + f_name + " -out " + out_file
        print command
    if way == "de":
        out_file = f_name.replace("en", "de")
        command = "openssl enc -d -aes-128-cbc" + " -k " + key + " -in " + f_name + " -out " + out_file
    begin_time = time.time()
    os.system(command)
    end_time = time.time()
    return end_time-begin_time


if __name__ == "__main__":
    key = "qwertyui+=asdqwe"
    for i in range(1,50):
        file_size = str(i) + "G"
        file_name = file_size + ".iso"
        list_en = []
        list_de = []
        os.system("fallocate -l "+file_size+" "+file_name)
        for i in range(0,3):
            t = crypt(file_name, "en")
            list_en.append(t)
        with open("ans.txt","a+") as f:
            f.write(file_name+" : "+str(list_en)+"\n")
        os.system("rm *.iso")