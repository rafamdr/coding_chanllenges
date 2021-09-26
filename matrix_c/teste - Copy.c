#include <stdint.h>
#include <math.h>
#include <stdio.h>

#define ARR_MAT_GET_ITEM(m, i, j, num_cols) *((m + i * num_cols) + j)

void print_mat(int* mat, int n, int m)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            printf("%d ", ARR_MAT_GET_ITEM(mat, i, j, m));
        }
        printf("\n");
    }
}

int main()
{
    int mat[3][4] = {
        { 10, 11, 12, 13 },
        { 14, 15, 16, 17 },
        { 18, 19, 20, 21 }
    };

    print_mat(mat, 3, 4);
}