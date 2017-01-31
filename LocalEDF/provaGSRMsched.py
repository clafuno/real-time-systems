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
import LSEDFe
import BinPacking

#-------------------------#
#          MAIN           #
#-------------------------#
def main (argv):
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    globalUtil = 0.8
    mCores = 3 # Cores in the system

    parts = []
    partInCore = []
    System.defineSystem(mCores, globalUtil)

    	
    nPartCriticas = 8
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
        BinPacking.initBin("BF", mCores, globalUtil)
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
        partInCore.append(cs.coreParts())
    print partInCore

    for i in range(mCores):
        LSEDFe.schedInit()
        for j in range(len(partInCore[i])):
            pid = partInCore[i][j]
            LSEDFe.scheAddPartition(pid)
        print "Core: ", i, " Tasks: "
        LSEDFe.showTasks()
        LSEDFe.schedRun(100)
        
main (sys.argv)