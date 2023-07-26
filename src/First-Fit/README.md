<h1>First Fit Algorithm</h1>

<h2>Introduction</h2>
<ul>
    <li>The First Fit algorithm is a strategy for allocating memory in operating systems.</li>
    <li>It operates by dividing memory into several fixed-sized partitions.</li>
    <li>Each partition is capable of containing a single process.</li>
</ul>

<h2>Algorithm Overview</h2>
<ul>
    <li>When a partition is available, a process is selected from the input queue and loaded into it.</li>
    <li>Once the process terminates, the partition becomes free for another process to occupy.</li>
    <li>The operating system maintains a table that indicates the availability of memory partitions.</li>
    <li>When a new process arrives and requires memory, the operating system provides a memory section that is large enough to accommodate it.</li>
    <li>If multiple free blocks of memory are available, the operating system must decide which block to allocate.</li>
    <li>The First Fit strategy selects the first available block that meets the size requirements.</li>
</ul>

<h2>Pseudocode</h2>
<ol>
    <li>
        For each process in the input queue:
        <ol>
            <li>
                For each block in memory:
                <ol>
                    <li>if block is not allocated and block size >= process size:</li>
                    <ol>
                        <li>allocate block to process</li>
                        <li>reduce available memory in this block</li>
                        <li>break</li>
                    </ol>
                </ol>
            </li>
        </ol>
    </li>
</ol>

<h2>Metrics & Characteristics</h2>
<ul>
    <li>The First Fit algorithm is straightforward to implement.</li>
    <li>It can be time-efficient.</li>
    <li>However, it may result in memory fragmentation over time.</li>
    <li>Small blocks of free memory may remain between allocated blocks.</li>
</ul>