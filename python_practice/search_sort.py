"""Basic searching and sorting algorithms. Run: python search_sort.py"""


def linear_search(items, target):
    """Return the index of target, or -1 if it is not present."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binary_search(sorted_items, target):
    """Binary search on an already-sorted list; return index or -1."""
    left, right = 0, len(sorted_items) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def bubble_sort(items):
    """Return a sorted copy using bubble sort."""
    result = items.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    numbers = [29, 10, 14, 37, 13]
    sorted_numbers = bubble_sort(numbers)

    print("Original list:", numbers)
    print("Bubble sort:", sorted_numbers)
    print("Linear search for 14 in original list:", linear_search(numbers, 14))
    print("Binary search for 14 in sorted list:", binary_search(sorted_numbers, 14))
    print("Search for 99:", linear_search(numbers, 99))
