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

                button = QPushButton()

                button.current_color = color
                button.is_center = (row == 1 and col == 1)

                button.setFixedSize(45, 45)

                button.setStyleSheet(
                    f"""
                    background-color:{color};
                    border:1px solid #444;
                    """
                )

                button.clicked.connect(
                    lambda checked, btn=button:
                    self.sticker_clicked(btn)
                )

                self.layout.addWidget(button, row, col)

                row_buttons.append(button)

            self.stickers.append(row_buttons)

        self.setLayout(self.layout)

    def sticker_clicked(self, button):

        if button.is_center:
            return

        parent_editor = self.parent()

        while parent_editor:

            if hasattr(parent_editor, "palette"):
                break

            parent_editor = parent_editor.parent()

        if not parent_editor:
            return

        selected_color = parent_editor.palette.selected_color

        button.current_color = selected_color

        button.setStyleSheet(
            f"""
            background-color:{selected_color};
            border:1px solid #444;
            """
        )