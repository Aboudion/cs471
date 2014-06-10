#Deque needed for handling Queue ADT
from collections import deque

class Process:
    __name = NULL
    __ProcessId = 0
    __age = 0
    __priority = 0
    
    def __init__(self, na = NULL, pi = 0, ag = 0, pr = 0):
        __name = na
        __ProcessId = pi
        __age = ag
        __priority = 0
        
    def getName(self):
        return __name
    
    def getPi(self):
        return __ProcessId
    
    def getAge(self):
        return __age
    
    def getPriority(self):
        return __priority
    
    def upPriority(self):
        __priority = __priority - 1
        
class Queue:
    __AcceptablePriority = 0
    __Processes = deque()
    __Empty = True 

    def __init__(self, ac = 0, pr = Process(), em = True):
        __AcceptablePriority = ac
        if(pr != 0): #is the process not junk input
            __Processes.append(pr)
        __Empty = em
            
    #get current process from front
    def getProcess(self):
        return __Process.popleft()
    
    #add process to back
    def addProcess(self, pr):
        __Process.append(pr)
        
    def isEmpty(self):
        return __Empty
    

def Run():
  #Main Function
  tester = 0 #test loop, currently 5 times
  RunLoop = True #on/off switch
  current = Process() #Process to be handled by user
  input = Process() #process to be given by user
  
  #3 priority Queues
  Q1 = Queue(1, 0, true)
  Q2 = Queue(2, 0, true)
  Q3 = Queue(3, 0, true)
  
  BlockList = [] #initial blocklist
  
  #adds process to q based on priority
  def SortProcess(self, p = Process()):
    if(p.getPriority() == 1)
        Q1.addProcess(input)
    else if(p.getPriority() == 2)
        Q2.addProcess(input)
    else
        Q3.addProcess(input)
        
        
#returns highest priority process from Queue
def getCurrent(self):
    if(!Q1.isEmpty()):
        return Q1.getProcess()
    else if(!Q2.isEmpty()):
        return Q2.getProcess()
    else if(!Q3.isEmpty()):
        return Q3.getProcess()
    else
        return Null
            
  #Main Loop
  while (RunLoop):
      #take input
        
      #process inputs
        ##add to Queue
        SortProcess(input)
        ##grab current process from Queue
        current = getCurrent()
        ##prompt for block input
        
        
        ##resolve process 
        if(input = 0):
            BlockList.append(current)
            #update Block GUI
        else if(input = 1):
            SortProcess(current)
            #update Q GUI
        else
            #Update Process Run GUI
        
        #implementation test code####################################################
        tester = tester + 1
        if(tester == 5):
            RunLoop = False
        ####################################################
    
if __name__ == '__main__':
    Run() #autorun for main
