#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int sem_id;
int total_sem = 5;

void init_sem(int sem_id) {
    for(int i = 0; i < total_sem; i++) {
        if(semctl(sem_id, i, SETVAL, 1) < 0) {
            perror("semctl() error");
            exit(1);
        }
    }
}

void P(int sem_num1, int sem_num2) {
    struct sembuf semaphore[2];
    semaphore[0].sem_num= sem_num1;
    semaphore[0].sem_op= -1;
    semaphore[0].sem_flg=~(IPC_NOWAIT|SEM_UNDO);

    semaphore[1].sem_num= sem_num2;
    semaphore[1].sem_op= -1;
    semaphore[1].sem_flg=~(IPC_NOWAIT|SEM_UNDO);

    if(semop(sem_id, semaphore, 2)){ 
        ("semopP() error");
        exit(1);
    }
}

void V(int sem_num1, int sem_num2) {
    struct sembuf semaphore[2];
    semaphore[0].sem_num= sem_num1;
    semaphore[0].sem_op= 1;
    semaphore[0].sem_flg=~(IPC_NOWAIT|SEM_UNDO);

    semaphore[1].sem_num= sem_num2;
    semaphore[1].sem_op= 1;
    semaphore[1].sem_flg=~(IPC_NOWAIT|SEM_UNDO);

    if(semop(sem_id, semaphore, 2)){ 
        ("semopV() error");
        exit(1);
    }
}

int main() {
    /* create semaphor set */
    // key
    key_t sem_key = ftok("/home/lars/Dokumente/vts", 1);
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

    for(int i = 0; i < 5; i++) {
        pid_t pid  = fork();
        int own_id = i+1;

        if(pid == -1) {
            perror("Fork failed");
            printf("\n");
            exit(1);
        }
        
        if(pid == 0) {
            printf("Fork successful. Own process number: %d | Unix proccess number: %ld", own_id, (long) getpid());
            printf("\n");

            for(int j = 0; j < 1; j++) {
                /* enter critical section */
                P((own_id-1), own_id%5);
                printf("Philosoph %d isst Spaghetti", own_id);
                printf("\n");
                sleep((rand() % (10 + 1 - 2)) + 2);
                printf("Philosoph %d hört auf Spaghetti zu essen", own_id);
                printf("\n");
                V((own_id-1), own_id%5);
                /* leave critical section */
                
                /* enter UNcritical section */
                printf("Philosoph %d denkt nach", own_id);
                printf("\n");
                sleep((rand() % (10 + 1 - 2)) + 2);
                printf("Philosoph %d hört auf zu denken", own_id);
                printf("\n");
                /* leave UNcritical section */
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