#include"math.h"
#include<rpc/rpc.h>

int* add_1_svc(intpair* pair, struct svc_req* rqstp) {
    static int res;
    res = pair->a + pair->b;
    return &res;
}

int* multiply_1_svc(intpair* pair, struct svc_req* rqstp) {
    static int res;
    res = pair->a * pair->b;
    return &res;
}

int* cube_1_svc(int* num, struct svc_req* rqstp) {
    static int res;
    res = *(num) * *(num);
    return &res;
}