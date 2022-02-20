from random import choice
from prettytable import PrettyTable
import fcfs
import sjf
import sjf_p
import rr

# def switcher(choice):
#     switch = {
#         1: "fcfs",
#         2: "sjf_np",
#         3: "sjf_p",
#         4: "round_robin"
#         # 5: "priority_scheduling"
#     }
#     return switch.get(choice, "Invalid Choice")


# Common for all algorithms
# Initializing variables
num = 0
process_lst = []
process_names = []
arrival_time = 0
burst_time = 0
average_WT = 0
average_TAT = 0
average_CT = 0

if __name__ == "__main__":
    print("\n SIMULATION OF CPU SCHEDULING ALGORITHM")
    print(" Menu:")
    print(" 1. FCFS")
    print(" 2. SJF")
    print(" 3. SJF with Preemption")
    print(" 4. Round Robin")
    print(" 5. Exit")
    choice = input(" Select: ")

    flag = True
    while flag:
        if choice == "1" or choice == "FCFS".lower():
            print("Running FCFS Algorithm...")
            fcfs.run()
        elif choice == "2" or choice == "SJF".lower():
            print("Running SJF Algorithm...")
            sjf.run()
        elif choice == "3" or choice == "SJF with Preemption".lower():
            print("Running SJF with Preemption Algorithm...")
            sjf_p.run()
        elif choice == "4" or choice == "Round Robin".lower():
            print("Running Round Robbin Algorithm...")
            rr.run()
        elif choice == "5" or choice == "Exit".lower():
            print("Exiting...")
            break
            quit()
        else:
            print("Incorrect choice! Please try again")
            break
