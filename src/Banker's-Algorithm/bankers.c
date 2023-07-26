#include <stdio.h>

#define MAX_PROCESSES 10
#define MAX_RESOURCES 10

int available[MAX_RESOURCES];
int max[MAX_PROCESSES][MAX_RESOURCES];
int allocation[MAX_PROCESSES][MAX_RESOURCES];
int need[MAX_PROCESSES][MAX_RESOURCES];
int safe_sequence[MAX_PROCESSES];

int processes, resources;

void input_data()
{
    int i, j;

    printf("Enter the number of processes: ");
    scanf("%d", &processes);

    printf("Enter the number of resources: ");
    scanf("%d", &resources);

    printf("Enter the available resources: ");
    for (i = 0; i < resources; i++)
    {
        scanf("%d", &available[i]);
    }

    printf("Enter the maximum resources required for each process: \n");
    for (i = 0; i < processes; i++)
    {
        printf("For process P%d: ", i);
        for (j = 0; j < resources; j++)
        {
            scanf("%d", &max[i][j]);
        }
    }

    printf("Enter the allocated resources for each process: \n");
    for (i = 0; i < processes; i++)
    {
        printf("For process P%d: ", i);
        for (j = 0; j < resources; j++)
        {
            scanf("%d", &allocation[i][j]);
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }
}

int is_process_executable(int process)
{
    int i;
    for (i = 0; i < resources; i++)
    {
        if (need[process][i] > available[i])
        {
            return 0;
        }
    }
    return 1;
}

void execute_process(int process)
{
    int i;
    for (i = 0; i < resources; i++)
    {
        available[i] += allocation[process][i];
        allocation[process][i] = 0;
        need[process][i] = 0;
    }
    safe_sequence[process] = 1;
}

void bankers_algorithm()
{
    int i, j;
    int executed_processes = 0;
    int is_executable;

    while (executed_processes < processes)
    {
        is_executable = 0;
        for (i = 0; i < processes; i++)
        {
            if (safe_sequence[i])
            {
                continue;
            }
            if (is_process_executable(i))
            {
                execute_process(i);
                is_executable = 1;
                executed_processes++;
            }
        }
        if (!is_executable)
        {
            break;
        }
    }

    if (executed_processes == processes)
    {
        printf("Safe sequence found: ");
        for (i = 0; i < processes; i++)
        {
            printf("P%d ", i);
        }
        printf("\n");
    }
    else
    {
        printf("Deadlock detected\n");
    }
}

int main()
{
    input_data();
    bankers_algorithm();
    return 0;
}