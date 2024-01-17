# Hash Table (Hash Map)
The Hash table data structure stores elements in key-value pairs where

Key- unique integer that is used for indexing the values
Value - data that are associated with keys.

Some important notes about hash tables:

- Values are not stored in a sorted order.
- You must account for potential collisions.

## Hashing (Hash Function)
In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called hashing.

Hashing is a technique of mapping a large set of arbitrary data to tabular indexes using a hash function. It is a method for representing dictionaries for large datasets.

It allows lookups, updating and retrieval operation to occur in a constant time i.e. O(1).

A hash function is an algorithm that produces an index of where a value can be found or stored in the hash table.

### Why Hashing is Needed?
After storing a large amount of data, we need to perform various operations on these data. Lookups are inevitable for the datasets. Linear search and binary search perform lookups/search with time complexity of O(n) and O(log n) respectively. As the size of the dataset increases, these complexities also become significantly high which is not acceptable.

We need a technique that does not depend on the size of data. Hashing allows lookups to occur in constant time i.e. O(1).

### Hash Collision
When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a hash collision.

We can resolve the hash collision using one of the following techniques.

- Collision resolution by chaining
- Open Addressing: Linear/Quadratic Probing and Double Hashing




###  1. Collision resolution by chaining
In chaining, if a hash function produces the same index for multiple elements, these elements are stored in the same index by using a doubly-linked list.

Chaining means that each key/value pair in the hash table, the value is a linked list of data rather than a single cell.

If _`j`_ is the slot for multiple elements, it contains a pointer to the head of the list of elements. If no element is present, _`j`_ contains NIL.

![Collision resolution by chaining](./images/Hash-3_1.webp)

The main drawback of chaining is the increase in time complexity. Instead of 0(1) as with a regular hash table, each lookup will take more time since we need to traverse each linked list to find the correct value.

### 2. Open Addressing
Open addressing means that, once a value is mapped to a key that's already occupied, you move along the keys of the hash table until you find one that's empty.

Unlike chaining, open addressing doesn't store multiple elements into the same slot. Here, each slot is either filled with a single key or left NIL.

Different techniques used in open addressing are:

<ol type="i">
<li><h4><b>Linear Probing</b></h4>
<p>
In linear probing, collision is resolved by checking the next slot.

Let k be a key and h(x) be a hash function.

Here, h(k) will give us a new index to store the element linked with k.

h(k, i) = (h′(k) + i) mod m

where

i = {0, 1, ….}
h'(k) is a new hash function
If a collision occurs at h(k, 0), then h(k, 1) is checked. In this way, the value of i is incremented linearly.

The problem with linear probing is that a cluster of adjacent slots is filled. When inserting a new element, the entire cluster must be traversed. This adds to the time required to perform operations on the hash table.
</p>
</li>

<li>
<h4><b>Quadratic Probing</b></h4>
<p>

It works similar to linear probing but the spacing between the slots is increased (greater than one) by using the following relation.

h(k, i) = (h′(k) + c<sub>1</sub>i + c<sub>2</sub>i<sup>2</sup>) mod m

where,

c<sub>1</sub> and c<sub>2</sub> are positive auxiliary constants,
i = {0, 1, ….}
</p>
</li>

<li>
<h4><b>Double Hashing</b></h4>
<p>
If a collision occurs after applying a hash function h(k), then another hash function is calculated for finding the next slot.

h(k, i) = (h<sub>1</sub> (k) + ih<sub>2</sub>(k)) mod m</p>
</li>
</ol>


### Good Hash Functions
A good hash function may not prevent the collisions completely however it can reduce the number of collisions.

Here, we will look into different methods to find a good hash function

1. **Division Method**

    If k is a key and m is the size of the hash table, the hash function h() is calculated as:

    h(k) = k mod m

    For example, If the size of a hash table is 10 and k = 112 then h(k) = 112 mod 10 = 2. The value of m must not be the powers of 2. This is because the powers of 2 in binary format are 10, 100, 1000, …. When we find k mod m, we will always get the lower order p-bits.

1. Multiplication Method
    h(k) = ⌊m(kA mod 1)⌋

    where,

    - kA mod 1 gives the fractional part kA,
    - ⌊ ⌋ gives the floor value
    - A is any constant. The value of A lies between 0 and 1. But, an optimal choice will be ≈ (√5-1)/2 suggested by Knuth.

1. Universal Hashing

    In Universal hashing, the hash function is chosen at random independent of keys.

## Advantages and Usages of Hash Tables:

- Fast Access: Hash tables provide constant-time average-case access time for inserting, deleting, and retrieving values.
- Data Caching: Hash tables are used in caching mechanisms to quickly store and retrieve recently accessed data.
- Dictionaries: Hash tables are used to implement dictionaries, where words are mapped to their definitions or translations.
- Indexing required: Hash tables are used to index and search data efficiently, reducing the need for linear searches.
- Cryptographic applications