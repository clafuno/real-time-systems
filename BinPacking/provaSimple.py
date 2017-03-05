import sys
import os

import BinPacking

def main (argv):

#Bins  creation
    Particiones = [("P1", 0.36), ("P2", 0.16), ("P3", 0.20), ("P4", 0.46), ("P5", 0.12), ("P6", 0.38), ("P7", 0.45), ("P8", 0.27), ("P9", 0.57)]

    # try:
    #     BinPacking.initBin("KF", 4)
    # except:
    #     print "Error en la inicializacion"

# first-fit ############################################################

    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

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
    
    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

    try:
        BinPacking.initBin("FF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop()
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: FF , Not Allocated"
    print "First-Fit Decremental:"
    BinPacking.show()

# next-fit ############################################################
    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

    try:
        BinPacking.initBin("NF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop(0)
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: NF , Not Allocated"
    print "Next-Fit Incremental:"
    BinPacking.show()

    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

    try:
        BinPacking.initBin("NF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop()
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: NF , Not Allocated"
    print "Next-Fit Decremental:"
    BinPacking.show()

# best-fit ############################################################
    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

    try:
        BinPacking.initBin("BF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop(0)
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: BF , Not Allocated"
    print "Best-Fit Incremental:"
    BinPacking.show()

    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

    try:
        BinPacking.initBin("BF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop()
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: BF , Not Allocated"
    print "Best-Fit Decremental:"
    BinPacking.show()

# Worst-fit ############################################################
    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])
    print pIncr

    try:
        BinPacking.initBin("WF", 4)
        lst = pIncr
        while (len(lst) > 0):
                part = lst.pop(0)
                BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: WF , Not Allocated"
    print "Worst-Fit Incremental:"
    BinPacking.show()

    pIncr = sorted(Particiones, key=lambda Particiones: Particiones[1])

    try:
        BinPacking.initBin("WF", 4)
        lst = pIncr
        while (len(lst) > 0):
            part = lst.pop()
            BinPacking.binAdd(part[0], part[1])
    except:
        print "Error: WF , Not Allocated"
    print "Worst-Fit Decremental:"
    BinPacking.show()

main (sys.argv)
