# Recursion

Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling itself.

## Three Laws of recursion
All recursive algorithms must obey three important laws:

1. A recursive algorithm must have a **base case**. 
1. A recursive algorithm must change its state and move toward the **base case**.
1. A recursive algorithm must call itself, recursively.

**Base case** is uaually a problem that is small enough to solve directly.

A change of state usually means some data that the algorithm is using is being modified. Usually the data that represents our problem gets smaller in some way.