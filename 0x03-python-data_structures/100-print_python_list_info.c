#include <Python.h>

/**
 * print_python_list_info - Print basic info about python
 * @p: Pyoject list
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
