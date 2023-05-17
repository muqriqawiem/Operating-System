<h1>Best-Fit Contiguous Memory Allocation</h1>

<h2>Introduction</h2>
<p>The code in this lab simulates the best-fit contiguous memory allocation strategy by using a list to represent the memory blocks. The list is initialized with all blocks set to 0, which indicates that they are not allocated. When the user enters a process size, the program checks each block in the list, starting from the beginning. If the block is not allocated and is large enough to accommodate the process, it is marked as allocated and the program continues to the next block. If the block is not allocated but is not large enough to accommodate the process, the program continues to the next block. If the block is allocated, the program prints an error message and asks the user to enter a new process size.</p>
<br>
<p>The program continues to allocate blocks until the user enters a process size of 0. When the user enters a process size of 0, the program prints a message indicating that all processes have been allocated to memory.</p>
<br>
<p>The program also allows the user to enter more processes. When the user enters 1 when prompted to enter more processes, the program prompts the user to enter a process size for the next process. If the user enters 0, the program exits.</p>

<h2>Pseudocode</h2>
<ol>
    <li>Initialize a list to represent the memory blocks.</li>
    <li>Set all blocks in the list to 0, which indicates that they are not allocated.</li>
    <li>
        Repeat the following steps until the user enters a process size of 0:
        <ul>
            <li>Get the process size from the user.</li>
            <li>Find the first free block of memory that is large enough to accommodate the process.</li>
            <li> 
                If a free block is found:
                <ul>
                    <li>Mark the block as allocated.</li>
                    <li>Print a message indicating that the block has been allocated.</li>
                    <li>Break.</li>
                </ul>
            </li>
            <li>
                Otherwise:
                <ul>
                    <li>Print a message indicating that the process cannot be allocated.</li>
                </ul>
            </li>
            <li>
                If the user enters a process size of 0:
                <ul>
                    <li>Print a message indicating that all processes have been allocated to memory.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Ask the user if they want to enter more processes.</li>
    <li>
        If the user enters 1:
        <ul>
            <li>Repeat the above steps.</li>
        </ul>
    </li>
    <li>
        Otherwise:
        <ul>
            <li>Exit the program</li>
        </ul>
    </li>
</ol>    

<h2>Example Output</h2>
```
    $ python best_fit_memory_allocation.py

    Enter the number of blocks: 10

    Enter the size of block 1: 10

    Enter the size of block 2: 15

    Enter the size of block 3: 12

    Enter the size of block 4: 13

    Enter the size of block 5: 14

    Enter the size of block 6: 15

    Enter the size of block 7: 10

    Enter the size of block 8: 11

    Enter the size of block 9: 12

    Enter the size of block 10: 13

    Enter the number of processes: 5

    Enter the size of process 1: 10

    Block 0 allocated.
    Block 1 allocated.
    Block 2 allocated.
    Block 3 allocated.
    Block 4 allocated.

    Enter the size of process 2: 15

    Block 5 allocated.
    Block 6 allocated.
    Block 7 allocated.
    Block 8 allocated.

    Enter the size of process 3: 12

    Block 9 allocated.
    Block 10 allocated.

    Enter the size of process 4: 13

    The process size is too large. Please enter a smaller process size.

    Enter the size of process 5: 0

    All processes have been allocated to memory.

    Do you want to enter more processes? ( 1 for YES, 0 for NO ): 0

    See you again.