
from processes import createProcess
from processes import process as p
from processes import printData
from fcfs import fcfs
from sjf import sjf
from sjf import sjfP
from rr import roundRobin
from priority import mainP


def main():
    flag = 1

    while flag:
        print("\n\t ========|| CPU Scheduling Simulator ||======== \n")
        print("\t Select CPU Scheduling Algorithm:")
        print("\t 1. First Come First Serve ")
        print("\t 2. Shortest Job First(Non-preemptive) ")
        print("\t 3. Shortest Remaining Time First(Preemptive) ")
        print("\t 4. Round Robin ")
        print("\t 5. Priority Scheduling ")
        print("\t 6. Exit")
        print()
        choice = int(input("Enter Your Choice :- "))
        if choice < 6:
            if choice == 0:
                flag = 0
                break
            else:
                if choice == 1:
                    # First Come First Serve Algorithm
                    print("Executing FCFS\n")
                    createProcess()
                    fcfs1 = fcfs(p.processes)
                    printData(fcfs1, fcfs1)
                elif choice == 2:
                    # Shortest Job First Algorithm
                    print("Executing SJF\n")
                    createProcess()
                    sjf1 = sjf(p.processes)
                    printData(sjf1, sjf1)
                elif choice == 3:
                    # Shortest Remaining Time First
                    print("Executing SRTF\n")
                    createProcess()
                    sjf2 = sjfP(p.processes)
                    printData(list(set(sjf2)), sjf2)
                elif choice == 4:
                    # Round Robin Algorithm
                    print("Executing RR\n")
                    createProcess()
                    rr1 = roundRobin(p.processes)
                    rrC = list(set(rr1))
                    rrC.sort(key=lambda x: x.processID)
                    printData(rrC, rr1)
                elif choice == 5:
                    # Priority Scheduling Algorithm
                    print("Executing Priority Scheduling")
                    mainP()
                elif choice == 6:
                    # Exit
                    print("Exitting Simulator...")
                    break
                    quit()
        else:
            print("Incorrect Choice! Please try again")
        p.processes.clear()


main()
