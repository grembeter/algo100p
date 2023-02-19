#include <stdlib.h>
#include <hashset.h>

enum {
    kPRIME = 71UL
};

struct hashset {
    size_t capacity;
    struct {
        int buck;
        int occupied;
    } d[1];
};

static size_t hash_key(struct hashset *hs, int key)
{
    if (key < 0) {
        key = -key;
    }

    return ((size_t)key * kPRIME % hs->capacity);
}

static struct hashset *hash_alloc(size_t capacity)
{
    struct hashset *hs;

    capacity += capacity / 3;

    hs = calloc(sizeof(*hs) + sizeof(int) * 2 * (capacity - 1), 1);

    if (!hs) {
        return NULL;
    }

    hs->capacity = capacity;

    return hs;
}

static void hash_free(struct hashset *hs)
{
    if (hs) {
        free(hs);
    }
}

static int hash_key_exists(struct hashset *hs, int key)
{
    size_t ibuck = hash_key(hs, key);

    while (hs->d[ibuck].occupied) {
        if (hs->d[ibuck].buck == key) {
            return 1;
        }

        ibuck++;
    }

    return 0;
}

static size_t hash_add(struct hashset *hs, int key)
{
    size_t ibuck = hash_key(hs, key);

    while (hs->d[ibuck].occupied) {
        ibuck = (ibuck + 1) % hs->capacity;
    }

    hs->d[ibuck].buck = key;
    hs->d[ibuck].occupied = 1;

    return ibuck;
}

/* A = [6,3,5,2,1,7], X = 4, Result = [3,1] */
/* H
   6 -> -2
   3 ->  1
   5 -> -1
   2 ->  2
   1 => return
 */
struct pair *find_2sum(int sum, int *arr, size_t nelems)
{
    struct hashset *hs;
    struct pair *pair;
    int i;

    hs = hash_alloc(nelems);

    if (!hs) {
        return NULL;
    }

    pair = NULL;

    for (i = 0; i < nelems; ++i) {
        int x = sum - arr[i];
        if (hash_key_exists(hs, arr[i])) {
            pair = malloc(sizeof(*pair));
            if (pair) {
                pair->x = x;
                pair->y = arr[i];
            }
            break;
        }

        hash_add(hs, x);
    }

    hash_free(hs);

    return pair;
}

