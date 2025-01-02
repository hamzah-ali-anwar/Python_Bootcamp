def find_missing_elements(arr):

    # create a complete range from the first to the last element in the input array
    full_range = set(range(arr[0], arr[-1] +1))

    # convert the input aray to a set for efficient lookup
    arr_set = set(arr)

    # find the missing elements by subtracting the input array set from the full range set
    missing_elements = sorted(list(full_range - arr_set))

    return missing_elements

arr = [1, 2, 3, 4, 7, 8, 10]

missing_elements = find_missing_elements(arr)
print(missing_elements)
