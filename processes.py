from random import randint as rint
from tabulate import tabulate


class process:
    processes = []

    def __init__(self, processID, arrivalTime, burstTime):
        self.processID = "P" + str(processID)
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.completionTime = 0
        self.turnAroundTime = 0
        self.waitingTime = 0
        self.remainingBurstTime = burstTime

    def calCompletionTime(self, p):
        self.completionTime = p - self.burstTime

    def calTurnaroundTime(self):
        self.turnAroundTime = self.completionTime - self.arrivalTime

    def calWaitingTime(self):
        self.waitingTime = self.turnAroundTime - self.burstTime
        if self.waitingTime < 0:
            self.waitingTime = 0


def createProcessManually():
    p = input("Number of processes :- ")
    for i in range(int(p)):
        x, y = input(
            f"Enter the arrival time and burst time for {i+1}st process :- ").split()
        process.processes.append(process(i+1, int(x), int(y)))
    # for i in processes:
    #     print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    # return processes


def createProcessRandomly():
    p = int(input("Number of processes:- "))
    while p:
        at = rint(0, p)
        bt = rint(1, 20)
        if at < bt:
            process.processes.append(process(p, at, bt))
            p -= 1
    # for i in process.processes:
    #     print(f"{i.processID} {i.arrivalTime} {i.burstTime}")


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


def printData(queue, completionQ):
    avgW = 0
    avgC = 0
    avgT = 0
    head = [
        "Process ID", "Arrival time", "Burst time",
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
