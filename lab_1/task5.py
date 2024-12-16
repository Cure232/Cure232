from typing import Optional

from task1 import scan_dataset
from task2 import scan_annotation


class ClassedAnnotationIterator:
    columns = []
    def __init__(self, class_name: str, annotation_path: str) -> None:
        """Initializes Iterator that can iterate through given annotation
        returning only items of given class.

        Args:
            class_name (str): Preffered item class.
            annotation_path (str): Path to annotation.
        """
        self.counter = 0
        self.class_name = class_name
        self.data = scan_annotation(annotation_path)
        self.columns = self.data.pop(0)
        self.limit = len(self.data)

    def __iter__(self):
        """Returns the Iterator object itself.
        """
        return self
    
    def __next__(self) -> Optional[str]:
        """Returns next image of Iterator's class

        Returns:
            Optional[str]: Returns either absolute path to image or None
        """
        while self.counter < self.limit:
            if self.data[self.counter][-1].upper() == self.class_name.upper():
                self.counter += 1
                return self.data[self.counter - 1][0]
            self.counter += 1
        raise StopIteration
    

class ClassedDatasetIterator:
    data = []
    def __init__(self, class_name: str, dataset_paths: list[str]) -> None:
        """Initializes Iterator that can iterate through given annotation
        returning only items of given class.

        Args:
            class_name (str): Preffered item class.
            annotation_path (str): Path to annotation.
        """
        self.counter = 0
        self.class_name = class_name
        self.data = scan_dataset(dataset_paths)
        self.limit = len(self.data)

    def __iter__(self):
        """Returns the Iterator object itself.
        """
        return self
        
    def __next__(self) -> Optional[str]:
        """Returns next image of Iterator's class

        Returns:
            Optional[str]: Returns either absolute path to image or None
        """
        while self.counter < self.limit:
            if self.data[self.counter][-1].upper() == self.class_name.upper():
                self.counter += 1
                return self.data[self.counter - 1][0]
            self.counter += 1
        raise StopIteration


if __name__ == '__main__':
    s_iter1 = ClassedAnnotationIterator("zebra", "new_annotation_task3.csv")
    for i in s_iter1:
        print(i)
    
    s_iter2 = ClassedDatasetIterator(
        "bay horse", 
        ["dataset\\bay horse", "dataset\\zebra"]
    )
    print(next(s_iter2))
    print(next(s_iter2))
    print(next(s_iter2))
