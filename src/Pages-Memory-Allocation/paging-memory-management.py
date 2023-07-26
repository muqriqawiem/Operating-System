# Constants
PAGE_SIZE = 10  # Number of elements in each page
MEMORY_SIZE = 5  # Total number of frames in memory

# Function to initialize the page table
def initialize_page_table(processes):
    page_table = {}
    for process in processes:
        page_table[process] = []
    return page_table

# Function to initialize the memory frames
def initialize_memory():
    return [-1] * MEMORY_SIZE

# Function to load a page into memory
def load_page(page_table, memory, process, page_number):
    if page_number in page_table[process]:
        print(f"Page {page_number} of Process {process} is already in memory.")
        return

    if len(page_table[process]) >= MEMORY_SIZE:
        print(
            f"\nNot enough free memory for Process {process}. Page {page_number} cannot be loaded.")
        return

    frame_index = memory.index(-1)
    memory[frame_index] = (process, page_number)
    page_table[process].append(page_number)
    print(
        f"\nLoaded Page {page_number} of Process {process} into Memory Frame {frame_index}.")

# Function to access a memory location
def access_memory(page_table, memory, process, logical_address):
    page_number = logical_address // PAGE_SIZE
    offset = logical_address % PAGE_SIZE

    if page_number in page_table[process]:
        frame_index = memory.index((process, page_number))
        physical_address = (frame_index * PAGE_SIZE) + offset
        print(
            f"\nAccessing Logical Address {logical_address} of Process {process}. Physical Address: {physical_address}")
    else:
        print(f"\nPage {page_number} of Process {process} is not in memory.")

# Function to display the current state of memory and page tables
def display_state(page_table, memory):
    print("\nMemory:")
    for i, frame in enumerate(memory):
        if frame == -1:
            print(f"Frame {i}: Empty")
        else:
            process, page_number = frame
            print(f"Frame {i}: Process {process}, Page {page_number}")

    print("\nPage Tables:")
    for process, pages in page_table.items():
        print(f"Process {process}: {pages}")

# Main function
def main():
    processes = [1, 2, 3]  # List of processes

    # Initialize page table and memory
    page_table = initialize_page_table(processes)
    memory = initialize_memory()

    # Load pages into memory
    load_page(page_table, memory, 1, 0)
    load_page(page_table, memory, 2, 2)
    load_page(page_table, memory, 3, 1)
    load_page(page_table, memory, 1, 3)

    # Access memory locations
    access_memory(page_table, memory, 1, 10)
    access_memory(page_table, memory, 2, 6)
    access_memory(page_table, memory, 3, 13)
    access_memory(page_table, memory, 1, 2)

    # Display current state
    display_state(page_table, memory)


# Run main function
if __name__ == '__main__':
    main()
