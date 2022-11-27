#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int sem_id;

void init_sem(int sem_id) {
    if(semctl(sem_id, 0, SETVAL, 1) < 0) {
        perror("semctl() error");
        exit(1);
    }
}

void P(int sem_num) {
    struct sembuf semaphore;
    semaphore.sem_num= sem_num;
    semaphore.sem_op= -1;
    semaphore.sem_flg=~(IPC_NOWAIT|SEM_UNDO);

    if(semop(sem_id, &semaphore, 1)){ 
        ("semopP() error");
        exit(1);
    }
}

void V(int sem_num) {
    struct sembuf semaphore;
    semaphore.sem_num= sem_num;
    semaphore.sem_op= 1;
    semaphore.sem_flg=~(IPC_NOWAIT|SEM_UNDO);

    if(semop(sem_id, &semaphore, 1)){ 
        ("semopV() error");
        exit(1);
    }
}

int main() {
    /* create semaphor set */
    // key
    key_t sem_key = ftok("/home/lars/Dokumente/vts", 0);
    if(sem_key < 0) {
        perror("ftok() error");
        exit(1);
    }

    // semaphor set
    int sem_id = semget(sem_key, 1, IPC_CREAT|0666);
    if(sem_id < 0) {
        perror("sem_get() error");
        exit(1);
    }

    // init semaphor
    init_sem(sem_id);

    for(int i = 0; i < 3; i++) {
        pid_t pid  = fork();

        if(pid == -1) {
            perror("Fork failed");
            printf("\n");
            exit(1);
        }
        
        if(pid == 0) {
            printf("Fork successful. Own process number: %d | Unix proccess number: %ld", i, (long) getpid());
            printf("\n");

            /* enter critical section */
            struct sembuf semaphore;
            P(0);
            printf("Prozess %d betritt kritischen Bereich", i);
            printf("\n");
            sleep(1);
            printf("Prozess %d verlässt kritischen Bereich", i);
            printf("\n");
            V(0);
            /* leave critical section */
            
            /* enter UNcritical section */
            printf("Prozess %d betritt NICHT-kritischen Bereich", i);
            printf("\n");
            sleep(1);
            printf("Prozess %d verlässt NICHT-kritischen Bereich", i);
            printf("\n");
            /* leave UNcritical section */

            exit(0);
        }
    }

    wait(NULL);
    wait(NULL);
    wait(NULL);
    printf("Father");
    printf("\n");
    exit(0);
}