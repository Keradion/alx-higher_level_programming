#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: double pointet to the head node of the list
 * return: 1 if its, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	struct listint_s *temp = *head;
	struct listint_s *temp2 = NULL;
	struct listint_s *new_node = NULL;

	if (temp == NULL || temp->next == NULL)
		return (0);
	while (temp != NULL)
	{
		new_node = malloc(sizeof(listint_t));

		new_node->n = temp->n;
		new_node->next = temp2;

		temp2 = new_node;
		temp = temp->next;
	}

	temp = *head;
	while (temp != NULL && new_node != NULL)
	{
		if (temp->n != new_node->n)
		{
			return (0);
		}
		temp = temp->next;
		new_node = new_node->next;
	}
	return (1);
}
