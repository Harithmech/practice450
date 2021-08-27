# reverse an array


# simple approach
""" arr = [1, 2, 3, 4, 5]
print(arr[::-1])
 """

# using iteration
""" arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(0, n//2):
    print(arr[i], arr[n-1-i])
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
print(arr) """

# using built-in funcstion
""" arr = [1, 2, 3, 4, 5]
arr.reverse()   #note the inbuilt function is an permanent option
print(arr)
 """

# using while loop
arr = [1, 2, 3, 4, 5]
start = 0
end = len(arr) - 1
while end > start:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)
