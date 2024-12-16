import sys
import os

from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from task5 import ClassedAnnotationIterator, ClassedDatasetIterator
from task1 import save_as_csv, scan_dataset
from task2 import copy_dataset, scan_annotation, dataset_2
from task3 import randomized_dataset_copy, dataset_3


class Window(QMainWindow):
    def __init__(self):
        """
        Данный конструктор вызывает методы для создания окна
        """
        super().__init__()

        self.main_window()
        self.create_iter()
        self.add_menu_bar()

    def main_window(self) -> None:
        """
        Данная функция размещает элементы по макету
        """
        self.setWindowTitle("Images horses and zebras")
        self.setWindowIcon(QIcon("icon/horse_zebra.png"))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("background-color: #FFFFFF;")

        button_horse = QPushButton(" Next horse", self)
        button_horse.setFixedSize(200, 50)
        button_horse.setStyleSheet("QPushButton {background-color: #B8B8FF}")
        button_zebra = QPushButton("Next zebra ", self)
        button_zebra.setFixedSize(200, 50)
        button_zebra.setStyleSheet("QPushButton {background-color: #B8B8FF}")

        pixmap = QPixmap()
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

        box = QHBoxLayout()
        box.addSpacing(1)
        box.addWidget(button_horse)
        box.addWidget(self.label)
        box.addWidget(button_zebra)

        self.centralWidget.setLayout(box)

        button_horse.clicked.connect(self.next_horse)
        button_zebra.clicked.connect(self.next_zebra)

        self.folderpath = ""

        self.showMaximized()

    def create_iter(self) -> None:
        """
        Данная функция создает два объекта-итератора
        """
        self.horse = ClassedDatasetIterator(
            "bay horse", [r"dataset\bay horse"]
        )

        self.zebra = ClassedDatasetIterator(
            "zebra", [r"dataset\zebra"]
        )

    def next_horse(self) -> None:
        """
        Данная функция получает путь к следующему
        изображению horse и размещает на экране
        """
        label_size = self.label.size()
        try: 
            next_image = next(self.horse)
        except StopIteration:
            next_image = None

        if next_image != None:
            img = QPixmap(next_image).scaled(
                label_size, aspectRatioMode=Qt.KeepAspectRatio
            )
            self.label.setPixmap(img)
            self.label.setAlignment(Qt.AlignCenter)
        else:
            self.create_iter()
            self.next_horse()

    def next_zebra(self) -> None:
        """
        Данная функция получает путь к следующему 
        изображению zebra и размещает на экране
        """
        label_size = self.label.size()
        try: 
            next_image = next(self.zebra)
        except StopIteration:
            next_image = None

        if next_image != None:
            img = QPixmap(next_image).scaled(
                label_size, aspectRatioMode=Qt.KeepAspectRatio
            )
            self.label.setPixmap(img)
            self.label.setAlignment(Qt.AlignCenter)
        else:
            self.create_iter()
            self.next_zebra()

    def add_menu_bar(self) -> None:
        """
        Данная функция создает меню и добавляет к нему действия
        """
        menu_bar = self.menuBar()

        self.file_menu = menu_bar.addMenu("&File")
        self.change_action = QAction(QIcon(), "&Choose dataset")
        self.change_action.triggered.connect(self.chooseDataset)
        self.file_menu.addAction(self.change_action)

        self.annotation_menu = menu_bar.addMenu("&Annotation")
        self.create_annot_action = QAction(QIcon(), "&Create annotation")
        self.create_annot_action.triggered.connect(self.create_annotation)
        self.annotation_menu.addAction(self.create_annot_action)

        self.datasets_menu = menu_bar.addMenu("&Datasets")

    def create_annotation(self) -> None:
        """
        Данная функция создает аннотацию для исходного dataset
        """
        dataset_path = str(self.folderpath)
        dataset_path = dataset_path.replace('/', '\\')
        dataset_name = dataset_path.split('\\')[-1]

        self.dataset_name = dataset_name
        if os.path.exists(dataset_path + "\\bay horse") and os.path.exists(dataset_path + "\\zebra"):
            data = scan_dataset([
                dataset_name + "\\bay horse",
                dataset_name + "\\zebra"
            ])
            save_as_csv(
                data, ["Abs Path", "Rel Path", "Item Class"],
                dataset_name + "_annotation.csv"
            )
            
            self.create_database_2_action = QAction(
                QIcon(), "&Create dataset2"
            )
            self.create_database_2_action.triggered.connect(self.createDataset2)
            self.datasets_menu.addAction(self.create_database_2_action)

            self.create_database_3_action = QAction(
            QIcon(), "&Create dataset3"
            )
            self.create_database_3_action.triggered.connect(self.createDataset3)
            self.datasets_menu.addAction(self.create_database_3_action)
        else: 
            print("Выбранная папка не соответствует исходному датасету по формату!")
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Выбранная папка не соответствует исходному датасету по формату!")
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()


    def createDataset2(self) -> None:
        """
        Данная функция создает dataset_2
        """
        dataset_2(self.dataset_name + "_annotation.csv")

    def createDataset3(self) -> None:
        """
        Данная функция создает dataset_3
        """
        dataset_3(self.dataset_name + "_annotation.csv")

    def chooseDataset(self) -> None:
        """
        Данная функция изменяет выбор папки исходного dataset
        """
        self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(
            self, "Select Folder"
        )


def main() -> None:
    """
    Данная функция создает приложение
    """
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
