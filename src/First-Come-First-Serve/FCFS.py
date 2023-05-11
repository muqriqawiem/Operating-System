num = int(input("Number of processes: "))
burst = []
wait = []
turn = []
total_wait = 0
total_turn = 0

for i in range(num):
    burst_time = int(input("Enter the burst time for process " + str(i+1) + ": "))
    burst.append(burst_time)

wait.append(0)
for j in range(1, num):
    wait_time = burst[j-1] + wait[j-1]
    wait.append(wait_time)

for k in range(num):
    turn_time = burst[k] + wait[k]
    turn.append(turn_time)

print("Processes   Burst time   Waiting time   Turn around time")
for i in range(num):
    total_wait += wait[i]
    total_turn += turn[i]
    print(str(i+1).rjust(9), str(burst[i]).rjust(13), str(wait[i]).rjust(15), str(turn[i]).rjust(18))

total_wait /= num
total_turn /= num
print("Average waiting time = %.3f" % total_wait)
print("Average turn around time = %.3f" % total_turn)