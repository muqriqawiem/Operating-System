<h1>FCFS CPU Scheduling Algorithm</h1>

<h2>Introduction</h2>
<ul>
    <li>This repository provides a program that implements the FCFS scheduling algorithm.</li>
    <li>The program calculates the waiting time and turnaround time for a given set of processes.</li>
</ul>

<h2>Algorithm Overview</h2>
<ul>
    <li>FCFS operates on the principle of executing processes based on their arrival time, regardless of other parameters.</li>
    <li>Each process is assigned a CPU burst time, representing the time required for its execution.</li>
    <li>Processes are executed in the order of their arrival, forming a queue.</li>
</ul>

<h2>Pseudocode</h2>
<ol>
    <li>Read `num` as the number of processes</li>
    <li>Initialize empty lists `burst`, `wait`, and `turn`</li>
    <li>Initialize `total_wait` and `total_turn` to 0</li>
    <li>
        For `i` in range(`num`):
        <ul>
            <ol>Read `burst_time` from the user</ol>
            <ol>Append `burst_time` to the `burst` list</ol>
        </ul>
    </li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ol>

<h2>Metrics</h2>
<ul>
    <li>Waiting Time: The time a process spends waiting in the ready queue before starting execution.</li>
    <li>Turnaround Time: The total time taken for a process to complete its execution, including waiting time and CPU execution time.</li>
</ul>

<h2>Characteristics</h2>
<ul>
    <li>FCFS scheduling does not consider differences in execution times or priorities among processes.</li>
    <li>Long-running processes arriving first can result in longer waiting times for subsequent shorter processes.</li>
    <li>Resource utilization may be inefficient in certain cases.</li>
</ul>