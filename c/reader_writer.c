#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int sem_id;
int total_sem = 3;
// sem1 = mutex(reader), sem2 = writer, sem3 = counter(reader)

void init_sem(int sem_id) {
    for(int i = 0; i < total_sem; i++) {
        if(semctl(sem_id, i, SETVAL, 1) < 0) {
            perror("semctl() error");
            exit(1);
        }
    }

    if(semctl(sem_id, 2, SETVAL, 0) < 0) {
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
    int var = 7;

    /* create semaphor set */
    // key
    key_t sem_key = ftok("/home/lars/Dokumente/vts", 7);
    if(sem_key < 0) {
        perror("ftok() error");
        exit(1);
    }

    // semaphor set
    sem_id = semget(sem_key, total_sem, IPC_CREAT|0666);
    if(sem_id < 0) {
        perror("sem_get() error");
        exit(1);
    }

    // init semaphor
    init_sem(sem_id);

    for(int i = 0; i < 7; i++) {
        // semaphore names
        int mutex = 0;
        int writer = 1;
        int reader = 2;

        pid_t pid  = fork();
        int own_id = i+1;

        if(pid == -1) {
            perror("Fork failed");
            printf("\n");
            exit(1);
        }
        
        if(pid == 0) {
            if(own_id <= 5) {
                printf("Fork successful. Im a new Reader. Own process number: %d | Unix proccess number: %ld", own_id, (long) getpid());
                printf("\n");

                for(int j = 0; j < 3; j++) {
                    P(mutex);
                        int counter = semctl(sem_id, reader, GETVAL);
                            if(semctl(sem_id, reader, SETVAL, counter+1) < 0) {
                                perror("semctl() error");
                                exit(1);
                            }
                        if(semctl(sem_id, reader, GETVAL) == 1) {
                            P(writer);
                        }
                    V(mutex);
                    
                    printf("Reading variable");
                    printf("\n");
                    sleep(1);
                    
                    P(mutex);
                        counter = semctl(sem_id, reader, GETVAL);
                            if(semctl(sem_id, reader, SETVAL, counter-1) < 0) {
                                perror("semctl() error");
                                exit(1);
                            }
                        if(semctl(sem_id, reader, GETVAL) == 0) {
                            V(writer);
                        }
                    V(mutex);
                }
            }

            if(own_id > 5) {
                printf("Fork successful. Im a new Writer. Own process number: %d | Unix proccess number: %ld", own_id, (long) getpid());
                printf("\n");

                for(int j = 0; j < 3; j++) {
                    P(writer);

                    printf("Writing variable");
                    printf("\n");
                    sleep(1);
                    
                    V(writer);
                }
            }

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