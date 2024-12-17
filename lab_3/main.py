import re
import csv

from typing import Optional, List

from config import path, regex_patterns
from checksum import calculate_checksum


def csv_to_list(file_path: str) -> Optional[List[List[str]]]:
    """
    Reads a CSV file and returns its content as a list of rows, excluding the header.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        Optional[List[List[str]]]: List of rows (each as a list of strings) or None on error.
    """
    try:
        with open(file_path, mode="r", encoding="utf-16") as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            return [row for row in reader]
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}.")
        return None


def is_valid_line(pattern: dict, row: List[str]) -> bool:
    """
    Checks if a row matches the given regular expression patterns.

    Args:
        pattern (dict): Dictionary of regex patterns.
        row (List[str]): Row to validate.

    Returns:
        bool: True if the row matches all patterns, otherwise False.
    """
    return all(re.match(pattern[key], data) for key, data in zip(pattern.keys(), row))


def get_invalid_occurences(pattern: dict, data: List[List[str]]) -> Optional[List[int]]:
    """
    Returns indices of rows that fail validation.

    Args:
        pattern (dict): Regex patterns for validation.
        data (List[List[str]]): List of rows to check.

    Returns:
        Optional[List[int]]: List of indices of invalid rows, or None on error.
    """
    invalid_occurences = [i for i, row in enumerate(data) if not is_valid_line(pattern, row)]
    return invalid_occurences


if __name__ == '__main__':
    check_list = []
    data = csv_to_list(path)
    check_list = get_invalid_occurences(regex_patterns, data)
    print(len(check_list))
    print(calculate_checksum(check_list))