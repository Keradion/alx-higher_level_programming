#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head node of the list
 * @number: value to be insert
 * Return: address of the new node or NULL if insertion fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head; /* for traversal purpouse */
	listint_t *new = malloc(sizeof(listint_t)); /* creating a new node */

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		/* in case of empyt list */
		*head = new;
		return (new);
	}

	while (temp->next != NULL)
	{
		if (new->n > temp->n && new->n < temp->next->n)
		{
			new->next = temp->next; /* connecting to the node with higher value */
			temp->next = new; /* connecting to the node with lesser value */
			return (new);
		}

		temp = temp->next; /* move to the next node */


	}

	if (temp->n < new->n)
		temp->next = new; /* insertio at the end of the list */
	temp = *head;
	else if (temp->n > new->n || temp->n < new->n)
		new->next = temp; /* insertion at the beginning */

return (new);
}
