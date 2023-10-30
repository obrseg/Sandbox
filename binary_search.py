# binary_search function accepts a range of numbers (starting from 0) and number to look for. Returns amount of iterarions and target number.

def binary_search (range, target):
    left = 0
    right = range - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if mid == target:
            return iterations, mid
        elif mid > target:
            right = mid - 1
        elif mid < target:
            left = mid + 1
    return -1

# test algorithm for infinite loops usin range of 100. Add all results into a list and find max and min amount of iterations
num = 100
res_set = []
for x in range(num):
    res_set.append(binary_search(num, x))

res_set.sort()
print("Min iterations:", res_set[0][0], "for target number", res_set[0][1], "\nMax iterations:", res_set[-1][0], "for target number", res_set[-1][1])