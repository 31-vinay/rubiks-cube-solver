from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout


class ColorPalette(QWidget):

    def __init__(self):
        super().__init__()

        self.selected_color = "white"

        layout = QVBoxLayout()

        colors = [
            "white",
            "yellow",
            "red",
            "orange",
            "blue",
            "green"
        ]

        for color in colors:

            btn = QPushButton()

            btn.setFixedSize(50, 50)

            btn.setStyleSheet(
                f"""
                background-color:{color};
                border:2px solid #444;
                """
            )

            btn.clicked.connect(
                lambda checked, c=color:
                self.set_color(c)
            )

            layout.addWidget(btn)

        self.setLayout(layout)

    def set_color(self, color):

        self.selected_color = color

        print("Selected:", color)