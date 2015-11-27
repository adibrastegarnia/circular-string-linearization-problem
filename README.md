circular-string-linearization-problem

This problem arises in chemical databases for circular molecules. Each molecule is represented
by a circular string of chemical characters; to allow faster lookup and comparisons of
molecules, one wants to store each circular string by a canonical linear string.
A circular string of length n is a string in which the last character n -1 is considered to
precede the first character 0. The circular string linearization problem for a string S of
n characters is the following: Choose a place to cut the string S so that the resulting linear
string is lexically smallest of all the n possible linear strings created by cutting S. For
example, for circular string S=gcttc, we can get five linear strings: gcttc, cttcg, ttcgc, tcgct,
cgctt. Of these cgctt is the lexically smallest one.

There are several approaches to solving this problem. One way to solve it using a suffix tree
is to consider the doubled string SS, creating a suffix tree for it, and then searching in the
tree for the lexicographically smallest substring of n characters.

Input/output specification:

python yourprogram.py stringinput


Given a circular DNA sequence S, the program should calculate the positions to cut S so
that the resulting string is lexically smallest. For example, in the first sample input if you
cut between positions 3 and 4, you will get the lexically smallest string cgctt. In the second
sample input, you need to cut between first and last position to get it.
Sample Input: gcttc
Sample Output: 3,4
Sample Input: cgctt
Sample Output: 0,4
