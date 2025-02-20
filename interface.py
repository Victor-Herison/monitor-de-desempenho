from turtledemo.nim import COLOR

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a tittle
        self.setWindowTitle("my screen")
        # layout
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel('hello guys')
        self.layout().addWidget(my_label)

app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec()