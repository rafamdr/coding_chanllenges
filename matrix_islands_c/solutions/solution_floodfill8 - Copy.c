// --------------------------------------------------------------------------------------------------------------------
// Includes
// --------------------------------------------------------------------------------------------------------------------
#include "solution_floodfill8.h"
#include "../mat_examples/mat_examples.h"
#include <time.h>
#include <sys/timeb.h>
#include <sys/time.h>
#include <stdbool.h>
#include "cstack.h"
// --------------------------------------------------------------------------------------------------------------------


// --------------------------------------------------------------------------------------------------------------------
// Functions
// --------------------------------------------------------------------------------------------------------------------
static void floodfill8_ifs(int* mat, int rows, int cols, int bcolor, int x, int y)
{
    ARR_MAT_SET_ITEM(mat, x, y, cols, bcolor);

    if((x - 1 >= 0) && (ARR_MAT_GET_ITEM(mat, x - 1, y, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x - 1, y);
    if((x - 1 >= 0) && (y - 1 >= 0) && (ARR_MAT_GET_ITEM(mat, x - 1, y - 1, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x - 1, y - 1);
    if((y - 1 >= 0) && (ARR_MAT_GET_ITEM(mat, x, y - 1, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x, y - 1);
    if((x + 1 < rows) && (y - 1 >= 0) && (ARR_MAT_GET_ITEM(mat, x + 1, y - 1, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x + 1, y - 1);
    if((x + 1 < rows) && (ARR_MAT_GET_ITEM(mat, x + 1, y, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x + 1, y);
    if((x + 1 < rows) && (y + 1 < cols) && (ARR_MAT_GET_ITEM(mat, x + 1, y + 1, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x + 1, y + 1);
    if((y + 1 < cols) && (ARR_MAT_GET_ITEM(mat, x, y + 1, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x, y + 1);
    if((x - 1 >= 0) && (y + 1 < cols) && (ARR_MAT_GET_ITEM(mat, x - 1, y + 1, cols) != bcolor))
        floodfill8_ifs(mat, rows, cols, bcolor, x - 1, y + 1);
}
// --------------------------------------------------------------------------------------------------------------------

// static void floodfill8_for(int* mat, int rows, int cols, int bcolor, int x, int y)
// {
//     static const int pos_modders[8][2] = {
//         {-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}
//     };

//     ARR_MAT_SET_ITEM(mat, x, y, cols, bcolor);

//     for(int i = 0; i < 8; i++)
//     {
//         int nx = x + pos_modders[i][0];
//         int ny = y + pos_modders[i][1];

//         if (
//             (nx >= 0) && (nx < rows) &&
//             (ny >= 0) && (ny < cols) &&
//             (ARR_MAT_GET_ITEM(mat, nx, ny, cols) != bcolor)
//         )
//         {
//             floodfill8_for(mat, rows, cols, bcolor, nx, ny);
//         }
//     }
// }
// --------------------------------------------------------------------------------------------------------------------

static void floodfill8_for(int* mat, int rows, int cols, int bcolor, int x, int y)
{
    static const int pos_modders[8][2] = {
        {-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}
    };

    ARR_MAT_SET_ITEM(mat, x, y, cols, bcolor);

    for(int i = 0; i < 8; i++)
    {
        int nx = x + pos_modders[i][0];
        int ny = y + pos_modders[i][1];

        if (
            (nx >= 0) && (nx < rows) &&
            (ny >= 0) && (ny < cols) &&
            (ARR_MAT_GET_ITEM(mat, nx, ny, cols) != bcolor)
        )
        {
            floodfill8_for(mat, rows, cols, bcolor, nx, ny);
        }
    }
}
// --------------------------------------------------------------------------------------------------------------------

static void add_to_stack(cstack_t *stack, int x, int y)
{
    int arr_temp[2] = {x, y};
    cstack_push(stack, arr_temp, sizeof(x) * 2);
}
// --------------------------------------------------------------------------------------------------------------------

static void floodfill8_for_queue(int* mat, int rows, int cols, int bcolor, int x, int y)
{
    cstack_t *stack = cstack_new();
    static const int pos_modders[8][2] = {
        {-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}
    };

    add_to_stack(stack, x, y);

    while(stack->size)
    {
        x = ((int*)stack->top->val)[0];
        y = ((int*)stack->top->val)[1];
        cstack_pop(stack);
        ARR_MAT_SET_ITEM(mat, x, y, cols, bcolor);

        for(int i = 0; i < 8; i++)
        {
            int nx = x + pos_modders[i][0];
            int ny = y + pos_modders[i][1];

            if (
                (nx >= 0) && (nx < rows) &&
                (ny >= 0) && (ny < cols) &&
                (ARR_MAT_GET_ITEM(mat, nx, ny, cols) != bcolor)
            )
            {
                add_to_stack(stack, nx, ny);
            }
        }
    }

    cstack_destroy(stack);
}
// --------------------------------------------------------------------------------------------------------------------

static int internal_solution_floodfill8(int* mat, int rows, int cols,  double* elapsed_time, FloodFillSolution_t sol)
{
    int counter = 0;
    int found = 0;
    int bordercolor = 0;

    do
    {
        found = 0;
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                if(ARR_MAT_GET_ITEM(mat, i, j, cols) != bordercolor)
                {
                    switch(sol)
                    {
                        case FF_IFS:
                            floodfill8_ifs(mat, rows, cols, bordercolor, i, j);
                            break;

                        case FF_FOR:
                            floodfill8_for(mat, rows, cols, bordercolor, i, j);
                            break;

                        case FF_FOR_QUEUE:
                            floodfill8_for_queue(mat, rows, cols, bordercolor, i, j);
                            break;

                        default:
                            break;
                    }
                    counter++;
                    found = 1;
                }
            }
        }
    }while(1 == found);
    return counter;
}
// --------------------------------------------------------------------------------------------------------------------

int solution_floodfill8(MatExample_t* example, double* elapsed_time, FloodFillSolution_t sol)
{
    struct timespec start, end;  
    clock_gettime(CLOCK_MONOTONIC, &start); 
    //ios_base::sync_with_stdio(false); 
    int counter = 0;
    int* mat = (int*)malloc(example->rows * example->cols * sizeof(int));
    memcpy(mat, example->mat, example->rows * example->cols * sizeof(int));
    counter = internal_solution_floodfill8(mat, example->rows, example->cols, elapsed_time, sol);
    free(mat);
    clock_gettime(CLOCK_MONOTONIC, &end); 
    (*elapsed_time) = (end.tv_sec - start.tv_sec) * 1e9; 
    (*elapsed_time) = ((*elapsed_time) + (end.tv_nsec  - start.tv_nsec)) * 1e-9; 
    return counter;
}
// --------------------------------------------------------------------------------------------------------------------