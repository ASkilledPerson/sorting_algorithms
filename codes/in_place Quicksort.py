# Python implementation of in-place quicksort, inspired by the textbook Data Structures and Algorithms

def in_place_quick_sort(S, a, b):
    """
    Sort the list from S[a] to S[b] inclusive using the quick_sort algorithm.
    :return: None
    """
    if a >= b:  # range is trivially sorted
        return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        # scan until reaching a value equal or larger than pivot
        while left <= right and S[left]<pivot:
            left += 1
        # scan until reaching a value lesser or equal than pivot
        while left <= right and S[right] > pivot:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1

    # put pivot in its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    in_place_quick_sort(S,a, left-1)
    in_place_quick_sort(S, left+1, b)