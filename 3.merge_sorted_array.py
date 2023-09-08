def mergeSortedArrays(arr1, arr2):
    # Create a third array by adding arr1 and arr2
    merged = arr1 + arr2

    # Sort the merged array
    merged.sort()

    # Split the sorted array back into arr1 and arr2 with original sizes
    arr1[:] = merged[:len(arr1)]
    arr2[:] = merged[len(arr1):]

# Driver code to test the mergeSortedArrays function
if __name__ == "__main__":
    arr1 = [1, 5, 9, 10, 15, 20]
    arr2 = [2, 3, 8, 13]

    mergeSortedArrays(arr1, arr2)

    print("Merged arr1:", arr1)
    print("Remaining arr2:", arr2)
