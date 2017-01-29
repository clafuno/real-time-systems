##Module Model

DCORES = {}
DPARTS = {}
DTASKS = {}
    
def addCoreModel(cid, c):
    DCORES[cid]=c
   
def addPartModel(pid, p):
    DPARTS[pid]=p
    	  
def addTaskModel(tid, t):
    DTASKS[tid]=t    
    	
def partById(pid):
    return DPARTS[pid]
    
def coreById(cid):
    return DCORES[cid]
    
def taskById(tid):
    return DTASKS[tid]