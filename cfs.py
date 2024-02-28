import random
import sys
import os
import time

SCHED_COLOR = '\033[92m'
RUNNABLE_COLOR = '\033[93m'
RESET = '\033[0m'

def sfair(processes: dict[str:int]) -> tuple:
    """Defining next schedule"""

    # Choosing runnable processes randomly
    n_of_runnables: int = random.randint(1, len(processes))
    runnable: list[str] = random.sample(list(processes.keys()), n_of_runnables)
    
    min_value: int = None;
    candidates: list[str] = [];

    # Figuring out, what processes from candidates have the lowest weight
    for p in runnable:
        if min_value is None or processes[p] < min_value:
            min_value = processes[p]
            candidates = [p]
        elif min_value == processes[p]:
            candidates.append(p)

    # Choosing random process from those, who have lowest weight
    to_sched: str = random.choice(candidates)

    # returning the name of the process to be scheduled and a list of runnables
    return to_sched, runnable

def apply(to_sched: str, 
          runnables: list[str], 
          processes: dict[str:int]) -> None:
    """Applying next schedule"""

    # Choosing random weight for the scheduled process
    processes[to_sched] = random.randint(0, MAX_WEIGHT);

    # Decreasing values of all runnable processes that are not to schedule
    for p in runnables:
        if p == to_sched: continue
        else: processes[p] -= 1

def printout(to_sched: str, 
             runnable: list[str], 
             processes: dict[str:int]) -> None:
    """ Print out the next sched """

    os.system("clear");
    print(f'Legend: {RUNNABLE_COLOR}RUNNABLE{RESET} {SCHED_COLOR}BEING SCHEDULED{RESET}\n')

    print(f'{"{:^14}".format("PROCESSES")}{" " * (-MIN_WEIGHT - 4)}WEIGHTS')
    for p in processes:
        weight: int = processes[p] 
        neg: int = -weight if weight < 0 else 0
        pos: int = weight if weight > 0 else 0

        if p == to_sched: 
            print(f"{SCHED_COLOR}{p} {'{:^10}'.format(weight)}: {'_' * (-MIN_WEIGHT - neg)}{'#' * neg}{'#' * pos}{RESET}")
        elif p in runnable: 
            print(f"{RUNNABLE_COLOR}{p} {'{:^10}'.format(weight)}: {'_' * (-MIN_WEIGHT - neg)}{'#' * neg}{'#' * pos}{RESET}") 
        else: 
            print(f"{p} {'{:^10}'.format(weight)}: {'_' * (-MIN_WEIGHT - neg)}{'#' * neg}{'#' * pos}")

if __name__ == '__main__':
    # Checking args -------
    if len(sys.argv) < 2:
        print("Usage: python3 cfs.py [N_OF_PROCESSES] [MAX_WEIGHT (optional, default - N_OF_PROCESSES * 2)]")
        exit(1)

    N_PROCESSES = int(sys.argv[1]);
    if 26 < N_PROCESSES or N_PROCESSES < 1: 
        print("Number of Processes must be 1 < n < 26!")
        exit(1)
    
    if len(sys.argv) == 3:
        MAX_WEIGHT = int(sys.argv[2]);
        if MAX_WEIGHT < 0: 
            print("Max weigth cannot be negative!")
            exit(1)
    else:
        MAX_WEIGHT = N_PROCESSES * 2

    MIN_WEIGHT = -MAX_WEIGHT - N_PROCESSES + 1
    # -------

    # Creating N_PROCESSES threads and assigning them random weights
    processes: dict[str:int] = {chr(ord('A') + i): random.randint(0, MAX_WEIGHT) 
                                for i in range(N_PROCESSES)}

    while True:
        to_sched, runnable = sfair(processes)
        printout(to_sched, runnable, processes)
        print("SCHEDULE IS BEING PERFORMED!")

        time.sleep(1)

        apply(to_sched, runnable, processes)
        printout(to_sched, runnable, processes)

        print("PROCESS IS RUNNING NOW!")
        time.sleep(3)
