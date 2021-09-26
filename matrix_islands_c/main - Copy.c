#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 256

/* Converts the string 's' from first-middle-last name 
   form into LAST-first-middle form. */

int lettercount(char *s)
{
  return 0;
}


int maximum(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}



int funcao_pqp(char* nome)
{
    // 1) checar as posicoes de um ponteiro
    // 2) incrementar uma variavel de controle
    // 3) ate encontrar o valor 0

    /*
    for(
        1a coisa: inicializar uma variavel de controle; int n = 2;

        2a coisa: limitar o loop; n <= 10;

        3a coisa: incrementos do loop; n = n + 2;
    )
    */

    // Ex: contar de 2 a 10 de 2 em 2
    int n;
    for(n = 0; nome[n] != 0; n++)
    {}


    

    return n;
}


/* Do not edit this function. */

int main()
{
    int n = funcao_pqp("silvioasdfsdf");
    printf("%d\n", n);

    return 0;
}