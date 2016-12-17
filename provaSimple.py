#!/usr/bin/python

import sys
import os

import BinPacking

def main (argv):

#Bins  creation
    Particiones = [("P1", 0.36), ("P2", 0.16), ("P3", 0.20), ("P4", 0.46), ("P5", 0.12), ("P6", 0.38), ("P7", 0.45), ("P8", 0.27), ("P9", 0.57)]

    try:
        BinPacking.initBin("FF", 4)
    except:
        print "Error en la inicializacion"


# First-fit ############################################################
    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])
    print pIncr

    try:
        BinPacking.initBin("FF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop(0)
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: FF , Not Allocated"
    print "First-Fit Incremental:"
    BinPacking.show()

main (sys.argv)
