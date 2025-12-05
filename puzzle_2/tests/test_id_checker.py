import pytest

from puzzle_2.gift_shop import id_check, find_invalid_ids, find_and_sum_invalid_ids


@pytest.mark.parametrize(
    "id,is_valid",
    [
        (11, False),
        (22, False),
        (99, False),
        (1010, False),
        (1188511885, False),
        (12, True),
        (13, True),
        (313, True),
    ],
)
def test_id_check(id, is_valid):
    assert id_check(id) == is_valid


@pytest.mark.parametrize(
    "start,stop,id_list",
    [
        (11, 22, [11, 22]),
        (95, 115, [99]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (38593856, 38593862, [38593859]),
    ],
)
def test_find_invalid_ids(start, stop, id_list):
    assert find_invalid_ids(start, stop) == id_list


def test_sum_invalid_ids():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    assert find_and_sum_invalid_ids(input) == 1227775554
