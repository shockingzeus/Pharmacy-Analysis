#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:27:29 2018

@author: Xiaoqing
"""

import time
import sys
from decimal import *
            

def main(filein, fileout):
    AMTdict = {}
    NAMEdict = {}
    name = ""
    headcount = 0
    outstr=[]
    with open(filein,"r", encoding='utf-8') as f:
        for line in f:
            firstname, lastname, medicine, amount = line.rstrip().rsplit(",")[1:5]
            name = firstname+","+lastname
            try:
                amount=Decimal(amount)
                if medicine in AMTdict:
                    AMTdict[medicine]+=amount
                    if name not in NAMEdict[medicine]:
                        NAMEdict[medicine].add(name)
                else:
                    AMTdict[medicine] = amount
                    NAMEdict[medicine] = set([name])
            except:
                pass

    for kv in sorted(AMTdict.items(),key=lambda kv: (-kv[1], kv[0])):
        medicine = kv[0]
        headcount = str(len(NAMEdict[medicine]))
        amount = str(kv[1])
        outstr.append(",".join([medicine,headcount,amount]))
            
    outstrs = "\n".join(outstr)
    with open(fileout,"w") as f:
        f.write(outstrs)

import contextlib          
@contextlib.contextmanager  
def timer(msg):
# for speed test
    start = time.time()
    yield
    end = time.time()
    print("%s: %.02fms" % (msg, (end-start)*1000))
           
if __name__=="__main__":
    main(str(sys.argv[1]), str(sys.argv[2]))