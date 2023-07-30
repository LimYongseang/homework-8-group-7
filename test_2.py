from exercise_2 import index_power


# test normal
def test_index_power():
    assert index_power([1, 2, 3, 4], 2) == 9
    assert index_power([1, 3, 10, 100], 3) == 1000000
    assert index_power([0, 1], 0) == 1


# test index outside the list
def test_index_power():
    assert index_power([1, 2], 3) == -1
    assert index_power([1, 3, 6, 7, 8], 19) == -1


# test 0
def test_index_power():
    assert index_power([1, 2, 3, 4], 0) == 1
    assert index_power([0, 1], 0) == 1
