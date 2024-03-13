#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head node of the list
 * @number: value to be insert
 * Return: address of the new node or NULL if insertion fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head; /* for traversal purpouse */
	listint_t *prev_node = NULL;
	listint_t *new_node = malloc(sizeof(listint_t)); /* creating a new node */

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (new_node->n < current_node->n)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}
	while (current_node = current_node->next != NULL)
	{
		prev_node = current_node;
		if (new_node->n >= current_node->n && new_node->n <= current_node->next->n)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		}
	}
	prev_node->next = new_node;
	return (new_node);
}
