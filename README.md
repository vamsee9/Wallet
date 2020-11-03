# Wallet

1. **Wallet** _ **:** _ Write a python program to implement the following operations for **Wallet** class. **Data Attributes** of the wallet class should be: **amount**.

**Behaviors** of the Wallet class should be as follows.

1. **addAmount** (amount) Adding an amount to the wallet and return wallet amount. 2. **payAmount** (amount) Paying money from the wallet and return wallet amount. 3. **checkBalance** () Return the current amount from the wallet.

**Note:**

● Don&#39;t consider negative numbers, when adding or paying the amounts

● Amount can be float (23 rupees 43 paisa = 23.43)

● Return an error message &quot; **Amount can&#39;t be negative**&quot;, if the amounts given are negative while paying and adding amounts from or to Wallet

● Return an error message &quot; **Insufficient funds**&quot;, if the Wallet amount is less than the amount to be paid

**Input Format:**

● The first line of the input contains the number of operations to be performed on Wallet class. **●** From the second line onwards, there will be a single operation per line.

● Each line contains one value for checkBalance() and two values for adding and paying the amounts. Check for the sample test case.

**Output Format:**

● For each operation you perform on the Wallet, print the amount from the Wallet. (Simple Invoke or call checkBalance())

**Sample Input #1:**

**10**

**payAmount 1000**

**checkBalance**

**addAmount 100**

**payAmount 25**

**payAmount 35**

**checkBalance**

**payAmount 30**

**addAmount 300**

**payAmount 270**

**checkBalance**

**Sample Output #1:**

**Wallet has zero balance. 0.0**

**100.0**

**75.0**

**40.0**

**40.0**

**10.0**

**310**

**40.0**

**40.0**
