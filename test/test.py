from bisect import bisect_right, bisect_left

a = [1,3,7,11]

print(bisect_right(a, 2))
print(bisect_left(a, 2))