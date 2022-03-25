
from random import randint as ran
from tabulate import tabulate


class processPriority:
    processesP = []

    def __init__(self, processID, arrivalTime, burstTime, priority):
        self.processID = "P" + str(processID)
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.completionTime = 0
        self.turnAroundTime = 0
        self.waitingTime = 0
        self.priority = priority
        self.remainingBurstTime = burstTime

    def calTurnaroundTime(self):
        self.turnAroundTime = self.completionTime - self.arrivalTime

    def calWaitingTime(self):
        self.waitingTime = self.turnAroundTime - self.burstTime
        if self.waitingTime < 0:
            self.waitingTime = 0


def printData(queue, completionQ):
    avgW = 0
    avgC = 0
    avgT = 0
    head = [
        "Process ID", "Arrival time", "Burst time", "Priority",
        "Completion Time", "Turn Around Time", "Waiting Time"]
    n = len(queue)
    # data = [[], [], []]
    data = []

    for pro in queue:
        pro.calTurnaroundTime()
        pro.calWaitingTime()
    for i in range(len(queue)):
        j = []
        j.append(queue[i].processID)
        j.append(queue[i].arrivalTime)
        j.append(queue[i].burstTime)
        j.append(queue[i].priority)
        j.append(queue[i].completionTime)
        j.append(queue[i].turnAroundTime)
        j.append(queue[i].waitingTime)
        data.append(j)
    data.sort(key=lambda x: x[0])
    print(tabulate(data, headers=head, tablefmt="grid", colalign="center"))
    for i in queue:
        avgC += i.completionTime
        avgT += i.turnAroundTime
        avgW += i.waitingTime
    avgC /= len(queue)
    avgT /= len(queue)
    avgW /= len(queue)
    print("\n Completion Queue Is \n\t")
    for i in completionQ:
        print(f"{i.processID}", end="--")
    print()
    print(f"\nAverage Completion Time of Processes is {round(avgC,3)}")
    print(f"Average Turn Around Time of Processes is {round(avgT,3)}")
    print(f"Average Waiting Time of Processes is {round(avgW,3)} \n")


def createProcessManually():
    p = input("Number of processes :- ")
    for i in range(int(p)):
        x, y, z = input(
            f"Enter the arrival time, burst time and Priority for {i+1}st process :- ").split()
        processPriority.processesP.append(
            processPriority(i+1, int(x), int(y), int(z)))
    # for i in processes:
    #     print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    # return processes


def createProcessRandomly():
    p = int(input("Number of processes:- "))
    while p:
        at = ran(0, p)
        bt = ran(1, 20)
        pri = ran(0, 10)
        if at < bt:
            processPriority.processesP.append(processPriority(p, at, bt, pri))
            p -= 1


def createProcess():
    print("How you want to create Processes ?")
    print("\t 1. Manual creation of Processes.")
    print("\t 2. Random creation of Processes.")
    ans = input()
    if ans == "1":
        createProcessManually()
    elif ans == "2":
        createProcessRandomly()
    else:
        print("Enter the correct Choice !")


def priority(processesP):
    readyQ = []
    global te #total execution time
    te = 0
    completeQ = []

    #complete Execution function
    def complete(pro, processesP):
        global te
        completeQ.append(pro)
        te += pro.burstTime
        rmov = []
        for pro in processesP:
            if pro.arrivalTime <= te:
                readyQ.append(pro)
                rmov.append(pro)
        for pro in rmov:
            processesP.remove(pro)


    processesP.sort(key=lambda pro: (pro.arrivalTime, -pro.priority))
    readyQ.append(processesP.pop(0))
    complete(readyQ.pop(0), processesP)
    while len(readyQ):
        readyQ.sort(key=lambda pro: pro.priority, reverse=True)
        complete(readyQ.pop(0), processesP)
    for pro in completeQ:
        if completeQ.index(pro) == 0:
            pro.completionTime = pro.arrivalTime + pro.burstTime
            ct = pro.arrivalTime + pro.burstTime
        else:
            pro.completionTime = ct + pro.burstTime
            ct = pro.burstTime + ct

    return(completeQ)


def priorityP(processesP):
    readyQ = []
    completeQ = []
    global te
    te = 0

    def complete(pro, processesP):
        global te
        # print("1")
        te += 1
        pro.remainingBurstTime -= 1
        completeQ.append(pro)
        rmov = []
        if len(processesP) > 0:
            for i in processesP:
                if i.arrivalTime <= te:
                    readyQ.append(i)
                    rmov.append(i)
            if len(rmov):
                for i in rmov:
                    processesP.remove(i)
        if pro.remainingBurstTime > 0:
            readyQ.append(pro)
        else:
            pro.completionTime = te
# When two process have same arrival time it will sort according to Priority 
    processesP.sort(key=lambda pro: (pro.arrivalTime, -pro.priority))
    readyQ.append(processesP.pop(0))
    # complete processesP.pop(0), processesP)
    complete(readyQ.pop(0), processesP)
    while len(readyQ) > 0:
        readyQ.sort(key=lambda pro: -pro.priority)
        complete(readyQ.pop(0), processesP)
    # queue = list(set(completeQ))
    return completeQ

    # rational agent


def mainP():
    flag = 1
    while flag == 1:
        print("\t1. Priority non Preemptive")
        print("\t2. Priority Preemptive")
        print("\t0. Exit")
        p = input("\nWhich Priority Algorithm You want to Execute ?? :- ")
        p = int(p)
        if p == 0:
            flag = 0
            break
        else:
            if p == 1:
                createProcess()
                pp = priority(processPriority.processesP)
                printData(list(set(pp)), pp)
            elif p == 2:
                createProcess()
                pp = priorityP(processPriority.processesP)
                printData(list(set(pp)), pp)
            else:
                print("Enter the Correct Choice !!!")
        processPriority.processesP.clear()
