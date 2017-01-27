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
    mCores = 1
  
    parts = []
    System.defineSystem(mCores, globalUtil)

    	
    nPartCriticas = 4

    params = ((20,4,0.2), (30, 6, 0.2), (50, 8, 0.16), (60, 12, 0.2))
    
    cid = "C0"
    c = Core(cid)
    System.addCore(cid)
    Model.addCoreModel(cid, c)

    	
    for i in range(4):
        (per, c, u) = params[i]
        pid = "P"+str(i+1)
        tid = "T"+str(i+1)
        p1 = Partition(pid, 1, u)
        t1 = Task(tid, u)
        t1.taskParams(per, c)
        p1.partAddTask(tid, u)
        Model.addTaskModel(tid, t1)
        System.addPartition(pid)
        Model.addPartModel(pid, p1)
        core = Model.coreById(cid)
        core.coreAddPartU(pid, u)
        p1.show()

        
    print "No Partitions: ", System.numberPartitions()
    System.show()
    
    GSRM.schedInit()
    for i in range(4): # Para cada particions creada
        pid = "P"+str(i+1)
        GSRM.scheAddPartition(pid)
    

    print "Tasks: "
    GSRM.showTasks()
    GSRM.schedRun(100)
        
main (sys.argv)