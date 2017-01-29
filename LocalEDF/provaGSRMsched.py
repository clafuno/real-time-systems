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
import GSRM

#-------------------------#
#          MAIN           #
#-------------------------#
def main (argv):
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    globalUtil = 0.8
    mCores = 2 # Cores in the system

    parts = []
    System.defineSystem(mCores, globalUtil)

    	
    nPartCriticas = 4
    # Parameters partitions
    params = ((20,4,0.2), (30, 6, 0.2), (50, 8, 0.16), (60, 12, 0.2))
    
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

        core = Model.coreById(cid[i%mCores]) # Select core for partition
        core.coreAddPartU(pid, u) # Assign partition to core
        p1.show()

        
    print "No Partitions: ", System.numberPartitions()
    System.show()
    
    GSRM.schedInit()
    for i in range(nPartCriticas):
        pid = "P"+str(i+1)
        GSRM.scheAddPartition(pid)
    

    print "Tasks: "
    GSRM.showTasks()
    GSRM.schedRun(100)
        
main (sys.argv)