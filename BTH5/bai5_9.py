# binary_search.py
def binary_search(lst, value):
    """
    Hàm tìm kiếm nhị phân (binary search) trên một danh sách đã được sắp xếp.

    :param lst: Danh sách đã sắp xếp
    :param value: Giá trị cần tìm
    :return: True nếu tìm thấy giá trị, False nếu không tìm thấy
    """
    lower_bound = 0
    upper_bound = len(lst) - 1

    while lower_bound <= upper_bound:
        mid_point = lower_bound + (upper_bound - lower_bound) // 2

        if lst[mid_point] < value:
            lower_bound = mid_point + 1
        elif lst[mid_point] > value:
            upper_bound = mid_point - 1
        else:
            return True  # Tìm thấy giá trị

    return False  # Không tìm thấy giá trị
