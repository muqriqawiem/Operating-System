# Function to allocate memory to
def firstFit(blockSize, m, processSize, n):
    # block allocated to a process
    allocation = [-1] * n

    # Flag to indicate if a block is already allocated
    blockAllocated = [False] * m

    # Initially no block is assigned to any process
    # pick each process and find suitable blocks
    # according to its size and assign to it
    for i in range(n):
        for j in range(m):
            if not blockAllocated[j] and blockSize[j] >= processSize[i]:
                # allocate block j to p[i] process
                allocation[i] = j
                blockAllocated[j] = True
                # Reduce available memory in this block.
                blockSize[j] -= processSize[i]
                break

    print("\nProcess No.     Process Size	   Block no.")
    for i in range(n):
        print(" ", i + 1, "		   ", processSize[i],
            "		      ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]  # length of array indicates how many blocks
    processSize = [212, 417, 112, 426]  # length of array indicates how many process
    print("\nThere are " + str(len(blockSize)) + " blocks. The size of blocks are:- ")
    j = 1
    for i in blockSize:
        print("Block " + str(j) + " = " + str(i) + "\n", end="")
        j += 1
    m = len(blockSize)
    n = len(processSize)

    firstFit(blockSize, m, processSize, n)
