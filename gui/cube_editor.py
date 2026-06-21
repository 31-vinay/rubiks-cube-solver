from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
)

from cube_face import CubeFace
from color_palette import ColorPalette
from PyQt6.QtWidgets import QPushButton

class CubeEditor(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        title = QLabel("Rubik's Cube Net")

        title.setStyleSheet("""
            color:white;
            font-size:20px;
            font-weight:bold;
        """)

        main_layout.addWidget(title)

        self.palette = ColorPalette()

        content_layout = QHBoxLayout()

        cube_net = QGridLayout()

        self.up = CubeFace("U")
        self.left = CubeFace("L")
        self.front = CubeFace("F")
        self.right = CubeFace("R")
        self.back = CubeFace("B")
        self.down = CubeFace("D")

        self.up.setParent(self)
        self.left.setParent(self)
        self.front.setParent(self)
        self.right.setParent(self)
        self.back.setParent(self)
        self.down.setParent(self)

        cube_net.addWidget(self.up, 0, 1)

        cube_net.addWidget(self.left, 1, 0)
        cube_net.addWidget(self.front, 1, 1)
        cube_net.addWidget(self.right, 1, 2)
        cube_net.addWidget(self.back, 1, 3)

        cube_net.addWidget(self.down, 2, 1)

        content_layout.addWidget(self.palette)
        content_layout.addLayout(cube_net)

        main_layout.addLayout(content_layout)

        self.reset_button = QPushButton("Reset Cube")

        self.reset_button.setStyleSheet("""
            QPushButton{
                background-color:#ef4444;
                color:white;
                border:none;
                border-radius:8px;
                padding:10px;
                font-size:14px;
            }

            QPushButton:hover{
                background-color:#dc2626;
            }
        """)

        self.reset_button.clicked.connect(self.reset_cube)

        main_layout.addWidget(self.reset_button)

        self.state_button = QPushButton("Generate State")

        self.state_button.setStyleSheet("""
            QPushButton{
                background-color:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:10px;
                font-size:14px;
            }

            QPushButton:hover{
                background-color:#1D4ED8;
            }
        """)

        self.state_button.clicked.connect(self.generate_state)

        main_layout.addWidget(self.state_button)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#121212;
            }
        """)
    def reset_cube(self):

        faces = [
            self.up,
            self.left,
            self.front,
            self.right,
            self.back,
            self.down
        ]

        center_colors = {
            "U": "white",
            "D": "yellow",
            "F": "green",
            "B": "blue",
            "R": "red",
            "L": "orange"
        }

        for face in faces:

            for row in range(3):

                for col in range(3):

                    sticker = face.stickers[row][col]

                    if sticker.is_center:

                        color = center_colors[face.face_name]

                    else:

                        color = "white"

                    sticker.current_color = color

                    sticker.setStyleSheet(
                        f"""
                        background-color:{color};
                        border:1px solid #444;
                        """
                    )

    def generate_state(self):

        faces = [
            self.up,
            self.right,
            self.front,
            self.down,
            self.left,
            self.back
        ]

        color_to_face = {
            "white": "U",
            "red": "R",
            "green": "F",
            "yellow": "D",
            "orange": "L",
            "blue": "B"
        }

        cube_state = ""

        for face in faces:

            for row in face.stickers:

                for sticker in row:

                    cube_state += color_to_face[
                        sticker.current_color
                    ]

        print("\nCube State:")
        print(cube_state)

        print("\nLength:")
        print(len(cube_state))