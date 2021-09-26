
// --------------------------------------------------------------------------------------------------------------------
// Includes
// --------------------------------------------------------------------------------------------------------------------
#include "cstack.h"
#include "stddef.h"
#include <stdlib.h>
#include <string.h>

// --------------------------------------------------------------------------------------------------------------------
// Functions
// --------------------------------------------------------------------------------------------------------------------
/**
 * Allocate a new cstack_t (NULL on failure)
 */

cstack_t *
cstack_new() {
  cstack_t *self;
  if (!(self = CSTACK_MALLOC(sizeof(cstack_t)))) return NULL;
  self->size = 0;
  self->top = NULL;
  return self;
}
// --------------------------------------------------------------------------------------------------------------------

/**
 * Allocate a new cstack_node_t (NULL on failure)
 */

cstack_node_t *
cstack_node_new(void *val, int val_size) {
  cstack_node_t *self;
  if (!(self = CSTACK_MALLOC(sizeof(cstack_node_t)))) return NULL;
  self->next = NULL;
  if (!(self->val = CSTACK_MALLOC(val_size))) return NULL;
  memcpy(self->val, val, val_size);
  return self;
}
// --------------------------------------------------------------------------------------------------------------------

/**
 * Push a new node onto the stack
 */

void
cstack_push(cstack_t *stack, void *val, int val_size) {
  cstack_node_t *node = cstack_node_new(val, val_size);
  node->next = stack->top;
  stack->top = node;
  stack->size++;
}
// --------------------------------------------------------------------------------------------------------------------

/**
 * Pop a node off the stack
 */

void
cstack_pop(cstack_t *stack) {
  if (stack->size) {
    cstack_node_t *popped = stack->top;
    stack->top = stack->top->next;
    stack->size--;
    CSTACK_FREE(popped->val);
    CSTACK_FREE(popped);
  }
}
// --------------------------------------------------------------------------------------------------------------------

/**
 * Remove all nodes from the stack
 */

void
cstack_empty(cstack_t *stack) {
  if (stack->size) {
    unsigned int size = stack->size;
    while (size--) cstack_pop(stack);
  }
}
// --------------------------------------------------------------------------------------------------------------------

/**
 * Destroy the entire stack
 */

void
cstack_destroy(cstack_t *stack) {
  cstack_empty(stack);
  CSTACK_FREE(stack);
}
// --------------------------------------------------------------------------------------------------------------------
