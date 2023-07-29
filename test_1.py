from exercise_1 import replace_last

# test normal 
def test_replace_last():
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]

# test empty list
def test_replace_last():
    assert replace_last([]) == []

# test one-element-list
def test_replace_last():
    assert replace_last([1]) == [1]
    assert replace_last([2]) == [2]
    assert replace_last([13]) == [13]

# test two-element-list
def test_replace_last():
    assert replace_last([1, 2]) == [2, 1]
    assert replace_last([9, 8]) == [8, 9]
    assert replace_last([0, 3]) == [3, 0]

