// --------------------------------------------------------------------------------------------------------------------
// Includes
// --------------------------------------------------------------------------------------------------------------------
#include "mat_examples.h"
#include <stdio.h>
#include <stdlib.h>
#include <bits/time.h>
#include <time.h>
// --------------------------------------------------------------------------------------------------------------------


// --------------------------------------------------------------------------------------------------------------------
// Functions
// --------------------------------------------------------------------------------------------------------------------
void print_mat(MatExample_t* example)
{
    for(int i = 0; i < example->rows; i++)
    {
        for(int j = 0; j < example->cols; j++)
            printf("%d ", ARR_MAT_GET_ITEM(example->mat, i, j, example->cols));

        printf("\n");
    }
}
// --------------------------------------------------------------------------------------------------------------------

int getExamples(MatExample_t** examples)
{
    int count = 0;
    MatExample_t* ptr = NULL;
    time_t t;
    srand((unsigned) time(&t));

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        empty, 
        /*Rows & Cols*/ 4, 3, 
        /*Exp_result*/  0,
        /*Matrix*/      {                 
            0, 0, 0, 
            0, 0, 0, 
            0, 0, 0, 
            0, 0, 0, 
        }
    );

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        ilha1, 
        /*Rows & Cols*/ 4, 3, 
        /*Exp_result*/  1,
        /*Matrix*/      {                 
            0, 0, 0, 
            0, 1, 0, 
            0, 0, 0, 
            0, 0, 0, 
        }
    );

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        ilha1_v2, 
        /*Rows & Cols*/ 4, 3, 
        /*Exp_result*/  1,
        /*Matrix*/      {                 
            0, 0, 0, 
            0, 1, 0, 
            1, 0, 0, 
            0, 0, 0, 
        }
    );

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        ilhas4, 
        /*Rows & Cols*/ 5, 5, 
        /*Exp_result*/  4,
        /*Matrix*/      {                 
            0, 1, 1, 0, 1, 
            0, 1, 0, 0, 0, 
            0, 0, 1, 0, 0, 
            0, 0, 0, 0, 1, 
            1, 0, 0, 0, 0  
        }
    );

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        ilhas4_v2, 
        /*Rows & Cols*/ 5, 5, 
        /*Exp_result*/  4,
        /*Matrix*/      {                 
            1, 0, 1, 0, 1, 
            0, 1, 0, 0, 0, 
            0, 0, 1, 0, 0, 
            0, 0, 0, 0, 1, 
            1, 0, 0, 0, 0  
        }
    );

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        ilhas3, 
        /*Rows & Cols*/ 5, 7, 
        /*Exp_result*/  3,
        /*Matrix*/      {                 
            1, 1, 0, 0, 0, 0, 1,     
            1, 1, 1, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 1, 0,
            0, 0, 0, 1, 1, 1, 0,
            1, 0, 0, 1, 1, 1, 1
        }
    );

    CREATE_EXAMPLE (
        /*ptr*/         ptr,
        /*count*/       count,
        /*Name*/        ilhas2_10_10, 
        /*Rows & Cols*/ 12, 10, 
        /*Exp_result*/  2,
        /*Matrix*/      {                 
            1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 
            1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 
            1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 
            0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 
            1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 
            1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 
            0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 
            0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 
            1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 
            1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
            1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        }
    );

    const int rr = 1024;
    const int rc = 1024;
    int ilhasRandom_mat[rr * rc];
    for(int i = 0; i < rr * rc; i++)
        ilhasRandom_mat[i] = rand() & 1;

    ptr = (MatExample_t*)realloc(ptr, (count + 1) * sizeof(MatExample_t));
    strcpy(ptr[count].name, "ilhasRandom"); 
    ptr[count].rows = rr; 
    ptr[count].cols = rc; 
    ptr[count].expected_result = -1; 
    ptr[count].mat = (int*)malloc(rr * rc * sizeof(int));
    memcpy(ptr[count].mat, ilhasRandom_mat, rr * rc * sizeof(int)); 
    count++;

    (*examples) = ptr;
    return count;
}
// --------------------------------------------------------------------------------------------------------------------
