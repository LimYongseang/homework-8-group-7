from exercise_3 import remove_all_after

# test normal
def test_remove_all_after():
    assert remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]
    
# test empty
def test_remove_all_after():
    assert remove_all_after([],0) == []
    assert remove_all_after([],3) == []

def test_remove_all_after():
    assert remove_all_after([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    assert remove_all_after([0, 4, 5, 6, 6,], 1) == [0, 4, 5, 6, 6,]