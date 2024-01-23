# Tree Data Structure
A tree is a non-linear abstract data type with a hierarchy-based structure. It consists of nodes (where the data is stored) that are connected via links. The tree data structure stems from a single node called a root node and has subtrees connected to the root.

![tree data structure](images/tree_data_structure.jpg)

### Why Tree Data Structure?
Other data structures such as arrays, linked list, stack, and queue are linear data structures that store data sequentially. In order to perform any operation in a linear data structure, the time complexity increases with the increase in the data size. But, it is not acceptable in today's computational world.

Different tree data structures allow quicker and easier access to the data as it is a non-linear data structure.

### Tree Terminologies
- **Node**
    A node is an entity that contains a key or value and pointers to its child nodes.

    The last nodes of each path are called **leaf nodes or external nodes** that do not contain a link/pointer to child nodes.

    The node having at least a child node is called an internal node.

- **Edge**
It is the link between any two nodes.
- **Root**
It is the topmost node of a tree.

- **Height of a Node**
The height of a node is the number of edges from the node to the deepest leaf (ie. the longest path from the node to a leaf node).

- **Depth of a Node**
The depth of a node is the number of edges from the root to the node.

- **Height of a Tree**
The height of a Tree is the height of the root node or the depth of the deepest node.

- **Degree of a Node**
The degree of a node is the total number of branches of that node.

- **Forest**
A collection of disjoint trees is called a forest.

- **Subtree**  represents the descendants of a node.
- **Visiting**   refers to checking the value of a node when control is on the node.

- **Traversing**   means passing through nodes in a specific order.
- **Keys**  represents a value of a node based on which a search operation is to be carried out for a node.

### Types of Trees
1. General Trees
1. Binary Trees
1. Binary Search Trees
1. AVL Trees

### 1.General Trees
General trees are unordered tree data structures where the root node has minimum 0 or maximum ‘n’ subtrees.

The General trees have no constraint placed on their hierarchy. The root node thus acts like the superset of all the other subtrees.

### 2.Binary Trees
Binary Trees are general trees in which the root node can only hold up to maximum 2 subtrees: left subtree and right subtree. Based on the number of children, binary trees are divided into three types.
- Full Binary Tree

    A full binary tree is a binary tree type where every node has either 0 or 2 child nodes.

- Complete Binary Tree

    A complete binary tree is a binary tree type where all the leaf nodes must be on the same level. However, root and internal nodes in a complete binary tree can either have 0, 1 or 2 child nodes.

- Perfect Binary Tree

    A perfect binary tree is a binary tree type where all the leaf nodes are on the same level and every node except leaf nodes have 2 children.

### 3.Binary Search Trees
Binary Search Trees possess all the properties of Binary Trees including some extra properties of their own, based on some constraints, making them more efficient than binary trees.

The data in the Binary Search Trees (BST) is always stored in such a way that the values in the left subtree are always less than the values in the root node and the values in the right subtree are always greater than the values in the root node, i.e. _**`left subtree < root node ≤ right subtree.`**_

### Advantages of BST
- Binary Search Trees are more efficient than Binary Trees since time complexity for performing various operations reduces.

- Since the order of keys is based on just the parent node, searching operation becomes simpler.

- The alignment of BST also favors Range Queries, which are executed to find values existing between two keys. This helps in the Database Management System.

### Disadvantages of BST
The main disadvantage of Binary Search Trees is that if all elements in nodes are either greater than or lesser than the root node, the tree becomes skewed. Simply put, the tree becomes slanted to one side completely.

This skewness will make the tree a linked list rather than a BST, since the worst case time complexity for searching operation becomes O(n).

To overcome this issue of skewness in the Binary Search Trees, the concept of **Balanced Binary Search Trees** was introduced.

#### Balanced Binary Search Trees
Consider a Binary Search Tree with ‘m’ as the height of the left subtree and ‘n’ as the height of the right subtree. If the value of (m-n) is equal to 0,1 or -1, the tree is said to be a Balanced Binary Search Tree.

The trees are designed in a way that they self-balance once the height difference exceeds 1. Binary Search Trees use rotations as self-balancing algorithms. There are four different types of rotations: Left Left, Right Right, Left Right, Right Left.

There are various types of self-balancing binary search trees −

- AVL Trees
- Red Black Trees
- B Trees
- B+ Trees
- Splay Trees
- Priority Search Trees


## Tree Applications
- Binary Search Trees(BSTs) are used to quickly check whether an element is present in a set or not.
- Heap is a kind of tree that is used for heap sort.
- A modified version of a tree called Tries is used in modern routers to store routing information.
- Most popular databases use B-Trees and T-Trees, which are variants of the tree structure we learned above to store their data
- Compilers use a syntax tree to validate the syntax of every program you write.