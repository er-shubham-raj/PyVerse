# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Increment the index
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partitioning index

# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        # Find the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort the two halves
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Driver code to test the algorithm
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    
    quick_sort(arr, 0, len(arr) - 1)
    
    print("Sorted array:", arr)
