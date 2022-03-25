def fcfs(processes):
    readyQueue = []
    completeQueue = []
    ct = 0
    processes.sort(key=lambda x: x.arrivalTime)
    for process in processes:
        completeQueue.append(process)
    for process in processes:
        if processes.index(process) == 0:
            process.completionTime = process.arrivalTime + process.burstTime
            ct = process.arrivalTime + process.burstTime
        else:
            process.completionTime = ct + process.burstTime
            ct = process.burstTime + ct
    return(completeQueue)
