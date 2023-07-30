from exercise_4 import chunking_by


# test normal
def test_chunking_by():
    assert chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
    assert chunking_by([3, 4, 5], 1) == [[3], [4], [5]]
    assert chunking_by([1, 2, 3, 5, 6, 9], 5) == [[1, 2, 3, 5, 6], [9]]


# test 0 chunck
def test_chunking_by():
    assert chunking_by([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert chunking_by([1, 3, 4, 5, 1, 2, 1], 0) == [1, 3, 4, 5, 1, 2, 1]


# test invalid inputs
def test_chunking_by():
    assert chunking_by([1, 2, 4, 6, 6], "a") == [1, 2, 4, 6, 6]
    assert chunking_by([9, 8, 5, 3, 2], "m") == [9, 8, 5, 3, 2]


# test empty list
def test_chunking_by():
    assert chunking_by([], 0) == []
    assert chunking_by([], 3) == []
