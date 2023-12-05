#include "lists.h"
/**
 * is_palindrome - function  checks if a singly linked list is a palindrome.
 *@head - the  singly linked list
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
	{
    listint_t *fast = *head, *slow = *head;
    listint_t *prev_slow = *head;
    listint_t *midnode = NULL;  // To handle odd size list
    listint_t *second_half = NULL;
    int res = 1;  // Initialize result

    if (*head != NULL && (*head)->next != NULL)
    {
        /* Get the middle of the list. Move slow by 1
           and fast by 2, slow will have the middle */
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;

            /* We need previous of the slow for
               linked list implementation */
            prev_slow = slow;
            slow = slow->next;
        }

        /* fast would become NULL when there are even elements in list.
           And not NULL for odd elements. We need to skip the middle node
           for odd case and store it somewhere so that we can restore the
           original list*/
        if (fast != NULL)
        {
            midnode = slow;
            slow = slow->next;
        }

        // Now reverse the second half and compare it with first half
        second_half = slow;
        prev_slow->next = NULL;  // NULL terminate first half
        reverse(&second_half);  // Reverse the second half
        res = compareLists(*head, second_half);  // compare

        /* Construct the original list back */
        reverse(&second_half);  // Reverse the second half again
        if (midnode != NULL)  // If there was a mid node (odd size case) which
                              // was not part of either first half or second half.
        {
            prev_slow->next = midnode;
            midnode->next = second_half;
        }
        else
            prev_slow->next = second_half;
    }
    return res;
}
