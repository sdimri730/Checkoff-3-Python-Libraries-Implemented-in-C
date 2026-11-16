# Checkoff-3-Python-Libraries-Implemented-in-C

This topic covers how External Python Libraries are optimized for performance through implementations in C

I mainly focused on the C implementations of Python's built-in List, comparing it to NumPy's array, and evaluating the performance differences between the two and where those differences come from. 

The main difference between the two is how they implement their collection through a C struct: Python's List is focused on flexibility and general usage, using a struct field that holds a double-pointer pointing to a list of addresses to Python objects. This implementation is incredibly memory-intensive and slow, as when iterating through the list, the C program must take time to dereference the pointer, locate it on the Heap, and return it. Meanwhile, the NumPy array focuses on speed, using a field that stores a contiguous block of memory (of a primitive C type) on the Heap. This allows for the use of pointer arithmetic to lookup and return elements quickly, optimizing the NumPy array for speed while sacrificing some flexibility. 

Specifically, in a test of adding 1 to each element of an array of 1,000,000 elements, a NumPy array implementatin is 10x faster than a Python List implementation, highlighting the major improvements in speed granted by NumPy's C implementations.
