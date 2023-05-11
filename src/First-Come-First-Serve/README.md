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

<h2>Process Execution</h2>
<ul>
    <li>The CPU executes the process at the front of the queue.</li>
    <li>Once a process completes its execution, the next process in the queue is selected and executed.</li>
    <li>This continues until all processes have been executed.</li>
</ul>

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