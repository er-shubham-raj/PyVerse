# Function to perform binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is at mid
        if arr[mid] == target:
            return mid  # Target found, return index

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # If target is not found, return -1
    return -1

# Driver code to test the function
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10

    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")
