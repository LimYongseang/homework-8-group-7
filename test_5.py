from exercise_5 import reverse_ascending

# test normal output
def test_reverse_ascending():
    assert reverse_ascending([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_ascending([12, 34, 21, 51, 55]) == [55, 51, 34, 21, 12]
    assert reverse_ascending(
        [
            9,
            7,
            8,
            4,
            5,
        ]
    ) == [9, 8, 7, 5, 4]
    assert reverse_ascending([1, 2, 3, 4, 5, 6, 7, 7, 8]) == [8, 7, 7, 6, 5, 4, 3, 2, 1]

