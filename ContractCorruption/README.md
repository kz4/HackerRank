You are a U.S. senator on a committee for figuring out the best way to install power grid infrastructure within your community. Currently, there are **N** distribution centers that have been constructed. It has been decided that all of these distribution centers must be connected in a network set up. In order to construct the power line connections, the work must be outsourced to private companies.

There are two main power mainatanance companies that will construct such connections: Maverick, and Desperado. You have approached each one with information regarding your distribution centers, and an amount you are willing to pay for each one, which is constant independent of what distribution centers you are trying to connect. In response, both companies have responded with a list of connections that they are willing to build given your proposed price.

Since each contract has the same price, you will minimize your costs by minimizing the number of contracts you give out. A set of contracts is valid if and only if it satisfies the following:

* All distribution centers are connected within the power grid. There can't be isolated components, and there should exist a path between every pair of centers.

* The total number of contracts given out is minimized.

Given their responses, you believe it should be relatively straight forward to figure out how to connect all the distribution centers for minimum cost. However, there is a problem... 2016 is approaching, and you forgot that you are also running for president. Part of your campaign image is that you are a down to earth american who enjoys college ball and healthy competition in a capitalist economy. If you gave out too many of the contracts to a single company, then those pesky data scientists with their big data algorithms will point out this fact and use it to attack you for inconsistency.

Suppose that you give **A** contracts out to Maverick, and **B** contracts out to Desperado. Then the bias of your assignments will be the absolute value difference of **A** and **B**. Your updated goal is to figure out which subset of contracts to give out, so that all of the distribution centers are connected, costs are minimized, and the bias of your contract selection is minimized.

Write a program to take the contract information, and determine how small of a bias you can achieve for a valid set of contracts. You do not need to determine the actual set of contracts to be outputted.

Input Format

Line 1 :  **N** **C**
The first line indicates there are **N** distribution centers labeled **1** through **N**, and there are **C** contracts to consider 
They will satisfy **1 <= N <= 10^5, N <= M <= 250000** 

Next **C** lines:  **i j c**
Each of the following lines indicates a contract where  and  are distribution center labels, and  is either "MAVERICK" or "DESPERADO", the name of the company willing to purchase this contract.

The set of contracts will always be enough to yield at least one valid set of contracts.

Output Format

Line 1: **V**
Indicating **V** is the minimum possible bias for a valid set of contracts.

Your output should terminate with a new-line character.

Sample Input

3 3 
1 2 MAVERICK 
2 3 MAVERICK 
1 3 DESPERADO

Sample Output

0

Explanation

For  nodes, you need at least  contracts to connect them all. It is possible to select the following contracts: 
1 2 MAVERICK 
1 3 DESPERADO

Then all of the distribution centers will be connected, while the bias of the contract set is |1 - 1| = 0.