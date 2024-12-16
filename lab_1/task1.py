import os

import pandas as pd


def save_as_csv(to_save: list[list[str]], columns: list[str], relpath: str) -> None:
    """Saves given data table as csv

    Args:
        to_save (list[list[str]]): Table (matrix) of strings to be saved,
        formatted as in scan_dataset.

        columns (list[str]): Name of data's columns.

        relpath (str): Relative path where data is to be saved.
    """
    df = pd.DataFrame(to_save, columns=columns)
    df.to_csv(relpath, sep=";")
    print(f'Successfully saved in {relpath}')


def scan_dataset(folder_paths: list[str]) -> list[list[str]]:
    """This function scans given datasets and returns them in a form 
    that can be saved as csv.

    Args:
        folder_paths (list[str]): Paths to datasets to be scanned.

    Returns:
        list[list[str]]: Data in a form of table of strings.
    """
    result = []
    for folder in folder_paths:
        item_class = folder.split('\\')[-1]
        for name in os.listdir(folder):
            result.append([
                os.path.abspath(folder + '\\' + name),
                    f'{folder}\\{name}',
                    item_class
                ])
    return result


if __name__ == "__main__":
    rel_path1 = r'dataset\bay horse'
    rel_path2 = r'dataset\zebra'

    columns = ["Absolute path", "Relative path", "Class"]
    data = scan_dataset([rel_path1, rel_path2])
    #save_as_csv(data, columns, 'annotation.csv')

    new_data1 = data[:2]
    new_data2 = data[:4]
    new_data1 += new_data2
    print(new_data1)



    