# Scheduling Simulation

This is a simple Python program for our Operating Systems activity. It demonstrates CPU scheduling algorithms and Banker's Algorithm.

## Algorithms

- **FCFS** - Non-Preemptive Scheduling
- **Round Robin** - Preemptive Scheduling
- **Banker's Algorithm** - checks if the system is in a safe or unsafe state

## Inputs

For FCFS and Round Robin, enter the number of processes, arrival time, burst time, and time quantum for Round Robin.

For Banker's Algorithm, enter the number of processes, number of resources, Allocation Matrix, Maximum Matrix, and Available Resources.

## Output

The scheduling algorithms display the Gantt Chart, Average Waiting Time, and Average Turnaround Time. Banker's Algorithm displays the Need Matrix, system state, and Safe Sequence if available.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Choose an option from the menu and enter the requested values.
