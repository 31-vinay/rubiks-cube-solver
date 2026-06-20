import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class CubeSolverGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rubik's Cube Solver")
        self.setGeometry(100, 100, 500, 300)

        self.title = QLabel("Rubik's Cube Solver")

        self.scan_button = QPushButton("Scan Cube")
        self.solve_button = QPushButton("Solve Cube")

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.scan_button)
        layout.addWidget(self.solve_button)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = CubeSolverGUI()
window.show()

sys.exit(app.exec())