"""
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of integers) and  (the number of left rotations you must perform).
The second line contains  space-separated integers describing the respective elements of the array's initial state.

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:

Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4.
"""
std_input = list(map(int, input().strip().split()))
size_of_list, number_of_rotation =  std_input[0], std_input[1]
list_of_number = list(map(int, input().strip().split()))


def left_rotation(list_of_number, size_of_list, number_of_rotation):
    temp = list_of_number[0:number_of_rotation]
    for i in range(number_of_rotation,size_of_list):
        list_of_number[i - number_of_rotation] = list_of_number[i]
    list_of_number[size_of_list - number_of_rotation:] = temp
    return list_of_number

list_of_number = left_rotation(list_of_number, size_of_list, number_of_rotation)

for number in list_of_number:
    print(number, end=' ')
