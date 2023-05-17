def main():
    f = [0] * 50

    while True:
        print("Please enter the starting block and length of the file you want to allocate.")
        print("The blocks are numbered from 0 to 49.")
        print("If a block is already allocated, you will be prompted to enter a new file.")
        print("To exit the program, enter 0 when prompted to enter more files.")

        st, len_ = map(int, input("\nEnter the starting block and length ( separated by a SPACE ): ").split())

        for j in range(st, st + len_):
            if f[j] == 0:
                f[j] = 1
                print(f"Block {j} allocated.")
            else:
                print(f"Block {j} is already allocated.")
                break

        if j == (st + len_ - 1):
            print("The file is allocated to disk.")

        c = int(input("\nDo you want to enter more files? ( 1 for YES, 0 for NO ): "))

        if c == 0:
            print("\nSee you again.")
            break


if __name__ == "__main__":
    main()