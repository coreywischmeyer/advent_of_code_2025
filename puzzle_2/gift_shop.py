from pathlib import Path
def id_check(product_id) -> bool:
    """
    Check if product id is valid.

    Parameters
    ----------
    product_id : int

    Returns
    -------
    bool
        Whether product id is valid.
    """
    size = 0
    result = product_id
    while result != 0:
        size += 1
        dividend = 10**size
        result = product_id // dividend
    if size % 2 != 0:
        return True
    left_dividend = 10 ** (size / 2)
    right_dividend = 10 ** (size - 1)
    left = int(product_id // left_dividend)
    right = int(product_id % left_dividend)
    if left == right:
        return False
    else:
        return True


def find_invalid_ids(start, stop) -> list[int]:
    """
    find invalid ids in range.

    Parameters
    ----------
    start : int
    stop : int

    Returns
    -------
    list[int]
        Invalid ids in range.
    """
    invalid_ids = []
    for i in range(start, stop + 1):
        if not id_check(i):
            invalid_ids.append(i)
    return invalid_ids

def find_and_sum_invalid_ids(input: str) -> int:
    data = input.split(',')
    invalid_id_sum = 0
    for item in data:
        start, stop = item.split('-')
        invalid_id_sum += sum(find_invalid_ids(int(start), int(stop)))
    return invalid_id_sum

if __name__ == "__main__":

    input_data = (Path('data') / 'data.txt').read_text()
    print(find_and_sum_invalid_ids(input_data))
