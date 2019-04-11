#!/usr/bin/env python

import os
import time

if __name__ == "__main__":
    file_name, order = raw_input("please input the filename:\n").split(" ")
    begin_time = time.time()
    if order == "-n":
        cmd = " "
    if order == "-en":
        cmd = " -dcpriv "
    command = "globus-url-copy -vb" + cmd + "file:///home/terry/ysc/" + file_name + " gsiftp://ubuntu/home/terry/ysc/"
    process = os.popen(command)
    res = process.read()
    process.close()
    print res
