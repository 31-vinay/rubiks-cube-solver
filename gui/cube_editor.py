from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
)

from cube_face import CubeFace
from color_palette import ColorPalette

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

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#121212;
            }
        """)