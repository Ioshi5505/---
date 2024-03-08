import sys
from PySide6.QtGui import QIcon, QFont, QPixmap, QPainter, QPalette, QColor
from PySide6.QtGui import QIcon, QFont, QPixmap, QPalette
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel,
                               QComboBox, QHBoxLayout)
from PySide6.QtGui import QIcon, QFont, QPixmap, QPainter
from PySide6.QtCore import Qt
from PIL import Image

class MaximizedImageConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер изображений - Джокер")
        self.setWindowIcon(QIcon("лого.png"))
        self.apply_dark_theme()
        self.create_ui()
        self.showMaximized()

    def create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        header_layout = QHBoxLayout()
        instructions = QLabel("Выберите изображение и целевой формат:")
        instructions.setFont(QFont("Sans Serif", 10))
        header_layout.addWidget(instructions)

        logo_label = QLabel(self)
        logo_pixmap = QPixmap("лого.png")
        logo_label.setPixmap(logo_pixmap)
        header_layout.addWidget(logo_label)

        layout.addLayout(header_layout)

        file_layout = QHBoxLayout()
        self.file_path_label = QLabel("Файл не выбран")
        self.file_path_label.setFont(QFont("Sans Serif", 9))
        self.select_file_button = QPushButton("Выбрать файл")
        self.select_file_button.clicked.connect(self.select_file)
        self.style_button(self.select_file_button, "#007bff", "#ffffff")
        file_layout.addWidget(self.file_path_label)
        file_layout.addWidget(self.select_file_button)
        layout.addLayout(file_layout)

        self.format_selector = QComboBox()
        self.format_selector.addItems(["JPEG", "PNG", "BMP", "GIF", "ICON", "ICO"])
        layout.addWidget(self.format_selector)

        self.convert_button = QPushButton("Конвертировать")
        self.convert_button.clicked.connect(self.convert_image)
        self.style_button(self.convert_button, "#28a745", "#ffffff")
        layout.addWidget(self.convert_button)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Image Files (*.png *.jpeg *.jpg *.bmp *.gif *.ico *.icon)")
        if file_name:
            self.file_path_label.setText(file_name)
            self.selected_file = file_name

    def convert_image(self):
        if hasattr(self, 'selected_file'):
            target_format = self.format_selector.currentText().lower()
            output_file = self.selected_file.rsplit('.', 1)[0] + '.' + (target_format if target_format not in ["icon", "ico"] else "ico")
            try:
                img = Image.open(self.selected_file)
                if target_format in ["icon", "ico"]:
                    img.save(output_file, format="ICO", sizes=[(256, 256)])
                else:
                    img.save(output_file, target_format.upper())
                self.file_path_label.setText(f"Конвертация выполнена: {output_file}")
            except Exception as e:
                self.file_path_label.setText(f"Ошибка: {e}")

    def style_button(self, button, background_color, text_color):
        button.setStyleSheet(f"QPushButton {{background-color: {background_color}; color: {text_color};}}")

    def apply_dark_theme(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(45, 45, 45))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(dark_palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = MaximizedImageConverter()
    sys.exit(app.exec_())

