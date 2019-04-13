#!/usr/bin/env python

import time
import os


def getinfo():
    command = "ls -n"
    process = os.popen(command)
    res = process.read()
    item = res.split("\n")
    return item


if __name__ == "__main__" :
    while True:
        data_pp = getinfo()
        time.sleep(1)
        data_rr = getinfo()
        flag = 0
        for x in range(1,len(data_pp)):
            data_p = data_pp[x]
            data_r = data_rr[x]
            if data_p == data_r and data_r[len(data_r)-3:] == "iso" :
                flag = 1
                pos = -1
                for i in range(len(data_r)-1,-1,-1):
                    if data_r[i]  == " " :
                       pos = i
                       break
                rm_item = data_r[pos:]
                os.system("rm "+rm_item)
        
