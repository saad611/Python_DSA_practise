def first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            result = mid
            right = mid - 1  # Move left to find the first occurrence
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

def last_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            result = mid
            left = mid + 1  # Move right to find the last occurrence
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example
arr = [1, 2, 4, 4, 4, 5, 6]
x = 4
print(first_occurrence(arr, x))  # Output: 2
print(last_occurrence(arr, x))   # Output: 4
