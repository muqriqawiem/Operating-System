<h1>Sequential File Allocation Simulation</h1>

<h2>Objective</h2>
<p>The objective of this program is to simulate sequential file allocation, where files are stored one after another on disk. Users can allocate files by specifying the starting block and length of each file.</p>

<h2>Introduction</h2>
<p>A file is a collection of data that is typically stored on a disk. File organization refers to the way data is stored within a file and how it can be accessed. In this program, we focus on sequential file allocation, where files are stored sequentially both physically and logically.</p>
<br>
<p>The provided Python code demonstrates sequential file allocation. It prompts the user to enter the starting block and length of the file they want to allocate. If the blocks are available, the program marks them as allocated. If any block in the specified range is already allocated, the program prompts the user to enter a new file. The program continues until the user chooses to exit.</p>

<h2>Pseudocode</h2>
<ol>
    <li>Initialize a list to represent the disk blocks.</li>
    <li>Set all blocks in the list to 0, which indicates that they are not allocated.</li>
    <li>
        Repeat the following steps until the user enters a length of 0:
        <ul>
            <li>Get the starting block and length from the user.</li>
            <li> 
                For each block from the starting block to the starting block + length - 1:
                <ul>
                    <li>
                        If the block is not allocated:
                        <ul>
                            <li>Mark the block as allocated.</li>
                            <li>Print a message indicating that the block has been allocated.</li>
                        </ul>
                    </li>
                    <li>
                        Otherwise:
                        <ul>
                            <li>Print an error message and ask the user to enter a new starting block.</li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li>
                If the user enters a length of 0:
                <ul>
                    <li>Print a message indicating that the file has been allocated to disk.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Ask the user if they want to enter more files.</li>
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
    $ python sequential_file_allocation.py

    Please enter the starting block and length of the file you want to allocate.
    The blocks are numbered from 0 to 49.
    If a block is already allocated, you will be prompted to enter a new file.
    To exit the program, enter 0 when prompted to enter more files.

    Enter the starting block and length ( separated by a SPACE ): 0 5
    Block 0 allocated.
    Block 1 allocated.
    Block 2 allocated.
    Block 3 allocated.
    Block 4 allocated.
    Block 5 allocated.
    The file is allocated to disk.

    Do you want to enter more files? ( 1 for YES, 0 for NO ): 1

    Please enter the starting block and length of the file you want to allocate.
    The blocks are numbered from 0 to 49.
    If a block is already allocated, you will be prompted to enter a new file.
    To exit the program, enter 0 when prompted to enter more files.

    Enter the starting block and length ( separated by a SPACE ): 10 3
    Block 10 allocated.
    Block 11 allocated.
    Block 12 allocated.
    The file is allocated to disk.

    Do you want to enter more files? ( 1 for YES, 0 for NO ): 0

    See you again.
```