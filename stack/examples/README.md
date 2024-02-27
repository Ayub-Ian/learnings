## Balanced Symbols

**Balanced symbols** means that each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested.e.g
`(()()()())`
`{ { ( [ ] [ ] ) } ( ) }`
`[ [ { { ( ( ) ) } } ] ]`
`[ ] [ ] [ ] ( ) { }`

The challenge then is to write an algorithm that will read a string of symbols from left to right and decide whether the symbols are balanced. To solve this problem we need to make an important observation.

 As you process symbols from left to right, the most recent opening symbols must match the next closing symbol

![par checker](../images/simpleparcheck.png)

Also, the first opening symbol processed may have to wait until the very last symbol for its match.

Closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out. This is a clue that **`stacks`** can be used to solve the problem.

### Steps
- Starting with an empty stack, process the symbol strings from left to right.
- If a symbol is an opening symbol, push it on the stack as a signal that a corresponding closing symbol needs to appear later.
- If, on the other hand, a symbol is a closing symbol, pop the stack. We must check to be sure that it correctly matches the type of the opening symbol on top of the stack. If the two symbols do not match, the string is not balanced. As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. 
- If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly. 
- At the end of the string, when all symbol have been processed, the stack should be empty. 


## Infix, Prefix and Postfix Expressions

**Infix** type of notation, has an operator in between the two operands it's working on. When you write an arithmetic expression such as B * C, the form of the expression provides you with information so that you can interpret it correctly. In this case we know that the variable B is being multiplied by the variable C since the multiplication operator * appears between them in the expression.

Each operator has a **precedence** level. Operators of higher precedence are used before operators of lower precedence. The only thing that can change that order is the presence of parentheses.

 The precedence order for arithmetic operators places multiplication and division above addition and subtraction. If two operators of equal precedence appear, then a left-to-right ordering or associativity is used.

 One way to write an expression that guarantees there will be no confusion with respect to the order of operations is to create what is called a **fully parenthesized** expression. This type of expression uses one pair of parentheses for each operator. The parentheses dictate the order of operations; there is no ambiguity. There is also no need to remember any precedence rules.

  Changes to the position of the operator with respect to the operands create two new expression formats, **prefix** and **postfix**. Prefix expression notation requires that all operators precede the two operands that they work on. Postfix, on the other hand, requires that its operators come after the corresponding operands. A + B * C would be written as + A * B C in prefix. In postfix, the expression would be A B C * +. Although the operators moved and now appear either before or after their respective operands, the order of the operands stayed exactly the same relative to one another. The order of operations within prefix and postfix expressions is completely determined by the position of the operator and nothing else.

  ### Conversion of Infix Expressions to Prefix and Postfix
  There are algorithmic ways to perform the conversion that allow any expression of any complexity to be correctly transformed:

  1. First technique is use of the **fully parenthesized** expression. Each parenthesis pair  denotes the beginning and the end of an operand pair with the corresponding operator in the middle. The position of the parenthesis pair is actually a clue to the final position of the enclosed operator.

  Assume the infix expression is a string of tokens delimited by spaces. The operator tokens are *, /, +, and -, along with the left and right parentheses, ( and ). The operand tokens are the single-character identifiers A, B, C, and so on. The following steps will produce a string of tokens in postfix order.

1. Use a dictionary called prec to hold the precedence values for the operators.

1. Create an empty stack called opstack for keeping operators. Create an empty list for output.

1. Convert the input infix string to a list by using the string method split.

1. Scan the token list from left to right.

    - If the token is an operand, append it to the end of the output list.

    - If the token is a left parenthesis, push it on the opstack.

    - If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.

    - If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.

1. When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.







### Postfix Evaluation

Consider the postfix expression 4 5 6 * +. As you scan the expression from left to right, you first encounter the operands 4 and 5. At this point, you are still unsure what to do with them until you see the next symbol. Placing each on the stack ensures that they are available if an operator comes next.

In this case, the next symbol is another operand. So, as before, push it and check the next symbol. Now we see an operator, *. This means that the two most recent operands need to be used in a multiplication operation. By popping the stack twice, we can get the proper operands and then perform the multiplication (in this case getting the result 30).

We can now handle this result by placing it back on the stack so that it can be used as an operand for the later operators in the expression. When the final operator is processed, there will be only one value left on the stack. Pop and return it as the result of the expression. 

Assume the postfix expression is a string of tokens delimited by spaces. The operators are *, /, +, and - and the operands are assumed to be single-digit integer values. The output will be an integer result.

1. Create an empty stack called operandStack.

1. Convert the string to a list by using the string method split.

1. Scan the token list from left to right.

    - If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.

    - If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the operandStack.

1. When the input expression has been completely processed, the result is on the stack. Pop the operandStack and return the value.