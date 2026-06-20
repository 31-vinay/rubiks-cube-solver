from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
)

class CubeEditor(QWidget):

    def __init__(self):
        super().__init__()

        self.selected_color = "white"

        main_layout = QVBoxLayout()

        title = QLabel("Cube Face Editor")
        title.setStyleSheet("""
            color: white;
            font-size: 20px;
            font-weight: bold;
        """)

        main_layout.addWidget(title)

        # 3x3 Sticker Grid
        self.grid_layout = QGridLayout()
        self.stickers = []

        for row in range(3):
            for col in range(3):

                sticker = QPushButton()

                sticker.setFixedSize(70, 70)

                sticker.setStyleSheet("""
                    background-color: white;
                    border: 2px solid #444;
                """)

                sticker.clicked.connect(
                    lambda checked, btn=sticker:
                    self.paint_sticker(btn)
                )

                self.grid_layout.addWidget(sticker, row, col)

                self.stickers.append(sticker)

        main_layout.addLayout(self.grid_layout)

        # Color Palette
        palette_layout = QHBoxLayout()

        colors = [
            "white",
            "yellow",
            "red",
            "orange",
            "blue",
            "green"
        ]

        for color in colors:

            color_btn = QPushButton()

            color_btn.setFixedSize(40, 40)

            color_btn.setStyleSheet(
                f"background-color: {color};"
            )

            color_btn.clicked.connect(
                lambda checked, c=color:
                self.set_color(c)
            )

            palette_layout.addWidget(color_btn)

        main_layout.addLayout(palette_layout)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#121212;
            }
        """)

    def set_color(self, color):
        self.selected_color = color

    def paint_sticker(self, sticker):
        sticker.setStyleSheet(
            f"""
            background-color:{self.selected_color};
            border:2px solid #444;
            """
        )