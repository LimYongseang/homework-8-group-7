from exercise_5 import reverse_ascending

# test normal output
def test_reverse_ascending():
    assert reverse_ascending([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]) == [
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
    assert test_reverse_ascending([3, 1, 2, 3, 2, 4, 5, 6, 2]) == [
        3,
        3,
        2,
        1,
        6,
        5,
        4,
        2,
        2,
    ]

def test_reverse_ascending():
    assert reverse_ascending([]) == []

