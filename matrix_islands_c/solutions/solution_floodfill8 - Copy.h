#ifndef SOLUTION_FLOODFILL8_H
#define SOLUTION_FLOODFILL8_H

// --------------------------------------------------------------------------------------------------------------------
// Includes
// --------------------------------------------------------------------------------------------------------------------
#include "../mat_examples/mat_examples.h"
// --------------------------------------------------------------------------------------------------------------------

// --------------------------------------------------------------------------------------------------------------------
// Typedefs/structs
// --------------------------------------------------------------------------------------------------------------------
typedef enum
{
    FF_IFS = 0,
    FF_FOR,
    FF_FOR_QUEUE,

}FloodFillSolution_t;
// --------------------------------------------------------------------------------------------------------------------

typedef struct MatPoint_t
{
    int x;
    int y;
}MatPoint_t;
// --------------------------------------------------------------------------------------------------------------------

// --------------------------------------------------------------------------------------------------------------------
// Exported functions
// --------------------------------------------------------------------------------------------------------------------
int solution_floodfill8(MatExample_t* example, double* elapsed_time, FloodFillSolution_t sol);
// --------------------------------------------------------------------------------------------------------------------


#endif /* !SOLUTION_FLOODFILL8_H */