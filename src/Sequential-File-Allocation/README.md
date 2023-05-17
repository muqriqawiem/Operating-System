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
