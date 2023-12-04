#include "lists.h"

/**
 * insert_node - function inserts a number into a sorted singly linked list., i wrote it ahhh
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
/*case empty list*/
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
/* case insern in begging */
	else if (temp->n > new->n)
	{
		*head = new;
		new->next = temp;
		return (new);
	}
/* insert in middel and at the end */
	else
	{

	while (temp->n < new->n)
	{
		rev = temp;
		temp = temp->next;
		/* in case it was in the end */
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
}
