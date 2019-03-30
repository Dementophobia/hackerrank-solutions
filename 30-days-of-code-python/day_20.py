def bubbleSort(arr):
    count = 0
    for iteration in range(1, len(arr)):
        for i in range(len(arr)-iteration):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
    return count, arr[0], arr[-1]

n = int(input())
a = list(map(int, input().split()))

count, first, last = bubbleSort(a)

print(f"Array is sorted in {count} swaps.")
print(f"First Element: {first}")
print(f"Last Element: {last}")