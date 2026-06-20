import sys
from PyQt6.QtWidgets import (
QApplication,
QWidget,
QLabel,
QPushButton,
QVBoxLayout
)
from PyQt6.QtCore import Qt

class CubeSolverGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rubik's Cube Solver")
        self.resize(800, 500)

        title = QLabel("Rubik's Cube Solver")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: white;
            padding: 20px;
        """)

        self.scan_button = QPushButton("Scan Cube")
        self.solve_button = QPushButton("Solve Cube")

        button_style = """
            QPushButton{
                background-color:#3B82F6;
                color:white;
                border:none;
                border-radius:10px;
                padding:12px;
                font-size:16px;
            }

            QPushButton:hover{
                background-color:#2563EB;
            }
        """

        self.scan_button.setStyleSheet(button_style)
        self.solve_button.setStyleSheet(button_style)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addStretch()

        layout.addWidget(self.scan_button)
        layout.addWidget(self.solve_button)

        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#121212;
            }
        """)

app = QApplication(sys.argv)

window = CubeSolverGUI()
window.show()

sys.exit(app.exec())
