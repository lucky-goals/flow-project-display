from src.bubble_sort import bubble_sort


def test_unsorted_list():
    assert bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_already_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_list_with_duplicates():
    assert bubble_sort([5, 3, 3, 1, 2, 2]) == [1, 2, 2, 3, 3, 5]
