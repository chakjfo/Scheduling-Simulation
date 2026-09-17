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
The program also implements **Banker's Algorithm** to determine whether the given system is in a safe or unsafe state.

As required by the activity, the Banker's Algorithm portion does **not require user input**. The matrices are already defined in the source code and the program displays only the required results:
- Need Matrix
- Safe or Unsafe State
- Safe Sequence, if the system is safe

For the included example, the expected safe sequence is:

```text
P1 -> P3 -> P4 -> P0 -> P2
```

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

- `main.py` — Python source code containing the scheduling algorithms and Banker's Algorithm.
- `README.md` — Instructions and explanation of the program.

The sample input/output file required for submission can be added separately after running the program with your chosen sample data.
