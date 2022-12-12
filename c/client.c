#include"math.h"
#include<rpc/rpc.h>
#include<stdlib.h>

int main(int argc, char* argv[]) {
    char* servername = argv[1];
    int num1 = atoi(argv[2]);
    int num2 = atoi(argv[3]);
    struct intpair numbers;

    numbers.a = num1;
    numbers.b = num2;

    CLIENT* cl = clnt_create(servername, MATHPROG, MATHVERS, "tcp");
    if(cl == (CLIENT *)NULL) {
        printf("error");
        exit(1);
    }

    int* res1 = add_1(&numbers, cl);
    printf("Addition Ergebnis: %d\n", *(res1));

    int* res2 = multiply_1(&numbers, cl);
    printf("Multiplikation Ergebnis: %d\n", *(res2));

    int* res3 = cube_1(&num1, cl);
    printf("Quadrat Ergebnis von Arg2: %d\n", *(res3));

    return 0;
}
// cc -o remo_math math_clnt.c math_xdr.c client.c -lnsl