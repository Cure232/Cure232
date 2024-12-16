from task2 import scan_annotation

counters = dict()
counters['BAY HORSE'] = 0
counters['ZEBRA'] = 0


def get_next_item_path(item_class: str) -> str:
    """Returns path to next item of given class.

    Args:
        item_class (str): Preferred class. 

    Returns:
        str: Path to next item of given class.
    """
    item_class = item_class.upper()
    counter = 0
    for item in data:
        if item[2].upper() == item_class:
            if counter == counters[item_class]:
                counters[item_class] += 1
                return item[1]
            else:
                counter += 1


if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    data.pop(0)
    print(get_next_item_path("ZEBRA"))
    print(get_next_item_path("ZEBRA"))
    print(get_next_item_path("Bay horse"))
    print(get_next_item_path("ZEBRA"))
    print(get_next_item_path("Bay horse"))
    print(get_next_item_path("Bay horse"))
