#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it
 * @list: the linked list that need to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if(list->next ==  NULL)
		return (0);
	else
	{

	head = list;
	tail = list;


	while (head != NULL)
	{
		head = (head)->next->next;
		tail = (tail)->next;
		if (head == tail)
			return (1);
	}
	return (0);
	}
}
