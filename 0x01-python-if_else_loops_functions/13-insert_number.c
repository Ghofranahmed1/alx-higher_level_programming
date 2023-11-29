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

	rev = *head;
	temp = (*head)->next;
	new = malloc(sizeof(listint_t));
	if  (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (rev->n > number)
	{
		*head = new;
		new->next = rev;
		return (new);
	}
	while (temp)
	{
		if (temp->n < number)
		{
			temp = temp->next;
			rev = rev->next;
		}
		else
		{
			rev->next = new;
			new->next = temp;
			break;
		}
	}
	return (new);
}
