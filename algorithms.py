class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=None, remaining_time=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = remaining_time if remaining_time is not None else burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0


def fcfs_scheduling(processes):
    """First Come First Serve scheduling"""
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes by arrival time
    current_time = 0
    for process in processes:
        process.waiting_time = max(0, current_time - process.arrival_time)
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time
        process.completion_time = current_time


def round_robin_scheduling(processes, time_quantum):
    """Round Robin scheduling"""
    current_time = 0
    queue = []
    remaining_processes = processes.copy()  # Make a copy of processes list for round robin
    
    while remaining_processes:
        for process in remaining_processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                queue.append(process)

        if queue:
            process = queue.pop(0)

            if process.remaining_time > time_quantum:
                process.remaining_time -= time_quantum
                current_time += time_quantum
                queue.append(process)  # Add the process back to the queue if not finished
            else:
                current_time += process.remaining_time
                process.remaining_time = 0  # Process is finished
                process.turnaround_time = current_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                process.completion_time = current_time
                
        else:
            current_time += 1  # Increment time if no process is available to execute


def priority_scheduling(processes):
    """Priority Scheduling"""
    processes.sort(key=lambda x: (x.priority, x.arrival_time))  # Sort by priority and arrival time
    current_time = 0
    for process in processes:
        process.waiting_time = max(0, current_time - process.arrival_time)
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time
        process.completion_time = current_time
