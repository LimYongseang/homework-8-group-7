from exercise_5 import reverse_ascending

# test normal output
def test_reverse_ascending():
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]

def test_reverse_ascending():
    assert list(reverse_ascending([])) == []

