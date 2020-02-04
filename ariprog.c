/*
ID: seishin1
LANG: C
TASK: ariprog
*/
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 30
#define MAX_M 300

void quick_sort(int n, int* a){ // Size n list, first element pointed at by a.
    // Choose a pivot
    // Everything smaller into sub-list L
    // Everything bigger or equal into sub-list R
    // Ensure you leave the list in following form: L ... pivot ... R
    // Recurse quick_sort on L and R
    // Recursion base cases: n == 2. In this case simply swap if needed to ensure a[0] <= a[1].
    int i;
//    for(i=0; i<n; i++)
//        printf("%d, ", a[i]);
//    printf("\n");

    if(n <= 1){
        return;
    }
    if(n == 2){
//        printf("Base case!");
        if(a[0] > a[1]){
//            printf("Swapping %d %d\n", 0, 1);
            int swap = a[0];
            a[0] = a[1];
            a[1] = swap;
        }
//        printf("\n");
        return;
    }

    int pivot_index = 0;
    int pivot = a[pivot_index];

    for(i=1; i < n - 1; i++){
        if(a[i] < pivot){
//            printf("Swapping %d %d .. new pivot|i: %d %d\n", pivot_index, i, pivot_index+1, i+1);
            a[pivot_index] = a[i];
            pivot_index++;
            a[i] = a[pivot_index];
            //i++;

//            int debug;
//            printf("  ");
//            for(debug=0; debug<n; debug++)
//                printf("%d, ", a[debug]);
//            printf("\n");
        }
//        else{
//            printf("Continuing %d %d\n", pivot_index, i);
//        }
    }

    if(a[n-1] < pivot){
        a[pivot_index] = a[n-1];
        pivot_index++;
        a[n-1] = a[pivot_index];
        a[pivot_index] = pivot;
    }
    else{
        a[pivot_index] = pivot;
    }

//    for(i=0; i<n; i++)
//        printf("%d, ", a[i]);
//    printf("\nExecuting qsort left:\n");
    quick_sort(pivot_index, &a[0]);
//    printf("Executing qsort right:\n");
    quick_sort(n - pivot_index - 1, &a[pivot_index + 1]);
    return;
}
// SSSSSSSSSSS P BBBBBBBBBBBBBB N  (if N < P)
// SSSSSSSSSSS N BBBBBBBBBBBBBB P
// SSSSSSSSSSS N PBBBBBBBBBBBBB B N

// P B SSSS // pi = 0, i = 1, do nothing
// ^ ^

// S B SSS  // pi = 0, i = 2, swap 0&1 -> pi = 1, i = 3
// ^   ^

// S S BSS  // pi = 1, i = 3, swap 2&3 -> pi = 2, i = 4
//   ^  ^

// S S SBS  // pi = 2, i = 4, swap 3&4 -> pi = 3, i = 5
//     ^ ^

// S S SSB  // Finished loop. Swap pi to n-1. Insert pivot to pi.
// S S SSPB


void main()
{
    FILE *fin  = fopen ("ariprog.in", "r");
    FILE *fout = fopen ("ariprog.out", "w");

    int i, j, limit, curr; // Temp vars
    
    int n, m;
    fscanf (fin, "%d %d", &n, &m);

//    scanf("%d", &n);
//    scanf("%d", &m);


//    n = 3;
//    m = 5;

//    #define TEST_N 2
//    int test[TEST_N] = {2, 1};
//    for(i=0; i<TEST_N; i++)
//        printf("%d, ", test[i]);
//    printf("\nQuick sorting!\n");
//    quick_sort(TEST_N, &test[0]);
//
//    for(i=0; i<TEST_N; i++)
//        printf("%d, ", test[i]);
//    printf("\n");


    printf("n: %d, m: %d\n", n, m);

    // Generate p-q nums
    int pqs[2*MAX_M*MAX_M + 1] = {}; // 0 for not p-q num. 1 for p-q num.
    int pq_nums[2 * MAX_M * MAX_M + 1];
    int num_pq_nums = 0; // Number of p-q numbers stored in pq_nums.

    limit = m + 1;
    for(i=0; i < limit; i++){
        //printf("TEST 2 ... %d\n", i);

        for(j=i; j < limit; j++){
            //printf("TEST 3 ... %d\n", j);
            curr = i*i + j*j;
            if(pqs[curr] != 1){
                //printf("TEST 4 ... %d\n", curr);
                pq_nums[num_pq_nums++] = curr;
                pqs[curr] = 1;
            }
        }
    }

    //printf("TEST 1\n");
    // DEBUG
//    limit = m*m + 1;
//    for(i=0; i < limit; i++){
//        printf("%d,", pqs[i]);
//    }

    //printf("TEST A\n");

//    limit = m*m + 1;
//    for(i=0; i < limit; i++){
//        printf("%d,", pqs[i]);
//    }

//    printf("\nSorted POG: %d\n", num_pq_nums);

//    for(i=0; i < num_pq_nums; i++){
//        printf("%d,", pq_nums[i]);
//    }
//    printf("\n");

    
//    printf("\n");
//    for(i=0; i < num_pq_nums; i++){
//        printf("%d,", pq_nums[i]);
//    }
//    printf("\n");

    //printf("TEST B\n");

    quick_sort(num_pq_nums, &pq_nums[0]);

    int max_bisquare = 2 * m*m;
    int a, b;
    int is_good;
    int none = 1;

    for(b=1; b < max_bisquare; b++){
        for(i=0; i < num_pq_nums; i++){
            if(max_bisquare < pq_nums[i] + (n-1)*b){
                break;
            }

            a = pq_nums[i];
            is_good = 1;
            for(j=1; j < n; j++){
                if(pqs[a + j*b] != 1){
                    is_good = 0;
                    break;
                }
            }

            if(is_good == 1){
                //printf("%d %d\n", a, b);
                fprintf (fout, "%d %d\n", a, b);
                if(none == 1)
                    none = 0;
            }
        }
    }

    if(none == 1)
        fprintf (fout, "NONE\n");

    exit (0);
}
