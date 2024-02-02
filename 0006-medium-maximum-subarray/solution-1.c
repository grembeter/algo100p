#include <stdio.h>
#include <stdlib.h>
#include <solution.h>


int max_subarray(int* buf, size_t len)
{
    int local_sum = buf[0];
    int global_sum = buf[0];
    int i;

    for (i = 1; i < len; ++i) {
        if (local_sum > 0) {
            local_sum += buf[i];
        } else {
            local_sum = buf[i];
        }
        if (local_sum > global_sum) {
            global_sum = local_sum;
        }
    }

    return global_sum;
}
