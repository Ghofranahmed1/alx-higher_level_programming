#include "lists.h"
/**
 *reverse: function to reverse list
 *head_ref: list need to reversr
 *Return: nothing
 */
void reverse(listint_t** head_ref)
{
    listint_t* prev   = NULL;
    listint_t* current = *head_ref;
    listint_t* next;
    while (current != NULL)
    {
        next  = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head_ref = prev;
}

/**
 * comparaelist- function to compare to lists
 * @head1: the list need to compare
 * @head2: list need to copmare with
 * Return: 0 if fail and 1 for sucess
 */

int compareLists(listint_t* head1, listint_t* head2)
{
    listint_t* temp1 = head1;
    listint_t* temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n == temp2->n)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else return 0;
    }

    if (temp1 == NULL && temp2 == NULL)
        return 1;

    return 0;
}
