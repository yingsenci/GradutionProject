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
    print "crypt_time is: ",end_time-begin_time


if __name__ == "__main__":
    key = "qwertyui+=asdqwe"
    file_name, order = raw_input("please input the order:\n").split(" ")
    crypt(file_name, order[1:])


