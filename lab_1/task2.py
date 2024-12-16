import os

import csv
import cv2

from task1 import save_as_csv


def scan_annotation(annotation_path: str) -> list[list[str]]:
    """Scans annotation by path and returns data as a matrix of strings.

    Args:
        annotation_path (str): Path to the annotation you want to scan.

    Returns:
        list[list[str]]: Returns data as matrix of strings
    """
    with open(annotation_path, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        result = []
        for row in filereader:
            row.pop(0)
            result.append(row)
        return result


def copy_dataset(dataset: list[list[str]], copy_path: str) -> list[list[str]]:
    """Copies dataset without columns in given folder without creating additional inner folders.

    Args:
        dataset (list[list[str]]): Data as a table (matrix) of strings without columns.
        copy_path (str): Folder where you copy the dataset.

    Returns:
        list[list[str]]: New dataset with new content.
    """
    # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    result = []

    for row in dataset:
        img_class = row[-1]
        img_name = (row[1].split('\\'))[-1]
        new_img_name = f'{img_class}_{img_name}'
        img = cv2.imread(row[1])
        cv2.imwrite(fr'{copy_path}\{new_img_name}', img)

        result.append([
            os.path.abspath(fr'{copy_path}\{new_img_name}'),
            fr'{copy_path}\{new_img_name}',
            img_class
        ])
        print(row)
        print("Saved successfully")
    
    return result


def dataset_2(annotation_path: str):
    """Creates dataset as in task 2 of lab 2

    Args:
        annotation_path (str): Annotation path.
    """
    data = scan_annotation(annotation_path)
    columns = data.pop(0)
    new_data = copy_dataset(data, 'dataset_2')
    save_as_csv(new_data, columns, 'dataset_2_annotation.csv')
