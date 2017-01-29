class Task:

    NoTasks = 0; 
  
    def __init__(self, id, u):  # attributos: Id, Period, Deadline, WCET, Util
		self.id = id
		self.util = u

		self.NoTasks += 1


    def taskParams(self, Per, Wcet):  # deadline = period
		self.period = Per
		self.deadLine = Per
		self.wcet = Wcet

    def taskId(self):
        return self.id

    def taskPeriod(self):
        return self.period  

    def taskDeadline(self):
		return self.deadLine

    def taskWCET(self):
		return self.wcet
    
    def taskUtil(self):
		return self.util
        
    def taskNumber(self):
		return Task.NoTasks
		
    def show(self):
		print "    Task( " +str(self.id)+ ", " +str(self.period)+ ", " +str(self.deadLine)+ ", " +str(self.wcet)+ ", " +str(self.util)+ " )"
    

