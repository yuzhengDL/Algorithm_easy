# Rotate-Array

Approach #1 Brute Force
The simplest approach is to rotate all the elements of the array in k steps by rotating the elements by 1 unit in each step.

Approach #2 Using Extra Array
We use an extra array in which we place every element of the array at its correct position i.e. the number at index i in the original array is placed at the index (i+k). Then, we copy the new array to the original one.
