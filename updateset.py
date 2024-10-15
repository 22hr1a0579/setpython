''' Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5'''
 
set1_input = input().strip().split()
set1 = set(map(int, set1_input))

set2_input = input().strip().split()
set2 = set(map(int, set2_input))
set1.update(set2)
sorted_values = sorted(set1)
print(" ".join(map(str, sorted_values)))
