#include "search.h"
/**
 * linear_skip - search in a skip list
 * @list: pointer to the head
 * @value: the value to search for
 * Return: NULL or a pointer
 */

skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *checkif;

	if (list == NULL)
		return (NULL);
	checkif = list;
	while (checkif->express)
	{
		printf("Value checked at index [%lu] = [%d]\n",
		       checkif->express->index, checkif->express->n);
		if (checkif->express->n >= value)
		{
			printf("Value found between indexes [%lu] and [%lu]\n",
			       checkif->index, checkif->express->index);
			break;
		}
		checkif = checkif->express;
	}
	if (!checkif->express)
	{
		list = checkif;
		while (list->next)
			list = list->next;
		printf("Value found between indexes [%lu] and [%lu]\n",
		       checkif->index, list->index);
	}
	list = checkif;
	while (list != checkif->express)
	{
		printf("Value checked at index [%lu] = [%d]\n",
		       list->index, list->n);
		if (list->n == value)
			break;
		list = list->next;
	}
	if (list != checkif->express)
		return (list);
	return (NULL);
}
