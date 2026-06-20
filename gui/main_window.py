import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout
)

from cube_editor import CubeEditor


class CubeSolverGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rubik's Cube Solver")
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.editor = CubeEditor()

        layout.addWidget(self.editor)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = CubeSolverGUI()
window.show()

sys.exit(app.exec())