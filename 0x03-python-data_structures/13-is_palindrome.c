#include "lists.h"

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
listint_t *middle = NULL, *ptr;

while (fast->next && fast->next->next)
{
fast = fast->next->next;
slow = slow->next;
}
/* copy main Linked list to middle "*/
while (slow != NULL)
{
ptr = malloc(sizeof(listint_t));
ptr->next = middle;
ptr->n = slow->n;
middle = ptr;
slow = slow->next;
}
free(ptr);
ptr = middle->next;
while (ptr != NULL)
{
if (tmp->n != ptr->n)
{
return (0);
}
ptr = ptr->next;
tmp = tmp->next;
}
return (1);
}
