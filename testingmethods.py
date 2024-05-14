import random
import time 
import pandas as pd

def bubble_sort(list_of_numbers):
    # Get the number of elements in the list
    n = len(list_of_numbers)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so the inner loop can avoid looking at the last i elements
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if list_of_numbers[j] > list_of_numbers[j+1]:
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
    # Return the sorted list
    return list_of_numbers

def selection_sort(list_of_numbers):
    # Iterate over each element in the list
    for i in range(len(list_of_numbers)):
        # Assume the first element is the minimum
        min_idx = i
        # Check the rest of the array for a smaller element
        for j in range(i+1, len(list_of_numbers)):
            # If a smaller element is found, update min_idx
            if list_of_numbers[j] < list_of_numbers[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        list_of_numbers[i], list_of_numbers[min_idx] = list_of_numbers[min_idx], list_of_numbers[i]
    # Return the sorted list
    return list_of_numbers

def insertion_sort(list_of_numbers):
    # Iterate from the second element of the list
    for i in range(1, len(list_of_numbers)):
        # The current element to be inserted into the sorted portion of the array
        key = list_of_numbers[i]
        # Start comparing with the element just before the current element
        j = i-1
        # Move elements of list_of_numbers[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < list_of_numbers[j]:
            list_of_numbers[j+1] = list_of_numbers[j]
            j -= 1
        # Insert the key at after the element just smaller than it.
        list_of_numbers[j+1] = key
    return list_of_numbers

def bucket_sort(list_of_numbers):
    if len(list_of_numbers) == 0:
        return list_of_numbers

    # Find minimum and maximum values
    min_value = min(list_of_numbers)
    max_value = max(list_of_numbers)

    # Number of buckets
    bucket_count = len(list_of_numbers)

    # Create buckets
    buckets = [[] for _ in range(bucket_count)]

    # Assign numbers into buckets
    for i in range(len(list_of_numbers)):
        index = int(((list_of_numbers[i] - min_value) / (max_value - min_value)) * (bucket_count - 1))
        buckets[index].append(list_of_numbers[i])

    # Sort buckets and concatenate
    sorted_list = []
    for i in range(len(buckets)):
        buckets[i].sort()
        sorted_list.extend(buckets[i])

    return sorted_list

def merge_sort(arr):
    # If the array has more than one element
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)

        # Initializing index variables
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # Checking if the element of the first half is smaller than the second half
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left in L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Checking if any element was left in R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    # Return the sorted array
    return arr

def test_sort(input, sort_func):
    start = time.time()
    sort_func(input)
    end = time.time()
    return end - start
    
bubble_sort_time = []
selection_sort_time = []
insertion_sort_time = []
bucket_sort_time = []
merge_sort_time = []
print("Running tests...")
start = time.time()
for i in range(500):
    print("Test", i+1)
    list_of_numbers = [random.randint(0, 1000) for i in range(10000)]
    list_of_numbers_mst = list_of_numbers.copy()
    bubble_sort_time.append(test_sort(list_of_numbers, bubble_sort))
    selection_sort_time.append(test_sort(list_of_numbers, selection_sort))
    list_of_numbers = list_of_numbers_mst.copy()
    insertion_sort_time.append(test_sort(list_of_numbers, insertion_sort))
    bucket_sort_time.append(test_sort(list_of_numbers, bucket_sort))
    merge_sort_time.append(test_sort(list_of_numbers, merge_sort))
end = time.time()
    
    
    
results = {
    'Bubble Sort': bubble_sort_time,
    'Selection Sort': selection_sort_time,
    'Insertion Sort': insertion_sort_time,
    'Bucket Sort': bucket_sort_time,
    'Merge Sort': merge_sort_time
}

df = pd.DataFrame(results)
print("Tests completed in", end-start, "seconds")
df.to_csv('sortingmethods.csv', index= True)