"""
There are  strings. Each string's length is no more than  characters. There are also  queries. For each query, you are given a string, and you need to find out how many times this string occurred previously.

Input Format

The first line contains , the number of strings.
The next  lines each contain a string.
The nd line contains , the number of queries.
The following  lines each contain a query string.

Constraints





Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Sample Output

2
1
0
Explanation

Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all.
"""

number_of_string = int(input().strip())

string_list = list()
for i in range(number_of_string):
    string_list.append(input().strip())

number_of_queries = int(input().strip())
for j in range(number_of_queries):
    query_string = input().strip()
    print(string_list.count(query_string))
