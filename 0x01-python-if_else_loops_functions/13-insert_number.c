#include "lists.h"

/**
 * insert_node - function inserts a number into a sorted singly linked list.
 * @number: number in the link list
 * @head: the linked list
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *rev;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if  (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		(*head)->next = new;
		return (new);
	}

	while (temp->n < new->n)
	{
		rev = temp;
		temp = temp->next;
		if (temp == NULL)
		{
			rev->next = new;
			return (new);
		}
	}
	new->next = rev->next;
	rev->next = new;
	return (new);
}
