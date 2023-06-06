#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list
 * @head: A pointer the head of the linked list
 * @number: The number to insert
 *
 * Return: NULL if function fails, otherwise inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *youth = *head;
	listint_t *shade = malloc(sizeof(listint_t));

	if (!shade)
		return (NULL);

	shade->n = number;
	shade->next = NULL;

	if (!youth || shade->n < youth->n)
	{
		shade->next = youth;
		*head = shade;
		return (shade);
	}

	while (youth->next)
	{
		if (shade->n < youth->next->n)
		{
			shade->next = youth->next;
			youth->next = shade;
			return (shade);
		}
		youth = youth->next;
	}

	youth->next = shade;
	return (shade);
}
