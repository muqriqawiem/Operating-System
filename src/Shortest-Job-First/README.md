<h1>SJF CPU Scheduling Algorithm</h1>

<h2>Introduction</h2>
<p>A non-preemptive CPU scheduling algorithm that selects the process with the shortest burst time for execution. It aims to minimize the average waiting time and provide faster response times for shorter jobs.</p>

<h2>Algorithm Review</h2>
<ul>
    <li>The SJF algorithm organizes the jobs in the system based on their CPU burst times.</li>
    <li>The jobs are arranged in ascending order, with the shortest burst time at the front of the queue.</li>
    <li>If two or more jobs have the same burst time, the First-Come, First-Served (FCFS) approach is followed to break the tie.</li>
</ul>

<h2>Pseudocode</h2>
<ol>
    <li>Read `num` as the number of processes</li>
    <li>Initialize empty lists `burst`, `wait`, `turn`, and `arrival`</li>
    <li>Initialize `total_wait` and `total_turn` to 0</li>
    <li>
        For `i` in range(`num`):
        <ol>
            <li>Read `arrival_time` from the user</li>
            <li>Read `burst_time` from the user</li>
            <li>Append `arrival_time` to the `arrival` list</li>
            <li>Append `burst_time` to the `burst` list</li>
        </ol>
    </li>
    <li>Append 0 to the `wait` list</li>
    <li>
        For `j` in range(1, `num`):
        <ol>
            <li>Calculate `wait_time` as `max(0, wait[j-1] + burst[j-1] - arrival[j])` (wait time can't be negative)</li>
            <li>Append `wait_time` to the `wait` list</li>
        </ol>
    </li>
    <li>
        For `k` in range(`num`):
        <ol>
            <li>Calculate `turn_time` as `burst[k] + wait[k]`</li>
            <li>Append `turn_time` to the `turn` list</li>
        </ol>
    </li>
    <li>Print "Processes   Burst time   Waiting time   Turn around time" for table header</li>
    <li>
        For `i` in range(`num`):
        <ol>
            <li>Add `wait[i]` to `total_wait`</li>
            <li>Add `turn[i]` to `total_turn`</li>
            <li>Print process number (`i+1`), `arrival[i]`, `burst[i]`, `wait[i]`, and `turn[i]` in a formatted table row</li>
        </ol>
    </li>
    <li>Calculate `average_wait` as `total_wait` divided by `num`</li>
    <li>Calculate `average_turn` as `total_turn` divided by `num`</li>
    <li>Print "Average waiting time = " concatenated with `average_wait` formatted to 3 decimal places</li>
    <li>Print "Average turn around time = " concatenated with `average_turn` formatted to 3 decimal places</li>
</ol>

<h2>Metrics</h2>
<ul>
    <li>Waiting Time: The time a process spends waiting in the ready queue before starting execution.</li>
    <li>Turnaround Time: The total time taken for a process to complete its execution, including waiting time and CPU execution time.</li>
</ul>

<h2>Implementation</h2>
<ul>
    <li>The SJF algorithm requires knowledge of the burst times of all processes.</li>
    <li>The burst times are used to prioritize the jobs in the ready queue.</li>
    <li>The algorithm calculates the waiting time and turnaround time for each process based on its burst time and position in the queue.</li>
</ul>