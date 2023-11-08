#include "lists.h"

/**
 * freelist - free list
 * @head: list that will be free
 */

void freelist(listint_t *head)
{
	listint_t *tmp;

	while(head)
	{
		tmp = head;
		free(tmp);
		head = head->next;
	}
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *middle = NULL, *ptr = NULL, *ptr1 = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast->next && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	slow = slow->next;
	/* copy main Linked list to middle "*/
	while (slow != NULL)
	{
		ptr = malloc(sizeof(listint_t));
		if (ptr == NULL)
		{
			freelist(ptr);
			return (0);
		}
		ptr->n = slow->n;
		ptr->next = middle;
		middle = ptr;
		slow = slow->next;
	}
	ptr1 = middle;
	while (ptr1 != NULL)
	{
		if (tmp->n != ptr1->n)
			return (0);
		ptr1 = ptr1->next;
		tmp = tmp->next;
	}
	return (1);
}
