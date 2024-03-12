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

	if (*head == NULL || new == NULL)
		return (NULL);

	new->n = number; /* value insertion on the new node */
	new->next = NULL;

	while (temp->next != NULL)
	{
		if (new->n > temp->n && new->n < temp->next->n)
		{
			new->next = temp->next; /* connecting to the node with higher value */
			temp->next = new; /* connecting to the node with lesser value */
			/* node insertion in the right index */
			return (new);
		}

		temp = temp->next; /* move to the next node */


	}

	if (temp->n < new->n)
		temp->next = new; /* insertio at the end of the list */
	else if (temp->n > new->n)
		new->next = temp; /* insertion at the beginning */
	return (new);


}