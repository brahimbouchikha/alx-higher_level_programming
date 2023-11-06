#include "lists.h"

/**
 * lenght_list - return lenght list
 * @head: list to calculate the lenght
 *
 * Return: lenght of the list
 */

int lenght_list(listint_t *head)
{
	int count = 0;
	listint_t *tmp = head;

	while (tmp != NULL)
	{
		count++;
		tmp = tmp->next;
	}
	return (count);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *array, size, i = 0, last;
	listint_t *tmp;

	if (*head == NULL)
		return (1);
	tmp = *head;
	size = lenght_list(*head);
	array = malloc(sizeof(int) * size);
	if (array == NULL)
	{
		return (0);
	}
	while (tmp != NULL)
	{
		array[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	for (i = 0; i < size / 2; i++)
	{
		last = (size - 1) - i;
		if (array[i] != array[last])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);

}
