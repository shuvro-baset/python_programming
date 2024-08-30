def remove_duplicates(arr):
    seen = set()
    result_array = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result_array.append(num)

    print(result_array)


remove_duplicates([1, 1, 1, 3, 4, 1, 2, 10, 9])