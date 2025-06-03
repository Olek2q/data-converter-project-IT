import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from converter import convert_file
from threading import Thread


class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Converter')
        self.setGeometry(300, 300, 400, 200)
    def convert_async(self):
        Thread(target=self.convert_files).start()

    def convert_files(self):
        try:
            convert_file(self.input_file, self.output_file)
        except Exception as e:
            print(f"Błąd: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())