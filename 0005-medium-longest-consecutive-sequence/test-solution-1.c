#include <stdio.h>
#include <stdlib.h>
#include <solution.h>

#define ARRAY_COUNT(x) (sizeof(x)/sizeof(x[0]))

static void print_buf(const int *buf, size_t len)
{
    size_t i;

    for (i = 0; i < len; ++i) {
        printf("%d ", buf[i]);
    }

    printf("\n");
}

static int test_1(void)
{
    int buf[] = {3, 10, 3, 11, 4, 5, 6, 7, 8, 12};
    int wanted = 7;
    int total = longest(buf, ARRAY_COUNT(buf));

    if (wanted == total) {
        printf("PASS: wanted(%d) == got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 0;
    } else {
        printf("FAIL: wanted(%d) != got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 1;
    }
}

static int test_2(void)
{
    int buf[] = {3, 0, 2, 0, 4};
    int wanted = 3;
    int total = longest(buf, ARRAY_COUNT(buf));

    if (wanted == total) {
        printf("PASS: wanted(%d) == got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 0;
    } else {
        printf("FAIL: wanted(%d) != got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 1;
    }
}

static int test_3(void)
{
    int buf[] = {1, 3};
    int wanted = 2;
    int total = longest(buf, ARRAY_COUNT(buf));

    if (wanted == total) {
        printf("PASS: wanted(%d) == got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 0;
    } else {
        printf("FAIL: wanted(%d) != got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 1;
    }
}

static int test_4(void)
{
    int buf[] = {6, 7, 8, 3, 4, 5, 9, 10};
    int wanted = 5;
    int total = longest(buf, ARRAY_COUNT(buf));

    if (wanted == total) {
        printf("PASS: wanted(%d) == got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 0;
    } else {
        printf("FAIL: wanted(%d) != got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 1;
    }
}

static int test_5(void)
{
    int buf[] = {2, 1, 3, 2, 4, 3, 5, 4, 6};
    int wanted = 5;
    int total = longest(buf, ARRAY_COUNT(buf));

    if (wanted == total) {
        printf("PASS: wanted(%d) == got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 0;
    } else {
        printf("FAIL: wanted(%d) != got(%d): ", wanted, total);
        print_buf(buf, ARRAY_COUNT(buf));
        return 1;
    }
}

static int test_by_no(int testno)
{
    int res = 0;

    switch (testno) {
        case 1: {
            res = test_1();
        } break;
        case 2: {
            res = test_2();
        } break;
        case 3: {
            res = test_3();
        } break;
        case 4: {
            res = test_4();
        } break;
        case 5: {
            res = test_5();
        } break;
        default: {
            fprintf(stderr, "test %d does not exist\n", testno);
            res = -1;
        }
    }

    return res;
}

int main(int argc, char *argv[])
{
    int testno = -1;
    int res;
    int i;

    if (argc > 1) {
        testno = atoi(argv[1]);
    }

    if (testno > 0) {
        return test_by_no(testno);
    }

    res = 0;

    for (i = 1; i <= 5; ++i) {
        if (test_by_no(i)) {
            res = 1;
        }
    }

    return res;
}
