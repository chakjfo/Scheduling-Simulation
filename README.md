# Scheduling Simulation

A simple Python program for an Operating Systems activity that demonstrates CPU scheduling and deadlock avoidance.

## Algorithms Included

### CPU Scheduling
- **First Come First Serve (FCFS)** — Non-Preemptive
- **Round Robin** — Preemptive

For CPU scheduling, the program accepts console input for:
- Number of processes
- Arrival time of each process
- Burst time of each process
- Time quantum for Round Robin

The program displays:
- Gantt Chart / execution order
- Waiting time of each process
- Turnaround time of each process
- Average Waiting Time
- Average Turnaround Time

### Banker's Algorithm
The program implements **Banker's Algorithm** to check whether a system is in a safe or unsafe state.

The user enters:
- Number of processes
- Number of resource types
- Allocation matrix
- Maximum matrix
- Available resources

The program calculates the Need Matrix using:

```text
Need = Maximum - Allocation
```

It then displays:
- Need Matrix
- Whether the system is in a Safe State or Unsafe State
- Safe Sequence of processes, if one exists

> The submission instruction saying that only the Banker's Algorithm output is needed refers to the sample/screenshot for submission. The actual program still accepts all required Banker's Algorithm inputs from the user.

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal or command prompt inside the project folder.
3. Run:

```bash
python main.py
```

If your computer uses `python3`, run:

```bash
python3 main.py
```

## Program Menu

```text
=============================================
          OPERATING SYSTEM SIMULATOR
=============================================
1. FCFS Scheduling (Non-Preemptive)
2. Round Robin Scheduling (Preemptive)
3. Banker's Algorithm
4. Exit
```

Choose **1** for FCFS, **2** for Round Robin, **3** for Banker's Algorithm, or **4** to exit.

## Files

- `main.py` — Python source code containing FCFS, Round Robin, and Banker's Algorithm.
- `README.md` — Instructions and explanation of the program.

The sample input/output file required for submission can be added separately after running the program with your chosen sample data. For Banker's Algorithm, only its output/screenshot needs to be included in that submission evidence.
