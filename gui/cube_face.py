from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout


class CubeFace(QWidget):

    def __init__(self, face_name):
        super().__init__()

        self.face_name = face_name

        self.layout = QGridLayout()
        self.layout.setSpacing(2)

        self.stickers = []

        for row in range(3):
            row_buttons = []

            for col in range(3):

                button = QPushButton()

                button.setFixedSize(45, 45)

                color = "white"

                if row == 1 and col == 1:

                    center_colors = {
                        "U": "white",
                        "D": "yellow",
                        "F": "green",
                        "B": "blue",
                        "R": "red",
                        "L": "orange"
                    }

                    color = center_colors[face_name]

                button.setStyleSheet(
                    f"""
                    background-color:{color};
                    border:1px solid #444;
                    """
                )

                self.layout.addWidget(button, row, col)

                row_buttons.append(button)

            self.stickers.append(row_buttons)

        self.setLayout(self.layout)