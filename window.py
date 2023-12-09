from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from reader import get_element_data

class PeriodicTable(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Periodic Table')
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.image_label = QLabel(main_widget)
        self.element_number_input = QLineEdit(main_widget)
        self.result_label = QLabel(main_widget)
        self.get_element_data_button = QPushButton('Получить данные', main_widget)
        self.get_element_data_button.clicked.connect(self.show_element_data)

        layout = QVBoxLayout(main_widget)
        layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.element_number_input, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.get_element_data_button, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.result_label)

        self.load_image('image\Periodic_table.png')

    def show_element_data(self):
        element_number = self.element_number_input.text()
        element_data = get_element_data(element_number)

        if element_data:
            formatted_data = (
                "Atomic Number: {}\n"
                "Symbol: {}\n"
                "Element: {}\n"
                "Origin of Name: {}\n"  
                "Group: {}\n"
                "Period: {}\n"
                "Atomic Weight: {}\n"
                "Density: {}\n"
                "Melting Point: {}\n"
                "Boiling Point: {}\n"
                "Specific Heat Capacity: {}\n"
                "Electronegativity: {}\n"
                "Abundance in Earth's Crust: {}\n"
            ).format(
                element_data['Atomic_number'],
                element_data['Symbol'],
                element_data['Element'],
                element_data['Origin_of_name'],  
                element_data['Group'],
                element_data['Period'],
                element_data['Atomic_weight'],
                element_data['Density'],
                element_data['Melting_point'],
                element_data['Boiling_point'],
                element_data['Specific_heat_capacity'],
                element_data['Electronegativity'],
                element_data['Abundance_in_earth\'s_crust']
            )

            self.result_label.setText(formatted_data)
        else:
            self.result_label.setText('Элемент не найден')


    def load_image(self, path):
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(960, 462, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)