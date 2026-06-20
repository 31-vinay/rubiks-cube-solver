from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel
)

from cube_face import CubeFace


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

        cube_net = QGridLayout()

        self.up = CubeFace("U")
        self.left = CubeFace("L")
        self.front = CubeFace("F")
        self.right = CubeFace("R")
        self.back = CubeFace("B")
        self.down = CubeFace("D")

        cube_net.addWidget(self.up, 0, 1)

        cube_net.addWidget(self.left, 1, 0)
        cube_net.addWidget(self.front, 1, 1)
        cube_net.addWidget(self.right, 1, 2)
        cube_net.addWidget(self.back, 1, 3)

        cube_net.addWidget(self.down, 2, 1)

        main_layout.addLayout(cube_net)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#121212;
            }
        """)