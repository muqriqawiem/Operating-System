def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j

        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(n):
        print(f"{i+1}\t\t{processSize[i]}\t\t{allocation[i]+1 if allocation[i] != -1 else 'Not Allocated'}")


# Driver code
if __name__ == '__main__':
    m = int(input("Enter the number of blocks: "))
    blockSize = []
    for i in range(m):
        size = int(input(f"\nEnter the size of block {i+1}: "))
        blockSize.append(size)

    n = int(input("\nEnter the number of processes: "))
    processSize = []
    for i in range(n):
        size = int(input(f"\nEnter the size of process {i+1}: "))
        processSize.append(size)

    bestFit(blockSize, m, processSize, n)
