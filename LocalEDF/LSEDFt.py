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
    chrono = []

    for i in range(len(tasksIds)):
        tsk = Model.taskById(tasksIds[i])
        tperiods.append(tsk.taskPeriod())
        elem = (tsk.taskPeriod(), tsk.taskId(), tsk.taskDeadline(), tsk.taskWCET())
        tList.append(elem)

    hyper = Utils.HyperPeriod(tperiods)
    print "Hyperperiodo = ", hyper
    print "------- Ticks scheduling -------"
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
    
    ### By-ticks mode ###                    
    while (clock < hyper):
        #add tasks in blocked to ready if release time
        nitems = len(blockedQueue)
        if (nitems > 0):
            (releaseAt, prio) = blockedQueue[0][0]
            while (clock  == releaseAt):
                (tid, period, rdead, adead, wcet, texec, nActiv) = blockedQueue[0][1]
                t = heappop(blockedQueue)
                prio = adead
                heappush(readyQueue, ((prio), (tid, period, rdead, adead, wcet, 0, nActiv + 1)))
                nitems -= 1
                if (nitems > 0):
                    (releaseAt, prio) = blockedQueue[0][0]
                else:
                    releaseAt = clock + 999   

        if (len(readyQueue) > 0):
            # Take first process from readyQueue
            ((prio), (cTaskId, period, rdead, adead, wcet, texec, nActiv)) = heappop(readyQueue)
            #check deadline miss
            if (clock > adead):
            	print "Task ", cTaskId, " missed at: ", adead, "removed"
            	Tracer.traceExecEnd(0, clock, cTaskId)
                nxtActiv = nActiv * period
                adead = nxtActiv + rdead
                heappush(blockedQueue, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))
            
            if (pTaskId <> cTaskId): #If it's different
            	Tracer.traceExecBegin(0, clock, cTaskId)
            
            clock = clock + 1
            texec += 1
            #print "Ready: ", readyQueue
            #print "blockedQueue: ", blockedQueue

            if (texec < wcet): # Pendent de finalitzar execucio
                heappush(readyQueue, ((prio), (cTaskId, period, rdead, adead, wcet, texec, nActiv)))
            else: # Finished execution
                Tracer.traceExecEnd(0, clock, cTaskId)
                nxtActiv = nActiv * period
                adead = nxtActiv + rdead
                heappush(blockedQueue, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))
        else: # No hi ha processos pendents de planificar
        	cTaskId = "Idle"
        	clock = clock + 1

        pTaskId = cTaskId
        

    chrono = Tracer.traceShow(0)
    print "Hyperperiodo = ", hyper, " Clock: ", clock

    return chrono, clock




