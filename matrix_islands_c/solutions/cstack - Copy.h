#ifndef CSTACK_H
#define CSTACK_H

#ifdef __cplusplus
extern "C" {
#endif

// --------------------------------------------------------------------------------------------------------------------
// Includes
// --------------------------------------------------------------------------------------------------------------------
#include <stdlib.h>

// --------------------------------------------------------------------------------------------------------------------
// Defines/macros
// --------------------------------------------------------------------------------------------------------------------
// Library version
#define CSTACK_VERSION "0.0.1"

// Memory management macros
#ifndef CSTACK_MALLOC
#define CSTACK_MALLOC malloc
#endif

#ifndef CSTACK_FREE
#define CSTACK_FREE free
#endif

// --------------------------------------------------------------------------------------------------------------------
// Typedefs/structs
// --------------------------------------------------------------------------------------------------------------------
/**
 * cstack_t node struct
 */

typedef struct cstack_node {
  struct cstack_node *next;
  void *val;
} cstack_node_t;
// --------------------------------------------------------------------------------------------------------------------

/**
 * cstack_t struct
 */

typedef struct {
  unsigned int size;
  cstack_node_t *top;
} cstack_t;
// --------------------------------------------------------------------------------------------------------------------

// --------------------------------------------------------------------------------------------------------------------
// Exported functions
// --------------------------------------------------------------------------------------------------------------------
/**
 * cstack_node_t prototypes
 */

cstack_node_t *
cstack_node_new(void *val, int val_size);
// --------------------------------------------------------------------------------------------------------------------

/**
 * cstack_t prototypes
 */

cstack_t *
cstack_new();
// --------------------------------------------------------------------------------------------------------------------

void
cstack_push(cstack_t *stack, void *val, int val_size);
// --------------------------------------------------------------------------------------------------------------------

void
cstack_pop(cstack_t *stack);
// --------------------------------------------------------------------------------------------------------------------

void
cstack_empty(cstack_t *stack);
// --------------------------------------------------------------------------------------------------------------------

void
cstack_destroy(cstack_t *stack);
// --------------------------------------------------------------------------------------------------------------------

#ifdef __cplusplus
}
#endif

#endif /* CSTACK_H */