import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QVBoxLayout, 
    QWidget, 
    QPushButton, 
    QDialog)
from PyQt5.QtCore import QSize, Qt

styles = """
    QWidget {
        border: none;
        background-color: #FFFFFF;
    }

    QPushButton {
        background-color: #1d78e2;
        color: #FFFFFF;
        font-size: 14px;
        min-width: 150px;
        min-height: 40px;
        border: none;
        border-radius: 20px;
    }
    QPushButton:hover {
        background-color: #ef9103;
    }
    QPushButton:presed {
        background-color: #1968c4;
    }
"""


class PyQAndroid(QMainWindow):
    def __init__(self, **kwargs):
        super(PyQAndroid, self).__init__(**kwargs)
        self.setMinimumSize(QSize(500, 600))
        self.setWindowTitle("PyQt6 on android")
        self.setStyleSheet(styles)

        widget = QWidget()

        button = QPushButton("Show details")
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.clicked.connect(self.showDialog)

        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(20, 20, 20, 20)
        lay.addWidget(button)

        widget.setLayout(lay)

        self.setCentralWidget(widget)
    
    def showDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Info")
        dialog.setFixedSize(QSize(250, 150))
        label = QLabel("Hi 👋, I'm PyQt running on Android")
        bLay = QVBoxLayout()
        bLay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bLay.setContentsMargins(20, 20, 20, 20)
        bLay.addWidget(label)
        dialog.setLayout(bLay)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyQAndroid()
    win.show()
    sys.exit(app.exec_())

# install python 3.11.0 32bits (x86)
# sip-6.7.11 = pip install sip
# PyQt-builder-1.15.2 = pip install PyQt-builder
# instal perl = https://strawberryperl.com/

# https://github.com/kviktor/pyqtdeploy-android-build
