
def sjf(processes):
    readyQueue = []
    global te
    te = 0
    completeQueue = []

    def complete(pro, processes):
        global te
        completeQueue.append(pro)
        te += pro.burstTime
        rmov = []
        for pro in processes:
            if pro.arrivalTime <= te:
                readyQueue.append(pro)
                rmov.append(pro)
        for pro in rmov:
            processes.remove(pro)

    processes.sort(key=lambda pro: pro.arrivalTime)
    readyQueue.append(processes.pop(0))
    complete(readyQueue.pop(0), processes)
    while len(readyQueue):
        readyQueue.sort(key=lambda pro: pro.burstTime)
        complete(readyQueue.pop(0), processes)
    for pro in completeQueue:
        if completeQueue.index(pro) == 0:
            pro.completionTime = pro.arrivalTime + pro.burstTime
            # ct-- completion time, it is to get the total completion time and calculate process ct according to it
            ct = pro.arrivalTime + pro.burstTime
        else:
            pro.completionTime = ct + pro.burstTime
            ct = pro.burstTime + ct

    return(completeQueue)


def sjfP(processes):
    readyQueue = []
    completeQueue = []
    global te
    te = 0

    def complete(pro, processes):
        global te
        # print("1")
        te += 1
        pro.remainingBurstTime -= 1
        completeQueue.append(pro)
        rmov = []
        if len(processes) > 0:
            for i in processes:
                if i.arrivalTime <= te:
                    readyQueue.append(i)
                    rmov.append(i)
            if len(rmov):
                for i in rmov:
                    processes.remove(i)
        if pro.remainingBurstTime > 0:
            readyQueue.append(pro)
        else:
            pro.completionTime = te

    # When two process have same arrival time it will sort according to burst time
    processes.sort(key=lambda pro: (pro.arrivalTime, pro.burstTime))
    readyQueue.append(processes.pop(0))
    # complete(processes.pop(0), processes)
    complete(readyQueue.pop(0), processes)
    while len(readyQueue) > 0:
        readyQueue.reverse()
        readyQueue.sort(key=lambda pro: pro.remainingBurstTime)
        complete(readyQueue.pop(0), processes)
    # queue = list(set(completeQ))
    return completeQueue
