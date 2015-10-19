Problem Statement

In this problem, you will have to efficiently implement modular exponentation. Recall that the problem of modular exponentation is, given positive integers a and n, and a non-negative integer x, calculate ax mod n.

One way of doing this is exponentation by squaring. It involves repeatedly squaring the base a and reducing it mod n. Doing so yields the values a, a^2, a^4, a^8, ... etc. By combining these in the correct way, and using the fact that every number has a binary representation, we can compute a^x mod n in time O(logx).

Implement modular exponentation by squaring, and output the intermediary values of a^(2^i), as well as the final value a^x mod n.

Input Format

The input will be exactly one line, with three space delimited integers a, x, and n.

The integers will satisfy 2 <= a, x, n <= 2^64

Output Format

On the first line, output the d-bit binary representation of x.

On the next d lines, output the values:

a^1 mod n,

a^2 mod n,

a^4 mod n

...

a^(2^d) mod n

On the last line, output a^x mod n

Sample Input

3 7 10

Sample Output

111

3

9

1

7

Explanation

7 in binary is written as 111.

3^1 = 3 mod 10

3^2 = 9 mod 10

3^4 = 81 = 1 mod 10

3^7 = 2187 = 7 mod 10
