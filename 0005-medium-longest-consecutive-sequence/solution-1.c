#include <stdio.h>
#include <stdlib.h>
#include <solution.h>


int longest(int* buf, size_t len)
{
    int *a = calloc(len, sizeof(a[0]));
    int nmax = 0;

    a[0] = 1;

    for (int i = 1; i < len; ++i) {
        a[i] = 1;

        for (int j = 0; j < i; ++j) {
            if (buf[j] < buf[i]) {
                if (a[i] < a[j] + 1) {
                    a[i] = a[j] + 1;
                }
            }
        }

        if (nmax < a[i]) {
            nmax = a[i];
        }
    }

    free(a);

    return nmax;
}
