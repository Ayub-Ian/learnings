## Definition
Contiguous area of memory consisting of equal-size elements indexed by contiguous numbers.

### Properties
- Accept only same type of data
- Fixed in size
- Constant-time access to any element.
- Constant time to add/remove element at the end.
- Linear time to add/remove element at an arbitrary location.

## Layouts
The elements of an array can be stored in column-major layout or row-major layout. For an array stored in column-major layout, the elements from the first (leftmost) dimension or index are contiguous in memory. In row-major, the elements from the last (rightmost) dimension or index are contiguous. N-dimensional arrays can be stored in column-major or row-major layout.

Computer memory stores data in terms of one-dimensional arrays. For example, when you declare a 3-by-3 matrix, the software stores this matrix as a one-dimensional array with nine elements.



### Row Major Indexing
In row major order, the elements of a particular row are stored at adjacent memory locations. The first element of the array (arr[0][0]) is stored at the first location followed by the arr[0][1] and so on. After the first row, elements of the next row are stored next.

arr[3][3] =
[ a00, a01, a02 ]
[ b10, b11, b12 ]
[ c20, c21, c22 ]

Row major order = a00, a01, a02, b10, b11, b12, c20, c12, c22



### Column Major Indexing
In column major order, the elements of a column are stored adjacent to each other in the memory.The first element of the array (arr[0][0]) is stored at the first location followed by the arr[1][0] and so on. After the first column, elements of the next column are stored stating from the top.

arr[3][3] =
[ a00, a01, a02 ]
[ b10, b11, b12 ]
[ c20, c21, c22 ]

Column major order = a00, b10, c20, a01, b11, c21, a02, b12, c22

### Comparison of Row Major Order VS Column Major Order
Storing elements in row major order matrix improves the performance when the array elements are to be traversed in a contiguous fashion. This means traversing the array in a way that the elements of the first row are traversed first then the elements of the next row and so on. Row major order becomes a better choice in such cases because elements are stored exactly like this in memory and hence the traversal would simply mean moving through contiguous memory locations.

Column Major Order would be more useful in case the traversal involves going through the elements in the same column first and then onto the next one

All in all, the advantage is entirely performance based which might vary depending on the use case. But Row major order might generally yield better performance because the cache prefetches contiguous elements which are used in case of row major order. However, in case of column major order the cache prefetch is not used because the elements in the cahe are the elements in same row but for column major order the elements from the same column need to be traversed.




## Finding address of element given the index
If we are given the address of the first element (This address is also called the base address) as well as the index of the element, we can find out the address of any element of the array. The method of finding the address is slightly different for 1D, 2D, and 3D arrays.

### 1D Array

Given the base address, and the array is of type Integer, then to calculate the address of any element:

_address[i] = base_addr + i(sizeof (data type) - first_index)_

i = index of desired element

Generally, the indexing base is 0. We usually consider arrays that have 0 as the first index. In some cases, arrays have 1 based indexing, which means that the first index is 1.

Example:

Consider the base address of an boolean array to be 1048. Find the address of the element at index = 5. (Indexing is 0 based)

address[5] = base_addr + i*(sizeof(boolean) - first_index)

address[5] = 1048 + 5*(2) = 1048 + 10 = 1058

- 01048, 1049 = arr[0]
- 1050, 1051 = arr[1]
- 1052, 1053 = arr[2]
- 1054, 1055 = arr[3]
- 1056, 1057 = arr[4]
- **1058, 1059 = arr[5]**

### 2D Array

**Row Major Address**

The formula is intutive if we understand what it actually does. To calculate the address of an element in the ith row and jth column, we need to count how many memory locations have been used by the elements in the preceeding i-1 rows (where each row has N elements) in addition to the memory locations used by the preceeding j-1 elements in the current row. Each element will require as many bytes as used by the data type of the array. Hence, calculating the number of bytes required by all the preceeding elements in a row major fashion and adding this to the base address, would give use the address of the required element.

_address[i][j] = I + W * (i - l_row) * N + (j - l_col)_

- I : Base address
- l_row : lower bound for row

- l_col : lower bound for column
- W : sizeof (data type)
- N : Number of columns

Example:

Consider an integer array of size 3X3. The address of the first element is 1048. Calculate the address of the element at index i = 2, j = 1. (0 based index)

I = 1048, l_row = 0 = l_col, i = 2, j = 1, W = 2, N = 3

address[2][1] = I + W * (i-l_row) * N + (j - l_col)

address[2][1] = 1048 + 2 * 2 * 3 + 1 = 1048 + 12 + 1 = 1061

**Column Major Address**

Here, for an element at index (i,j) we need to calculate the number of memory locations required by the elements in the preceeding j-1 columns (where each column has M elements) in addition to the i-1 elements in the current column. Adding this amount to the base element will give us the address of the required element.

address[i][j] = I + W * ((j – l_col) * M + (i – l_row))

Example:

Consider an integer array of size 3X3. The address of the first element is 1048. Calculate the address of the element at index i = 2, j = 1. (0 based index)

I = 1048, l_row = 0 = l_col, i = 2, j = 1, W = 2, M = 3

address[2][1] = I + W * (j - l_col) * M + (i - l_row)

address[2][1] = 1048 + 2 * 1 * 3 + 2 = 1048 + 6 + 2 = 1056

### 3D Array



**Row Major Order**
- I : Base address,
- W : sizeof (data type) in bytes
- l_row : lower bound for row
- l_col : lower bound for column
- l_block : lower bound for block
- N : Number of columns
- R : Number of blocks


address of[i][j][k] = I + W * {[(i – l_row) * N] + [(j – l_col)]} * R + [k – l_block]


**Column Major Order**

address of[i][j][k] = I + W * {[(i – l_row)] + [(j – l_col) * M]} * R + [k – l_block]



## Dynamic Arrays

## Jagged Arrays