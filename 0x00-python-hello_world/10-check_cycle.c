#include "lists.h"
/**
 * check_cycle - check if there is a cycle in a singly linked list
 * @list: pointer to the head node of the list
 * Return: 1 if cycle exist 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* if no node exist or a single node only */
	/* no cycle can be formed with a single node */

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast != NULL)
	{
		slow = slow->next; /* move by 1 node at a time */
		fast = fast->next->next; /* move by 2 nodes at a time*/
			/* if there a cycle in the list, at some node fast and slow will be same */

			if (fast == slow)
				return (1);
	}
	return (0);

}
