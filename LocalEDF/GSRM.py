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
    global readyQueue, releaseTime, blockedTasks
    readyQueue = []   # this is a heap
    releaseTime = []
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
        heappush(releaseTime, ((0, prio), (values) ))
    
    print releaseTime
    
    Tracer.traceInit(2)
    clock = 0
    pTaskId = "X"
    
    # while (clock < hyper):
    #     minReleaseTime = 9999
    #     minWCET = 9999

    #     # check if there are tasks waiting
    #     if (len(releaseTime) > 0): 
    #         (minReleaseTime,prioRelease) = releaseTime[0][0] # activation time and period(prio)

    #     # check if there are tasks running
    #     if (len(readyQueue) > 0):
    #         minWCET = readyQueue[0][1][5] # wcet of the task with closer period

    #     if (minWCET <= minReleaseTime): # Finishing time of running task is closer than next period/deadline
    #         ### Finish the execution of the task due to wcet and add it to releaseTime ###

    #         ((prio), (cTaskId, period, rdead, adead, wcet, texec, nActiv)) = heappop(readyQueue) # running task
    #         texec =  releaseAt + wcet # update execution time of the tast

    #         if()

    #         clock = prio[0] + texec # clock is set to the moment the task finishes

    #         # Task finishes execution because we are in wcet instant
    #         Tracer.traceExecEnd(0, clock, cTaskId)
    #         nxtActiv = nActiv * period
    #         adead = nxtActiv + rdead
    #         prio = adead #Update priority to next
            
    #         # Insert task in ready process.
    #         heappush(releaseTime, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))

    #     else: # Next activation of a task is closer than finishing time of another
    #         ### Check deadline and/or activate the task ###

    #         if() # check if the task has finished before deadline


    #         (releaseAt, prio) = releaseTime[0][0]
    #         clock = # update clock
    #         while (clock  == releaseAt):
    #             # Move task from releaseTime to readyQueue
    #             (tid, period, rdead, adead, wcet, texec, nActiv) = releaseTime[0][1]
    #             t = heappop(releaseTime)
    #             heappush(readyQueue, ((prio), (tid, period, rdead, adead, wcet, 0, nActiv + 1)))
                
    #             if (len(releaseTime) > 0): # IF there are processes to schedule
    #                 (releaseAt, prio) = releaseTime[0][0]
    #             else:
    #                 releaseAt = clock + 999


    while (clock < hyper):
        #add tasks in blocked to ready if release time
        nitems = len(releaseTime)
        if (nitems > 0):
            (releaseAt, prio) = releaseTime[0][0]
            while (clock  == releaseAt):
                (tid, period, rdead, adead, wcet, texec, nActiv) = releaseTime[0][1]
                t = heappop(releaseTime)
                heappush(readyQueue, ((prio), (tid, period, rdead, adead, wcet, 0, nActiv + 1)))
                nitems -= 1
                if (nitems > 0):
                    (releaseAt, prio) = releaseTime[0][0]
                else:
                    releaseAt = clock + 999   

        if (len(readyQueue) > 0):
            ((prio), (cTaskId, period, rdead, adead, wcet, texec, nActiv)) = heappop(readyQueue)
            #check deadline miss
            if (clock > adead):
            	print "Task ", cTaskId, " missed at: ", adead, "removed"
            	Tracer.traceExecEnd(0, clock, cTaskId)
                nxtActiv = nActiv * period
                adead = nxtActiv + rdead
                heappush(releaseTime, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))
            
            if (pTaskId <> cTaskId): #If it's different
            	Tracer.traceExecBegin(0, clock, cTaskId)
            
            clock = clock + 1
            texec += 1

            if (texec < wcet): # Pendent de finalitzar execucio
                heappush(readyQueue, ((prio), (cTaskId, period, rdead, adead, wcet, texec, nActiv)))
            else: # Finished execution
                Tracer.traceExecEnd(0, clock, cTaskId)
                nxtActiv = nActiv * period
                adead = nxtActiv + rdead
                heappush(releaseTime, ((nxtActiv, prio), (cTaskId, period, rdead, adead, wcet, 0, nActiv)))
        else: # No hi ha processos pendents de planificar
        	cTaskId = "Idle"
        	clock = clock + 1

        pTaskId = cTaskId

    Tracer.traceShow(0)
    print "Hyperperiodo = ", hyper, " Clock: ", clock





