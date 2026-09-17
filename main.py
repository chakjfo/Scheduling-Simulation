from collections import deque


def get_processes():
    """Get process arrival and burst times from the user."""
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        arrival = int(input(f"Enter arrival time for P{i}: "))
        burst = int(input(f"Enter burst time for P{i}: "))
        processes.append({"pid": f"P{i}", "arrival": arrival, "burst": burst})

    return processes


def display_results(title, processes, gantt, completion):
    """Display Gantt chart, waiting times, turnaround times, and averages."""
    print(f"\n{title}")
    print("\nGantt Chart:")

    for pid, start, end in gantt:
        print(f"| {pid} ", end="")
    print("|")

    if gantt:
        print(gantt[0][1], end="")
        for _, _, end in gantt:
            print(f" -> {end}", end="")
        print()

    total_waiting = 0
    total_turnaround = 0

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    for p in processes:
        turnaround = completion[p["pid"]] - p["arrival"]
        waiting = turnaround - p["burst"]
        total_waiting += waiting
        total_turnaround += turnaround
        print(f'{p["pid"]}\t{p["arrival"]}\t{p["burst"]}\t{waiting}\t{turnaround}')

    print(f"\nAverage Waiting Time: {total_waiting / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_turnaround / len(processes):.2f}")


def fcfs():
    """First Come First Serve: a non-preemptive CPU scheduling algorithm."""
    processes = get_processes()
    ordered = sorted(processes, key=lambda p: (p["arrival"], int(p["pid"][1:])))

    time = 0
    gantt = []
    completion = {}

    for p in ordered:
        # CPU stays idle if the next process has not arrived yet.
        if time < p["arrival"]:
            gantt.append(("Idle", time, p["arrival"]))
            time = p["arrival"]

        start = time
        time += p["burst"]
        gantt.append((p["pid"], start, time))
        completion[p["pid"]] = time

    display_results("FCFS SCHEDULING", processes, gantt, completion)


def round_robin():
    """Round Robin: a preemptive CPU scheduling algorithm."""
    processes = get_processes()
    quantum = int(input("Enter time quantum: "))

    if quantum <= 0:
        print("Time quantum must be greater than 0.")
        return

    ordered = sorted(processes, key=lambda p: (p["arrival"], int(p["pid"][1:])))
    remaining = {p["pid"]: p["burst"] for p in processes}
    completion = {}
    ready_queue = deque()
    gantt = []

    time = 0
    index = 0

    while len(completion) < len(processes):
        # Add all processes that have arrived to the ready queue.
        while index < len(ordered) and ordered[index]["arrival"] <= time:
            ready_queue.append(ordered[index])
            index += 1

        # If no process is ready, move time to the next arrival.
        if not ready_queue:
            next_arrival = ordered[index]["arrival"]
            gantt.append(("Idle", time, next_arrival))
            time = next_arrival
            continue

        process = ready_queue.popleft()
        pid = process["pid"]
        execution_time = min(quantum, remaining[pid])
        start = time
        time += execution_time
        remaining[pid] -= execution_time
        gantt.append((pid, start, time))

        # Processes arriving during this time slice enter the queue first.
        while index < len(ordered) and ordered[index]["arrival"] <= time:
            ready_queue.append(ordered[index])
            index += 1

        if remaining[pid] > 0:
            ready_queue.append(process)
        else:
            completion[pid] = time

    display_results("ROUND ROBIN SCHEDULING", processes, gantt, completion)


def bankers_algorithm():
    print("\nBANKER'S ALGORITHM")

    # Get number of processes and resources
    num_processes = int(input("Enter number of processes: "))
    num_resources = int(input("Enter number of resources: "))

    # Input Allocation Matrix
    allocation = []

    print("\nEnter Allocation Matrix:")
    print(f"Enter {num_resources} values separated by spaces.")

    for i in range(num_processes):
        while True:
            row = list(map(int, input(f"P{i}: ").split()))

            if len(row) == num_resources:
                allocation.append(row)
                break
            else:
                print(f"Please enter exactly {num_resources} values.")

    # Input Maximum Matrix
    maximum = []

    print("\nEnter Maximum Matrix:")
    print(f"Enter {num_resources} values separated by spaces.")

    for i in range(num_processes):
        while True:
            row = list(map(int, input(f"P{i}: ").split()))

            if len(row) == num_resources:
                maximum.append(row)
                break
            else:
                print(f"Please enter exactly {num_resources} values.")

    # Input Available Resources
    while True:
        available = list(
            map(
                int,
                input(
                    f"\nEnter Available Resources "
                    f"({num_resources} values): "
                ).split()
            )
        )

        if len(available) == num_resources:
            break
        else:
            print(f"Please enter exactly {num_resources} values.")

    # Calculate Need Matrix
    # Need = Maximum - Allocation
    need = []

    for i in range(num_processes):
        row = []

        for j in range(num_resources):
            row.append(maximum[i][j] - allocation[i][j])

        need.append(row)

    # Display Need Matrix
    print("\nNeed Matrix:")

    for i in range(num_processes):
        print(f"P{i}: {need[i]}")

    # Banker's Safety Algorithm
    work = available.copy()
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:

        process_found = False

        for i in range(num_processes):

            # Check if process is unfinished
            if not finish[i]:

                can_execute = True

                # Check if Need <= Available/Work
                for j in range(num_resources):
                    if need[i][j] > work[j]:
                        can_execute = False
                        break

                # If process can execute
                if can_execute:

                    # Release allocated resources
                    for j in range(num_resources):
                        work[j] += allocation[i][j]

                    finish[i] = True
                    safe_sequence.append(i)
                    process_found = True

        # If no process can execute,
        # the system is unsafe
        if not process_found:
            break

    # Display result
    if len(safe_sequence) == num_processes:

        print("\nSystem is in a Safe State.")

        print(
            "Safe Sequence: "
            + " -> ".join(f"P{i}" for i in safe_sequence)
        )

    else:

        print("\nSystem is in an Unsafe State.")
        print("No Safe Sequence exists.")

def main():
    """Main menu for the Operating System scheduling simulator."""
    while True:
        print("\n" + "=" * 45)
        print("          OPERATING SYSTEM SIMULATOR")
        print("=" * 45)
        print("1. FCFS Scheduling (Non-Preemptive)")
        print("2. Round Robin Scheduling (Preemptive)")
        print("3. Banker's Algorithm")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            fcfs()
        elif choice == "2":
            round_robin()
        elif choice == "3":
            bankers_algorithm()
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
