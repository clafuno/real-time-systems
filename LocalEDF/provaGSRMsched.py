#!/usr/bin/python

import sys
import os
import Utils
import random
from heapq import heappush, heappop

from Task import Task
from Partition import Partition
from Core import Core
import System
import Model
import LSEDFt
import BinPacking
import chronogram

#-------------------------#
#          MAIN           #
#-------------------------#
def main (argv):
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    ## Inicialization
    globalUtil = 0.8
    mCores = 2 # Cores in the system
    nPartCriticas = 4 # nPartitions = nTasks
    allocationPolicy = "WF" # Policy to allocate tasks in cores ("FF", "NF", "BF", "WF")


    parts = []
    partInCore = [] # i = core index. Cotains paritions in each core.
    chrono = [] # trace for representation
    Texec = [] # execution time of the system
    System.defineSystem(mCores, globalUtil)

    	
    # Parameters partitions
    params = ((20,4,0.2), (30, 6, 0.2), (50, 8, 0.16), (60, 12, 0.5), (10,2,0.15),(40,5,0.3), (70, 4, 0.5), (35, 3, 0.2))
    
    cid = [] #Configuration N cores
    for i in range(mCores):
        cid.append("C"+str(i))
        System.addCore(cid[i])
        Model.addCoreModel(cid[i], Core(cid[i]))


    for i in range(nPartCriticas):
        (per, c, u) = params[i] # Period, exec.time, utilization
        pid = "P"+str(i+1) # Partition
        tid = "T"+str(i+1) # Task
        p1 = Partition(pid, 1, u) # (ID, priority, util)
        t1 = Task(tid, u) 
        t1.taskParams(per, c)
        p1.partAddTask(tid, u)
        Model.addTaskModel(tid, t1)
        System.addPartition(pid)
        Model.addPartModel(pid, p1)

        ## Bin Packing Allocation
        BinPacking.initBin(allocationPolicy, mCores, globalUtil)
        core = BinPacking.binAdd(tid, u)
        print "core bn: ",core
        coreId = Model.coreById(cid[core])
        coreId.coreAddPartU(pid, u)

        ## Fast allocation
        # core = Model.coreById(cid[i%mCores]) # Select core for partition 
        # core.coreAddPartU(pid,u) # Assign partition to core
        
        p1.show()

        
    print "No Partitions: ", System.numberPartitions()
    System.show()
    

    for i in range(mCores):
        cs = Model.coreById(cid[i]); #Id of core
        partInCore.append(cs.coreParts()) #Vector containing partitions in core
    print partInCore

    for i in range(mCores):
        LSEDFt.schedInit()
        for j in range(len(partInCore[i])):
            pid = partInCore[i][j]
            LSEDFt.scheAddPartition(pid)
        print "Core: ", i, " Tasks: "
        LSEDFt.showTasks()
        a, clock = LSEDFt.schedRun(100)
        chrono.append(a)
        Texec.append(clock)

    ## Representation

    hyper = max(Texec)
    
    print "Hyper: ", hyper
    chronogram.chronoInit(mCores, hyper, "chrono")

    #Pone una linea por cada core con su nombre: C0, C1, C2, .....    
    for i in range(mCores):
        chronogram.chronoAddLine(i, "C"+str(i))

    #listaEjecuciones = chrono[i]
    for i in range(mCores):
        for le in chrono[i]:
            (tsk, start, end) = le
            chronogram.chronoAddExec(i, start, end, tsk)

    chronogram.chronoClose()


        
main (sys.argv)