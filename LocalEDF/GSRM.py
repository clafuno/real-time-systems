##Module: Utils
import sys
import os
from heapq import heappush, heappop

import Model
import Utils
import Tracer

tasksIds = []
tasks = {}

nTaskActiv = {}

clock = 0
PRI = 0
PER = 1
DED = 2
WCT = 3
ETM = 4
TID = 5

        
def schedInit():
    global clock, tasksIds, tasks
    clock = 0
    tasksIds = []
    tasks = {}
    global readyQueue, blockedQueue, blockedTasks
    readyQueue = []   # this is a heap
    blockedQueue = []
    blockedTasks = [] # this is a list


def scheAddPartition(pid):
    global tasksIds
    part = Model.partById(pid)
    tsks = part.partTaskList()
    for i in range(len(tsks)):
        tasksIds.append(tsks[i])

def nTaskActivation(tid):
	if (nTaskActiv.has_key(tid)):
	    nTaskActiv[tid] = nTaskActiv[tid] + 1
	else:
		nTaskActiv[tid] = 1

def showTasks():
    print tasksIds
    
def schedRun(ticks):
    #prepare data structures
    global tasks
    tperiods = []
    tList = []
    for i in range(len(tasksIds)):
        tsk = Model.taskById(tasksIds[i])
        tperiods.append(tsk.taskPeriod())
        elem = (tsk.taskPeriod(), tsk.taskId(), tsk.taskDeadline(), tsk.taskWCET())
        tList.append(elem)

    hyper = Utils.HyperPeriod(tperiods)
    print "Hyperperiodo = ", hyper
    tList.sort()   #RM priority
    prio = 1
    for i in range(len(tList)):
        t = tList[i]
        #         tid, period, rdeadline, absdel, wcet, texe, nact)
        values = (t[1], t[0], t[2], t[2], t[3], 0, 0)
    	prio = t[2] # priority is equal to abs_deadline
        heappush(blockedQueue, ((0, prio), (values) ))
    
    print blockedQueue
    
    Tracer.traceInit(2)
    clock = 0
    pTaskId = "X"
    
    endQueue = [] # heap

    ## Event-ish ###
    while (clock < hyper):
        minReleaseTime = 9999
        minWCET = 9999

        # check if there are tasks waiting
        if (len(blockedQueue) > 0): 
            (releaseAt,prioRelease) = blockedQueue[0][0] # next activation time and period(prio)
            minReleaseTime = releaseAt - clock # time to next activation

        # check if there are tasks running
        if (len(readyQueue) > 0):
            minWCET = readyQueue[0][1][4] - readyQueue[0][1][5] # closer wcet = wcet - texec


        if (minWCET <= minReleaseTime): # Finishing time of running task is closer than next period/deadline
            ### Finish the execution of the task due to wcet and add it to blockedQueue ###

            ((prio), (cTaskId, period, rdead, adead, wcet, texec, nActiv)) = heappop(readyQueue) # running task
            Tracer.traceExecBegin(0, clock, cTaskId)

            texec =  clock + wcet # update execution time of the task

            clock = texec # clock is set to the moment the task finishes

            if (clock > adead):
                print "Task ", cTaskId, " missed at: ", adead, "removed"
                Tracer.traceExecEnd(0, clock, cTaskId)
                nxtActiv = nActiv * period
                adead = nxtActiv + rdead
                heappush(blockedQueue, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))

            else:
            # Task finishes execution because we are in wcet instant
                Tracer.traceExecEnd(0, clock, cTaskId)
                nxtActiv = nActiv * period
                adead = nxtActiv + rdead
                prio = adead #Update priority to next
            
                # Insert task in finished process.
                heappush(blockedQueue, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))

        elif (minReleaseTime <= minWCET): # Next activation of a task is closer than finishing time of another
            ### Check deadline and/or activate the task ###

            (releaseAt, prio) = blockedQueue[0][0]
            clock = releaseAt # update clock
            while (clock  == releaseAt):
                # Move task from blockedQueue to readyQueue
                (tid, period, rdead, adead, wcet, texec, nActiv) = blockedQueue[0][1]
                t = heappop(blockedQueue)
                heappush(readyQueue, ((prio), (tid, period, rdead, adead, wcet, 0, nActiv + 1)))
                
                if (len(blockedQueue) > 0): # IF there are processes to schedule
                    (releaseAt, prio) = blockedQueue[0][0]
                else:
                    releaseAt = clock + 999
      

    Tracer.traceShow(0)
    print "Hyperperiodo = ", hyper, " Clock: ", clock





